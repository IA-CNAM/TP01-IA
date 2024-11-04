# Image Processor

A simple Python application for processing images using the Pillow library. This application allows you to resize images to a specified square size, add padding to non-square images, and save the processed images in a designated output folder.

## Features

- Resize images to a square format.
- Add padding to non-square images.
- Save processed images in a user-defined folder.
- Easily configurable for different input and output settings.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IA-CNAM/TP01-IA.git
   cd TP01-IA
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input images in a folder named `input_images`.
2. Run the application:
   ```bash
   python main.py
   ```
   The processed images will be saved in a folder named `dataset`, which will be created automatically if it doesn't exist.

## Configuration

- You can customize the target size for resizing images by modifying the `TARGET_SIZE` constant in `image_processor.py`.
- To change the input folder, you can modify the `input_images` path in `main.py` or use the `set_source_folder()` method of the `ImageProcessor` class.

## Example

Here’s how you can instantiate the `ImageProcessor` class and set a different input folder programmatically:

```python
from src.image_processor import ImageProcessor

processor = ImageProcessor(input_folder='path/to/your/images', image_size=800)
processor.process_folder()
```
