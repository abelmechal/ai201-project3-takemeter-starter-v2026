"""Build the instructor-approved balanced AG News sample for TakeMeter."""

from __future__ import annotations

import csv
import random
from collections import defaultdict
from pathlib import Path

from datasets import load_dataset


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = PROJECT_ROOT / "labels.csv"
SEED = 20261021
PER_CLASS = 50
LABEL_MAP = {
    "World": "world",
    "Sports": "sports",
    "Business": "business",
    "Sci/Tech": "sci_tech",
}


def main() -> None:
    dataset = load_dataset("ag_news", split="train")
    source_names = dataset.features["label"].names
    rows_by_source_label: dict[str, list[int]] = defaultdict(list)
    for index, source_label_id in enumerate(dataset["label"]):
        rows_by_source_label[source_names[source_label_id]].append(index)

    chooser = random.Random(SEED)
    chosen_indices: list[int] = []
    for source_name in LABEL_MAP:
        chosen_indices.extend(chooser.sample(rows_by_source_label[source_name], PER_CLASS))
    chooser.shuffle(chosen_indices)

    selected = dataset.select(chosen_indices)
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=("text", "label", "note"))
        writer.writeheader()
        for row in selected:
            source_name = source_names[row["label"]]
            writer.writerow(
                {
                    "text": row["text"].strip(),
                    "label": LABEL_MAP[source_name],
                    "note": (
                        "Instructor-approved source label from AG News "
                        f"train split: {source_name}. Sample seed: {SEED}."
                    ),
                }
            )
    print(f"Wrote {len(selected)} rows to {OUTPUT_FILE.name}.")


if __name__ == "__main__":
    main()
