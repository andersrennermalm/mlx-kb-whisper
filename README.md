# mlx-kb-whisper
MLX version of the KBLAB/kb-whisper model on HuggingFace.
KBLAB/kb-whisper is a suite of Whisper models trained on Swedish speech by The National Library of Sweden. 
mlx-whisper is a speech-to-text framework for Apple Silicon. 

This project contains example code and instructions for converting a kb-whisper model for use with mlx.

## Getting Started
To get started with this project, clone the repository:
```
git clone https://github.com/andersrennermalm/mlx-kb-whisper.git
cd mlx-kb-whisper
```

## Convert a kb-whisper model

This project uses `uv` for dependency management. To install the dependencies, run:
```
uv sync
```

1. Clone the mlx-examples repo
   ```
   git clone https://github.com/ml-explore/mlx-examples.git
   ```
2. Run the conversion script. The script takes the path to the HuggingFace model, for example `KBLab/kb-whisper-large-hf` and the path to save the converted model.
   ```
   uv run python mlx-examples/whisper/convert.py --torch-name-or-path KBLab/kb-whisper-large --mlx-path kb-whisper-large-mlx
   ```

## Run the converted model

To run the converted model, use the `main.py` script. You need to provide an input audio file and an output file.

### Parameters:
* `<input_audio_file>`: Path to the input audio file.
* `<output_file>`: Path to save the output transcription.
* `--language`: (Optional) Language code of the audio (e.g., `en` for English, `sv` for Swedish). If not provided, the model will attempt to detect the language.
* `--format`: (Optional) Output format, either `json` (default) or `txt`.

```bash
uv run python main.py <input_audio_file> <output_file> --language <language_code> --format <json_or_txt>
```

For example:

```bash
uv run python main.py audio.mp3 output.json --language sv --format json
```

## Read more
* mlx-whisper: https://github.com/ml-explore/mlx-examples/tree/main/whisper
* KBLAB/kb-whisper: https://huggingface.co/KBLab/kb-whisper-large 
