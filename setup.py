from setuptools import setup, find_packages

setup(
    name="muxlisa_speech_to_text",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    description="A simple Muxlisa AI STT client for processing and transcribing audio.",
    author="Muzaffar Sabitjanov",
    author_email="msabitjanov1@gmail.com",
    url="https://github.com/muxlisa-ai/muxlisa-stt-client.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)