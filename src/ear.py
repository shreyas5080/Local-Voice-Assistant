import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import os

MODEL_PATH = "model/faster-whisper-base"
FS = 16000
DURATION = 5

print("👂 Loading Whisper Model...")
model = WhisperModel(MODEL_PATH, device="cpu", compute_type="int8")


def listen_and_transcribe():
    print(f"\nRecording for {DURATION} seconds... Speak now!")

    recording = sd.rec(int(DURATION * FS), samplerate=FS, channels=1)
    sd.wait()
    print(" Recording stopped.")

    write("temp_audio.wav", FS, recording)

    # 3. Transcribe
    print("🔍 Transcribing...")
    segments, info = model.transcribe("temp_audio.wav", beam_size=5)
    text = " ".join([segment.text for segment in segments]).strip()

    # Clean up the file
    if os.path.exists("temp_audio.wav"):
        os.remove("temp_audio.wav")

    return text