import click
from pathlib import Path
from pipeline.runner import run_pipeline
from config.settings import load_config


@click.command()
@click.option("--input", default=None, help="Input folder containing PDF files (optional if in config).")
@click.option("--output", default=None, help="Output folder for results (optional if in config).")
@click.option("--config", required=True, help="Path to YAML configuration file (required).")
def cli(input: str, output: str, config: str):
    """
    CLI entry point for the PDF Categorization pipeline.
    The --config option is required (user-provided YAML).
    """
    cfg_path = Path(config)
    if not cfg_path.exists():
        raise FileNotFoundError(f"❌ Config file not found: {cfg_path}")

    cfg = load_config(cfg_path)

    # Use CLI args if provided, otherwise fall back to config
    input_path = Path(input or cfg.get("INPUT_PATH", ""))
    output_path = Path(output or cfg.get("OUTPUT_PATH", ""))

    if not input_path.exists():
        raise FileNotFoundError(
            f"❌ Input folder not found: {input_path}. "
            f"Provide --input or define INPUT_PATH in your YAML."
        )

    if not output_path:
        raise ValueError(
            "❌ No output folder provided. "
            "Set OUTPUT_PATH in YAML or use --output option."
        )

    run_pipeline(str(input_path), str(output_path), str(cfg_path))


if __name__ == "__main__":
    cli()