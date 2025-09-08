import sys
import whisper

# Ensure UTF-8 encoding for terminal output
sys.stdout.reconfigure(encoding='utf-8')

# Load the Whisper model
model = whisper.load_model("base", device="cpu")

# Path to your audio file
path_to_audio = r"C:/Users/hoang/Downloads/ngan.wav"

# Transcribe the audio
result = model.transcribe(path_to_audio)

# Print the result
print(result["text"])