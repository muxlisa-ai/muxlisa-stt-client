# 🎤 Speech-to-Text (STT) Client  
*A lightweight Python package for processing and transcribing audio using an external STT service.*  

## 🚀 Features  
✅ **Audio Conversion** – Converts uploaded audio to WAV format optimized for STT  
✅ **Automatic Segmentation** – Splits audio into smaller chunks for better transcription  
✅ **STT Integration** – Sends audio to a speech-to-text (STT) service and retrieves transcriptions  
✅ **Lightweight & Modular** – Can be used in any Python project or Django app  
✅ **Easy Installation** – Install directly from GitHub with `pip`  

---

## 📦 Installation  

### **1. Install via GitHub**  
You can install this package **directly from GitHub** (no need for PyPI):  
```sh
pip install git+https://github.com/yourusername/speech-to-text.git
```

## 🛠 Usage
```python
from muxlisa_stt_client import SpeechToTextProcessor

# Initialize with API endpoints
stt = SpeechToTextProcessor(
    audio_conversion_url="https://api.example.com/convert",
    stt_service_url="https://api.example.com/stt"
)

# Load an audio file
with open("example_audio.mp3", "rb") as audio_file:
    transcription = stt.process_audio(audio_file)

print(transcription)  # Prints transcribed text

```

# 📘 SpeechToTextProcessor - Exceptions Guide

The `SpeechToTextProcessor` class includes custom exceptions to handle errors during speech-to-text (STT) processing. Below is a list of possible exceptions and when they might be raised.

## 🔹 Base Exception

### `SpeechToTextError`
- The base exception for all speech-to-text errors.
- All other exceptions inherit from this class.

## 🔹 Specific Exceptions

### `AudioConversionError`
**Raised when audio conversion to WAV format fails.**  
**Possible causes:**
- Invalid or corrupt audio input.
- Issues with the audio conversion service.

**Example:**
```python
try:
    processor.convert_audio_to_wav(audio)
except AudioConversionError as e:
    print(f"Audio conversion failed: {e}")
```

### `AudioProcessingError`
**Raised when processing audio segments fails (e.g., handling a ZIP file).**  

**Possible causes:**  
- Corrupt ZIP file.  
- Disk-related errors when extracting or reading files.  

**Example:**
```python
try:
    processor.process_audio_segments(audio_bytes)
except AudioProcessingError as e:
    print(f"Error processing audio: {e}")
```

### `ZipExtractionError`
**Raised when extracting a ZIP file fails during processing.**  

**Possible causes:**  
- Invalid or corrupt ZIP archive.  
- Insufficient permissions to extract files.  

**Example:**
```python
try:
    processor.extract_zip_file(zip_path, extract_dir)
except ZipExtractionError as e:
    print(f"ZIP extraction error: {e}")
```

### `ZipExtractionError`
**Raised when extracting a ZIP file fails during processing.**  

**Possible causes:**  
- Invalid or corrupt ZIP archive.  
- Insufficient permissions to extract files.  

**Example:**
```python
try:
    processor.extract_zip_file(zip_path, extract_dir)
except ZipExtractionError as e:
    print(f"ZIP extraction error: {e}")
```

### `TranscriptionError`
**Raised when the transcription service fails to process audio.**  

**Possible causes:**  
- The STT service is down or unreachable.  
- The STT service returns an invalid response.  
- The API request times out.  

**Example:**
```python
try:
    processor.transcribe_audio(file_path)
except TranscriptionError as e:
    print(f"Transcription error: {e}")
```

## 💡 Handling Exceptions
To ensure the program does not crash, use `try-except` blocks to catch and handle these exceptions gracefully.

**Example:**
```python
try:
    processor = SpeechToTextProcessor()
    result = processor.process_audio(audio_file)
    print("Transcription:", result)
except SpeechToTextError as e:
    print(f"Error processing speech-to-text: {e}")
```