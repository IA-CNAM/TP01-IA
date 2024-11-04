# main.py
"""Main module for processing images in a specified folder."""
import os

from src.image_processor import ImageProcessor


def main():
    """Main function to process images."""
    input_path = os.path.join(os.getcwd(), "input_images")
    processor = ImageProcessor(input_path)
    processor.process_images_in_folder()


if __name__ == "__main__":
    main()
