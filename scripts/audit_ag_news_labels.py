"""Verify a reproducible 20-row audit of the AG News source labels."""

from __future__ import annotations

import csv
import random
from collections import defaultdict
from pathlib import Path

from datasets import load_dataset


PROJECT_ROOT = Path(__file__).resolve().parents[1]
LABELS_FILE = PROJECT_ROOT / "labels.csv"
REPORT_FILE = PROJECT_ROOT / "data" / "ag_news_source_label_audit.md"
SAMPLE_SEED = 20261021
AUDIT_SEED = 20261028
PER_CLASS = 50
AUDIT_SIZE = 20
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

    chooser = random.Random(SAMPLE_SEED)
    sampled_indices: list[int] = []
    for source_name in LABEL_MAP:
        sampled_indices.extend(chooser.sample(rows_by_source_label[source_name], PER_CLASS))
    chooser.shuffle(sampled_indices)

    expected = {}
    for row in dataset.select(sampled_indices):
        expected[row["text"].strip()] = LABEL_MAP[source_names[row["label"]]]

    with LABELS_FILE.open(encoding="utf-8", newline="") as handle:
        actual_rows = list(csv.DictReader(handle))
    actual = {row["text"].strip(): row["label"].strip() for row in actual_rows}
    if len(actual_rows) != 200 or set(actual) != set(expected):
        raise RuntimeError("labels.csv does not match the expected sampled AG News rows.")

    audit_texts = random.Random(AUDIT_SEED).sample(sorted(expected), AUDIT_SIZE)
    audit_rows = [(text, actual[text], expected[text]) for text in audit_texts]
    matches = sum(project_label == source_label for _, project_label, source_label in audit_rows)

    lines = [
        "# AG News source-label audit",
        "",
        "The instructor-approved AG News training sample was reconstructed with "
        f"seed `{SAMPLE_SEED}`. A deterministic 20-row audit used seed "
        f"`{AUDIT_SEED}`.",
        "",
        f"**Result:** {matches}/{AUDIT_SIZE} project labels match their AG News source labels.",
        "",
        "| # | Article excerpt | Project label | Source label | Match |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for number, (text, project_label, source_label) in enumerate(audit_rows, start=1):
        excerpt = text.replace("|", "\\|").replace("\n", " ")[:120]
        result = "yes" if project_label == source_label else "no"
        lines.append(
            f"| {number} | {excerpt} | `{project_label}` | `{source_label}` | {result} |"
        )
    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {REPORT_FILE.name}: {matches}/{AUDIT_SIZE} labels match.")


if __name__ == "__main__":
    main()
