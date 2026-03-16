import wave
from pathlib import Path

DATASET = Path("dataset/processed/wavs")

for file in DATASET.glob("*.wav"):
    with wave.open(str(file), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        dur = wf.getnframes() / sr

    if sr != 16000:
        print("Bad sample rate:", file)

    if ch != 1:
        print("Not mono:", file)

    if dur < 2 or dur > 20:
        print("Bad duration:", file)