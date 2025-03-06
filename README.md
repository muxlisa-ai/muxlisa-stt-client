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
from stt_client import STTClient

# Initialize with API endpoints
stt = STTClient(
    audio_conversion_url="https://api.example.com/convert",
    stt_service_url="https://api.example.com/stt"
)

# Load an audio file
with open("example_audio.mp3", "rb") as audio_file:
    transcription = stt.process_audio(audio_file)

print(transcription)  # Prints transcribed text

```