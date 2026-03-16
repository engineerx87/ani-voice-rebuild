from pathlib import Path
import subprocess
import sys

AUDIO_ROOTS = [
    Path("dataset/raw"),
    Path("dataset/processed"),
]

VALID_EXTENSIONS = {".wav", ".mp3", ".flac", ".m4a", ".ogg"}

def check_ffprobe() -> bool:
    try:
        subprocess.run(
            ["ffprobe", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
        return True
    except Exception:
        return False

def verify_audio_file(path: Path) -> bool:
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "error",
                "-show_entries", "stream=codec_name,sample_rate,channels",
                "-of", "default=noprint_wrappers=1:nokey=0",
                str(path),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            print(f"Invalid audio file: {path}")
            print(result.stderr.strip())
            return False

        print(f"OK: {path}")
        return True
    except Exception as exc:
        print(f"Error reading {path}: {exc}")
        return False

def main() -> int:
    if not check_ffprobe():
        print("ffprobe is not installed or not available in PATH.")
        return 1

    files = []
    for root in AUDIO_ROOTS:
        if root.exists():
            files.extend(
                p for p in root.rglob("*")
                if p.is_file() and p.suffix.lower() in VALID_EXTENSIONS
            )

    if not files:
        print("No audio files found. Skipping audio verification.")
        return 0

    failed = False
    for audio_file in files:
        if not verify_audio_file(audio_file):
            failed = True

    if failed:
        print("Audio verification failed.")
        return 1

    print("All audio files passed verification.")
    return 0

if __name__ == "__main__":
    sys.exit(main())