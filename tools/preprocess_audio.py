from pathlib import Path
from pydub import AudioSegment, silence

RAW_DIR = Path("dataset/raw")
OUT_DIR = Path("dataset/processed/wavs")

OUT_DIR.mkdir(parents=True, exist_ok=True)

TARGET_SR = 16000
MIN_MS = 2000
MAX_MS = 20000

counter = 1

for file in RAW_DIR.glob("*"):
    if file.suffix.lower() not in [".wav", ".mp3", ".m4a", ".mp4"]:
        continue

    audio = AudioSegment.from_file(file)
    audio = audio.normalize()
    audio = audio.set_frame_rate(TARGET_SR).set_channels(1)

    chunks = silence.split_on_silence(
        audio,
        min_silence_len=600,
        silence_thresh=audio.dBFS - 16,
        keep_silence=200,
    )

    for chunk in chunks:
        if MIN_MS <= len(chunk) <= MAX_MS:
            out = OUT_DIR / f"ani_{counter:05d}.wav"
            chunk.export(out, format="wav")
            counter += 1

print(f"Exported {counter-1} clips")