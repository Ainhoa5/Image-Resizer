from PIL import Image
import os
from PIL import Image
import os

def resize_images_in_folder(folder_path, target_width, target_height):
    """
    Resizes all images in a specified folder to uniform dimensions for thumbnails.
    
    Parameters:
    folder_path (str): The path to the folder containing images.
    target_width (int): Desired width for the thumbnail.
    target_height (int): Desired height for the thumbnail.
    
    Returns:
    None: Saves resized images in a 'thumbnails' folder inside the specified folder.
    """
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Folder path is invalid. Please check the path and try again.")
        return

    # Create a 'thumbnails' folder inside the specified folder if it doesn't exist
    thumbnails_folder = os.path.join(folder_path, "thumbnails")
    os.makedirs(thumbnails_folder, exist_ok=True)
    
    # Process each image file in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                # Resize the image to the target dimensions using LANCZOS for high quality
                resized_image = img.resize((target_width, target_height), Image.LANCZOS)
                
                # Save the resized image in the 'thumbnails' folder
                save_path = os.path.join(thumbnails_folder, filename)
                resized_image.save(save_path)
                print(f"Thumbnail saved as {save_path}")


# Example usage:
# Assuming `list_of_images` is a list of Image objects already loaded
# resized_thumbnails = resize_images(list_of_images, 100, 100)
if __name__ == "__main__":
    # Ask the user to input the folder path
    folder_path = input("Enter the folder path containing images: ")
    
    # Set target dimensions for the thumbnails
    target_width = 100
    target_height = 100
    
    # Resize images in the specified folder
    resize_images_in_folder(folder_path, target_width, target_height)