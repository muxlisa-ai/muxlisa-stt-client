import os
import zipfile
import tempfile
import requests
from typing import Any


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
        response = requests.post(url=self.audio_conversion_url, files={'audio': audio})
        return response.content

    def process_audio_segments(self, audio_content: bytes) -> list[str]:
        with tempfile.NamedTemporaryFile(suffix=".zip", delete=True) as temp_zip:
            temp_zip.write(audio_content)
            temp_zip.flush()

            with tempfile.TemporaryDirectory() as extract_dir:
                self.extract_zip_file(temp_zip.name, extract_dir)
                return self.transcribe_audio_files(extract_dir)

    def extract_zip_file(self, zip_path: str, extract_to: str):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

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
            response = requests.post(
                self.stt_service_url,
                files={"audio": ("audio.wav", audio, "audio/wav")},
                timeout=45
            )
        return response.json().get('text', '')

    def combine_transcriptions(self, transcriptions: list[str]) -> str:
        return " ".join(transcriptions)
