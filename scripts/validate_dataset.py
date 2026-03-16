from pathlib import Path
import sys

DATASET_DIR = Path("dataset")

REQUIRED_SUBDIRS = [
    "raw",
    "processed",
]

OPTIONAL_FILES = [
    "metadata.csv",
]

def main() -> int:
    if not DATASET_DIR.exists():
        print("dataset/ directory not found. Skipping dataset structure validation.")
        return 0

    missing = []

    for subdir in REQUIRED_SUBDIRS:
        path = DATASET_DIR / subdir
        if not path.exists():
            missing.append(str(path))

    if missing:
        print("Dataset structure validation failed.")
        print("Missing required paths:")
        for item in missing:
            print(f" - {item}")
        return 1

    for filename in OPTIONAL_FILES:
        path = DATASET_DIR / filename
        if not path.exists():
            print(f"Warning: optional file not found: {path}")

    print("Dataset structure looks valid.")
    return 0

if __name__ == "__main__":
    sys.exit(main())