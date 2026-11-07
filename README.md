# FastSpeech2_VN — FastSpeech 2 for Vietnamese TTS

A Vietnamese adaptation of [ming024/FastSpeech2](https://github.com/ming024/FastSpeech2) (FastSpeech 2: *Fast and
High-Quality End-to-End Text to Speech*, Ren et al., 2020), trained on the **VLSP 2020** TTS corpus with a HiFi-GAN
vocoder. Built during my 2021 Vietnamese TTS research.

## What is Vietnamese-specific

| Added / changed | Purpose |
|---|---|
| `preprocessor/vlsp2020.py` | Prepare the VLSP 2020 corpus (`metadata.csv` → aligned raw data) |
| `text/phoneme.py`, `text/phoneme.txt`, `dict_char2word.txt` | Vietnamese grapheme → phoneme decomposition (e.g. `ang → a n g`) |
| `config/vlsp_char/`, `config/vlsp_phoneme/` | Two input representations: characters or phonemes |
| `gen_train_test.py` | Train/validation split for VLSP 2020 |

Everything else (variance adaptor, Transformer encoder/decoder, HiFi-GAN) follows the upstream implementation.

## Usage

```bash
pip install -r requirements.txt     # pinned to the 2021 stack (PyTorch 1.7, librosa 0.7)

# 1. point config/vlsp_phoneme/preprocess.yaml at your copy of the VLSP 2020 corpus, then
python prepare_align.py config/vlsp_phoneme/preprocess.yaml
python preprocess.py   config/vlsp_phoneme/preprocess.yaml

# 2. train
python train.py -p config/vlsp_phoneme/preprocess.yaml \
                -m config/vlsp_phoneme/model.yaml \
                -t config/vlsp_phoneme/train.yaml

# 3. synthesize one sentence (set the HiFi-GAN checkpoint path in utils/model.py → get_vocoder)
python synthesize.py --mode single --restore_step 130000 \
    --text "xin chào các bạn" \
    -p config/vlsp_phoneme/preprocess.yaml -m config/vlsp_phoneme/model.yaml -t config/vlsp_phoneme/train.yaml
```

Pitch, energy and speaking rate can be controlled with `--pitch_control`, `--energy_control` and
`--duration_control`.

Text should be normalized first (numbers, dates, abbreviations…) — see
[NormTTS](https://github.com/cuongnguyengit/NormTTS).

## Notes

- The VLSP 2020 corpus and trained checkpoints are not included (dataset license).
- The vocoder checkpoint path in `utils/model.py` is hard-coded to the original Colab location — change it before synthesizing.
- This is a 2021 research snapshot and is not maintained.

## Credits

- [ming024/FastSpeech2](https://github.com/ming024/FastSpeech2) — original implementation (MIT)
- [jik876/hifi-gan](https://github.com/jik876/hifi-gan) — vocoder (MIT, see `hifigan/LICENSE`)
- VLSP 2020 TTS shared task organisers for the corpus
