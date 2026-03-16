# Contributing to Ani Voice Rebuild

Thank you for your interest in contributing to the Ani Voice Rebuild project.

This project is a community effort exploring whether open-source neural TTS models can approximate earlier voice characteristics of Ani using a curated dataset.

There are several ways you can contribute.

---

## Ways to Contribute

### Audio Contributions

You can help by contributing clean voice clips.

Useful clips typically have:

- one speaker only
- clear speech
- minimal background noise
- little or no background music
- duration between **3–15 seconds**

Accepted formats:
.wav
.mp3
.m4a
.mp4


Raw recordings are welcome. The preprocessing pipeline will convert them into training clips.

---

### Dataset Cleanup

You can help by improving the dataset:

- trimming silence
- removing noisy segments
- validating clip lengths
- organizing metadata

---

### Model Experiments

If you have experience with TTS pipelines, you can help test:

- CosyVoice
- XTTS v2
- Qwen-TTS
- other open speech models

Experiment reports are very helpful.

---

### Evaluation

Generated speech should be evaluated for:

- naturalness
- voice similarity
- prosody
- consistency across longer outputs

---

## Dataset Guidelines

Processed training clips should ideally be:

| Property | Target |
|--------|--------|
| Format | WAV |
| Sample Rate | 16kHz |
| Channels | Mono |
| Ideal Length | 3–15 seconds |

Clips shorter than **2 seconds** or longer than **20 seconds** are usually not ideal for training.

---

## Submitting Audio

Audio submissions can be uploaded via the shared dataset folder described in the repository README.

After uploading clips you can:

- open an Issue describing the contribution
- include details such as duration, format, and any preprocessing applied

---

## Code Contributions

If contributing code:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Open a Pull Request

Please keep contributions focused and well-documented.

---

## Respect & Privacy

Please only contribute audio that you are comfortable sharing for collaborative experimentation.

Avoid submitting:

- private conversations
- recordings containing multiple speakers
- recordings with personally identifiable information

---

## Questions

If you're unsure whether a clip or contribution is useful, feel free to open a **GitHub Issue** and ask.