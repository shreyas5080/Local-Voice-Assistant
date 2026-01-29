# 🤖 Local-AI-Voice-Assistant (Llama 3.2 + Faster-Whisper)

A fully offline, privacy-focused voice assistant built with **Python 3.13**. This project integrates a Large Language Model (LLM) for reasoning and a Speech-to-Text (STT) engine to run entirely on local hardware (16GB RAM) without any external API keys or internet connection.

## 🚀 Key Features
* **Ears (STT):** Powered by `faster-whisper-base` for real-time, high-accuracy local transcription.
* **Brain (LLM):** Uses `Llama-3.2-3B-Instruct` in GGUF format via `llama-cpp-python` for local reasoning.
* **Mouth (TTS):** Uses `pyttsx3` for fast, offline text-to-speech generation.
* **Privacy First:** All processing happens on-device; no data ever leaves your machine.

---

## 🏗️ Project Structure
```text
VoiceAssistantProject/
├── models/             # (Excluded from Git) Stores LLM and STT weights
│   ├── faster-whisper-base/
│   └── llama-3.2-3b-instruct-q4_k_m.gguf
├── src/
│   ├── ears.py         # Microphone and Whisper transcription logic
│   └── brain.py        # Llama-cpp-python reasoning logic
├── main.py             # Main execution loop (Orchestrator)
├── requirements.txt    # Project dependencies
└── .gitignore          # Filters out heavy model and environment files