class SpeechToTextError(Exception):
    """Base exception for SpeechToTextProcessor errors."""
    pass


class AudioConversionError(SpeechToTextError):
    """Raised when audio conversion to WAV format fails."""
    def __init__(self, message="Failed to convert audio to WAV format."):
        super().__init__(message)


class AudioProcessingError(SpeechToTextError):
    """Raised when processing audio segments fails."""
    def __init__(self, message="Failed to process audio segments."):
        super().__init__(message)


class ZipExtractionError(SpeechToTextError):
    """Raised when extracting the ZIP file fails."""
    def __init__(self, message="Failed to extract ZIP file."):
        super().__init__(message)


class TranscriptionError(SpeechToTextError):
    """Raised when transcription service fails."""
    def __init__(self, message="Failed to transcribe audio file."):
        super().__init__(message)