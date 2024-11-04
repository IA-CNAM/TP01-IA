# image_processor.py
import os
from datetime import datetime
from typing import Final

from PIL import Image


class ImageProcessor:
    """
    A class for handling basic image processing tasks such as
    resizing, padding, and saving images.

    Attributes:
        TARGET_SIZE (int): Size to which images are resized. Default is 640.
        OUTPUT_FOLDER (str): Directory where processed images are saved.
        DATE_FORMAT (str): Format for naming the output folder.
        source_folder (str): Directory with images to process.
        target_size (int): Final dimension for resizing images.
    """

    TARGET_SIZE: Final[int] = 640
    OUTPUT_FOLDER: Final[str] = "dataset"
    DATE_FORMAT: Final[str] = "%Y%m%d%H%M%S"

    def __init__(
        self, source_folder: str = "", target_size: int = TARGET_SIZE
    ) -> None:
        self.source_folder = source_folder
        self.target_size = target_size

    def process_images_in_folder(self) -> None:
        """Creates an output directory, iterates over images in the
        source folder, and processes them."""
        if not os.path.isdir(self.source_folder):
            raise ValueError(
                "Invalid source folder. Please specify a valid folder"
                " with set_source_folder()."
            )

        output_dir = self.create_output_folder()
        os.makedirs(output_dir, exist_ok=True)

        for img_file in os.listdir(self.source_folder):
            image_path = os.path.join(self.source_folder, img_file)
            self.process_single_image(image_path, output_dir)

    def process_single_image(self, image_path: str, output_dir: str) -> None:
        """Processes a single image by resizing, adding padding, and saving it.

        Args:
            image_path (str): Path to the image.
            output_dir (str): Directory to save processed images.
        """
        img = Image.open(image_path)
        resized = self.resize_to_square(img)
        padded = self.apply_padding(resized)
        self.store_image(padded, image_path, output_dir)

    def resize_to_square(
        self, img: Image.Image, dimension: int = 0
    ) -> Image.Image:
        """Resizes an image to square dimensions while
        preserving aspect ratio.

        Args:
            img (Image.Image): Image to resize.
            dimension (int, optional): Target size.
            Defaults to the instance target_size.

        Returns:
            Image.Image: Resized image.
        """
        size = dimension or self.target_size
        width, height = img.size

        if width > height:
            new_width = size
            new_height = int(height * (size / width))
        elif height > width:
            new_width = int(width * (size / height))
            new_height = size
        else:
            new_width = new_height = size

        return img.resize((new_width, new_height))

    def apply_padding(
        self,
        resized_img: Image.Image,
        pad_color: tuple[int, ...] = (114, 114, 114),
    ) -> Image.Image:
        """Adds padding to make the image square if needed.

        Args:
            resized_img (Image.Image): Image to pad.
            pad_color (tuple[int, ...]): Padding color.
            Defaults to (114, 114, 114).

        Returns:
            Image.Image: Padded image.
        """
        width, height = resized_img.size
        if width == height:
            return resized_img

        color = pad_color if resized_img.mode == "RGB" else (114,)
        square_img = Image.new(
            resized_img.mode, (self.target_size, self.target_size), color
        )
        square_img.paste(resized_img, (0, 0))
        return square_img

    @staticmethod
    def store_image(
        img: Image.Image, original_img_path: str, output_dir: str
    ) -> None:
        """Saves an image to the specified directory.

        Args:
            img (Image.Image): Image to save.
            original_img_path (str): Original image path to preserve naming.
            output_dir (str): Directory where the image is saved.
        """
        img_name = os.path.basename(original_img_path)
        save_path = os.path.join(output_dir, img_name)
        img.save(save_path)

    def create_output_folder(self) -> str:
        """Creates a timestamped output folder path.

        Returns:
            str: Path of the output folder.
        """
        timestamped_folder = datetime.now().strftime(self.DATE_FORMAT)
        return os.path.join(self.OUTPUT_FOLDER, timestamped_folder)

    def set_source_folder(self, path: str) -> None:
        """Sets the source folder path for images to be processed.

        Args:
            path (str): Path to the source folder.
        """
        self.source_folder = path
