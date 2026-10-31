from pathlib import Path
import cv2
import numpy as np


def load_grayscale(image_path: str | Path) -> np.ndarray:
    image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")
    return image


def resize_keep_aspect(image: np.ndarray, target_height: int = 48,
                       max_width: int = 320) -> np.ndarray:
    if image.ndim != 2:
        raise ValueError("Expected a grayscale image.")
    height, width = image.shape
    if height == 0 or width == 0:
        raise ValueError("Image dimensions must be non-zero.")
    scale = target_height / height
    new_width = max(1, min(max_width, round(width * scale)))
    resized = cv2.resize(image, (new_width, target_height), interpolation=cv2.INTER_AREA)
    canvas = np.zeros((target_height, max_width), dtype=np.uint8)
    canvas[:, :new_width] = resized
    return canvas.astype(np.float32) / 255.0
