import os
import zipfile
import tempfile
import requests

from typing import Any

from .exceptions import AudioConversionError, AudioProcessingError, ZipExtractionError, TranscriptionError


class SpeechToTextProcessor:
    """
    A client for handling speech-to-text (STT) processing.
    """

    def __init__(self, audio_conversion_url: str = None, stt_service_url: str = None):
        self.audio_conversion_url = audio_conversion_url or os.getenv("AUDIO_CONVERSION_ENDPOINT")
        self.stt_service_url = stt_service_url or os.getenv("STT_SERVICE_ENDPOINT")

    def process_audio(self, audio: Any) -> str:
        processed_audio = self.convert_audio_to_wav(audio)
        transcriptions = self.process_audio_segments(processed_audio)
        return self.combine_transcriptions(transcriptions)

    def convert_audio_to_wav(self, audio: Any) -> bytes:
        if not audio:
            raise AudioConversionError("No audio provided for conversion.")

        response = requests.post(url=self.audio_conversion_url, files={'audio': audio})
        if response.status_code != 200:
            raise AudioConversionError(f"Audio conversion service returned status code {response.status_code}.")
        return response.content

    def process_audio_segments(self, audio_content: bytes) -> list[str]:
        try:
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=True) as temp_zip:
                temp_zip.write(audio_content)
                temp_zip.flush()

                with tempfile.TemporaryDirectory() as extract_dir:
                    self.extract_zip_file(temp_zip.name, extract_dir)
                    return self.transcribe_audio_files(extract_dir)

        except (OSError, IOError, zipfile.BadZipFile):
            raise AudioProcessingError("Failed to process audio segments. Possible ZIP corruption.")

    def extract_zip_file(self, zip_path: str, extract_to: str):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        except zipfile.BadZipFile:
            raise ZipExtractionError("Failed to extract ZIP file.")

    def transcribe_audio_files(self, directory: str) -> list[str]:
        transcriptions = []
        for file_name in sorted(os.listdir(directory)):
            if file_name.endswith('.wav'):
                file_path = os.path.join(directory, file_name)
                transcription = self.transcribe_audio(file_path)
                transcriptions.append(transcription)
        return transcriptions

    def transcribe_audio(self, file_path: str) -> str:
        with open(file_path, "rb") as audio:
            try:
                response = requests.post(
                    self.stt_service_url,
                    files={"audio": ("audio.wav", audio, "audio/wav")},
                    timeout=45
                )
                if response.status_code != 200:
                   raise TranscriptionError(
                    f"STT service returned status code {response.status_code}: {response.text}"
                )

                return response.json().get('text', '')

            except requests.exceptions.RequestException:
                raise TranscriptionError("Request to STT endpoint failed.")

    def combine_transcriptions(self, transcriptions: list[str]) -> str:
        return " ".join(transcriptions)
