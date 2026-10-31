# Dataset Specification

## 1. Dataset unit

A single product package image is one source sample. A package may have multiple image views (front, back, cap, side, bottom). Keep all views from the same physical package in the same data split to prevent leakage.

## 2. Suggested folder layout

```text
data/
├── raw/
│   ├── images/
│   └── source_log.csv
├── interim/
│   ├── quality_checked/
│   └── crops/
├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
└── annotations/
    ├── products.csv
    ├── regions.jsonl
    └── field_labels.csv
```

## 3. Annotation fields

Recommended product-level fields:
- sample_id: unique ID
- package_group_id: ID shared by all views of the same physical package
- image_path: relative path
- product_category: food, beverage, personal_care, household, other
- brand_text: optional
- product_name_text: optional
- barcode_text: optional, if legitimately captured
- capture_device: optional
- lighting_condition: normal, low, glare, mixed
- orientation: upright, rotated, perspective
- split: train, validation, test

Recommended date-region fields:
- region_id
- sample_id
- x_min, y_min, x_max, y_max (pixel coordinates)
- transcription: exact visible text; preserve punctuation and spacing
- semantic_type: MFD, EXP, BEST_BEFORE, USE_BY, SHELF_LIFE, BATCH_CODE, UNKNOWN
- legibility: clear, partly_legible, unreadable
- reviewer_verified: true/false

Recommended parsed-date fields:
- raw_text
- parsed_value (ISO date only when unambiguous)
- date_format
- date_type
- parse_status: valid, ambiguous, invalid, not_a_date
- confidence
- verification_status: pending, accepted, corrected, rejected

## 4. Annotation rules

- Transcribe exactly; do not silently correct what appears on the package.
- Record semantic type separately from transcription.
- Keep ambiguous date formats unresolved until verified.
- Do not label batch/lot codes as dates without evidence.
- Distinguish a printed absolute date from a duration such as "6 months".
- Record missing fields as missing, not as guessed values.
- Keep package-group IDs together across train/validation/test.
- Have a second review pass for test annotations if possible.

## 5. Dataset split

Suggested starting split: 70% train, 15% validation, 15% test, grouped by physical package/product family where practical. The test set should contain packages not seen during training. Avoid placing near-identical images of one package in different splits.

## 6. Data augmentation

Use realistic augmentation: mild rotation, perspective warp, brightness/contrast changes, blur, compression artifacts and sensor noise. Do not transform dates so aggressively that the target becomes physically implausible. Apply augmentation only to training data.

## 7. Privacy and licensing

Prefer photographs you take yourself. Do not collect personal receipts, faces or private information unless necessary and consented to. Record the source and usage permission for external images. Do not redistribute third-party datasets unless their licence permits it.
