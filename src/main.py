from __future__ import annotations

import time
import logging
from pathlib import Path
from typing import List, Dict, Any
import argparse
from paddleocr import PaddleOCR

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Initialize the OCR engine
OCR_ENGINE = PaddleOCR(use_angle_cls=True, lang="en")


def ocr(image: Path) -> List[Dict[str, Any]]:
    """
    Perform OCR on an image using PaddleOCR.

    Parameters
    ----------
    image : Path
        The path to the image file to process.

    Returns
    -------
    list
        A list containing OCR results for the image. Each result includes:
        - text (str): Recognized text.
        - confidence (float): Confidence score of the detection.
        - bounding_box (dict): The bounding box for the detected text.
          - top (float): Top coordinate.
          - left (float): Left coordinate.
          - width (float): Width of the box.
          - height (float): Height of the box.
    """
    start_time = time.time()
    try:
        # Perform OCR using PaddleOCR
        result = []
        detections = []
        ocr_result = OCR_ENGINE.ocr(str(image), cls=True)

        for line in ocr_result[0]:
            detections.append(
                {
                    "text": line[1][0],
                    "confidence": line[1][1],
                    "bounding_box": {
                        "top": line[0][2][1],
                        "left": line[0][0][0],
                        "width": line[0][1][0] - line[0][0][0],
                        "height": line[0][2][1] - line[0][0][1],
                    },
                }
            )

        result.append({"filename": image.name, "detections": detections})
        elapsed_time = time.time() - start_time
        logging.info(f"Processed '{image.name}' in {elapsed_time:.2f} seconds.")
        return result

    except Exception as e:
        logging.error(f"Error processing image '{image}': {e}")
        return []


def main():
    """
    Main function to parse CLI arguments and execute the OCR process.

    Usage
    -----
    python script.py --image <path_to_image>

    Parameters
    ----------
    --image : str
        The path to the image file to process.
    """
    parser = argparse.ArgumentParser(
        description="Perform OCR on an image using PaddleOCR."
    )
    parser.add_argument(
        "--image", type=str, required=True, help="Path to the image file to process."
    )
    args = parser.parse_args()

    # Validate the input path
    image_path = Path(args.image)
    if not image_path.exists() or not image_path.is_file():
        logging.error(
            f"The provided path is invalid or the file does not exist: {image_path}"
        )
        return

    # Perform OCR and print results
    print(ocr(image_path))

if __name__ == "__main__":
    main()
