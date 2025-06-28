import argparse
import json
import mlx_whisper

def main():
    parser = argparse.ArgumentParser(description="Transcribe using KB-Whisper MLX")
    parser.add_argument("input_file", help="Input audio file path")
    parser.add_argument("output_file", help="Output file path")
    parser.add_argument("--language", default=None, help="Language code")
    parser.add_argument("--format", default="json", choices=["json", "txt"], help="Output format")
    
    args = parser.parse_args()
    
    print(f"Using converted KB-Whisper MLX model")
    print(f"Processing: {args.input_file}")
    
    # Use your converted model
    result = mlx_whisper.transcribe(
        args.input_file,
        path_or_hf_repo="./kb-whisper-large-mlx",
        language=args.language,
        verbose=True
    )
    
    # Save based on format
    if args.format == "txt":
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(result['text'])
        print(f"✅ Complete! Saved text to: {args.output_file}")
    else:
        output = {
            "text": result["text"],
            "segments": result.get("segments", []),
            "language": result.get("language", "unknown")
        }
        with open(args.output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"✅ Complete! Saved JSON to: {args.output_file}")
    
    print(f"Text preview: {result['text'][:100]}...")

if __name__ == "__main__":
    main()