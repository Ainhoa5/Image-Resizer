# Image Resizer for Uniform Thumbnails

This repository contains a Python script to resize a list of images to uniform thumbnail dimensions, ideal for web galleries, portfolios, or applications requiring consistent image display. The script uses the `Pillow` library to process images, ensuring high-quality results.

## Features
- **Batch Resizing**: Processes multiple images at once.
- **Customizable Dimensions**: Set your target width and height.
- **High-Quality Filtering**: Uses `LANCZOS` for smooth downscaling.
- **Easy Setup**: Lightweight with minimal dependencies.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ainhoa5/Image-Resizer.git
   cd Image-Resizer
   ```

2. **Install the required libraries**:
   Make sure you have `Pillow` installed:
   ```bash
   pip install pillow
   ```

## Usage

1. Place your images in the `images` folder (or specify a path).
2. Run the script to resize images to your specified dimensions:

   ```bash
   python image_resizer.py
   ```

3. Example code in `image_resizer.py`:
   ```python
   from PIL import Image

   if __name__ == "__main__":
       # Load an image from the images folder
       original_image = Image.open("images/sample.jpg")
       list_of_images = [original_image]
       
       # Resize to 100x100 pixels
       resized_thumbnails = resize_images(list_of_images, 100, 100)
       
       # Save resized image
       resized_thumbnails[0].save("images/thumbnail_sample.jpg")
   ```

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.

## License
This project is licensed under the MIT License.

