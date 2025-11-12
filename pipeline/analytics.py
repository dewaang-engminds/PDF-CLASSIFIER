from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import json
from utils.logger import setup_logger

logger = setup_logger()


def generate_analytics(output_path: str, analytics_data: list):
    """
    Generate summary CSV, per-file JSON, and overall charts.
    """
    analytics_dir = Path(output_path) / "analytics"
    analytics_dir.mkdir(parents=True, exist_ok=True)

    df_rows = []
    for entry in analytics_data:
        df_rows.append({
            "FileName": entry["FileName"],
            "PredictedType": entry["PredictedType"],
            "PredictedScore": entry.get("PredictedScore", 0.0),
            "AllScores": entry.get("AllScores", {}),
        })

        # Per-file detailed JSON
        detail_path = analytics_dir / f"{entry['FileName']}.json"
        with open(detail_path, "w", encoding="utf-8") as f:
            json.dump(entry.get("KeywordDetails", {}), f, indent=2)

    df = pd.DataFrame(df_rows)
    csv_path = analytics_dir / "classification_results.csv"
    df.to_csv(csv_path, index=False)
    logger.info(f"Analytics CSV written: {csv_path}")

    if not df.empty:
        avg = df.groupby("PredictedType")["PredictedScore"].mean().sort_values(ascending=False)
        ax = avg.plot(kind="bar", title="Average Classification Score")
        ax.set_ylabel("Score")
        plt.tight_layout()
        chart_path = analytics_dir / "average_scores.png"
        plt.savefig(chart_path)
        plt.close()
        logger.info(f"Chart saved: {chart_path}")
