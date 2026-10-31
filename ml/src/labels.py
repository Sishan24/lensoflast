DATE_FIELD_CLASSES = (
    "MFD",
    "EXP",
    "BEST_BEFORE",
    "USE_BY",
    "SHELF_LIFE",
    "BATCH_CODE",
    "UNKNOWN",
)

def validate_label_class(label: str) -> str:
    if label not in DATE_FIELD_CLASSES:
        raise ValueError(f"Unknown date-field class: {label}")
    return label
