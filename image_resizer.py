from PIL import Image

def resize_images(images, target_width, target_height):
    """
    Resizes a list of images to uniform dimensions for thumbnails.
    
    Parameters:
    images (list): List of PIL Image objects.
    target_width (int): Desired width for the thumbnail.
    target_height (int): Desired height for the thumbnail.
    
    Returns:
    list: List of resized PIL Image objects.
    """
    resized_images = []
    
    for image in images:
        # Resize the image to the target dimensions using LANCZOS for high quality
        resized_image = image.resize((target_width, target_height), Image.LANCZOS)
        resized_images.append(resized_image)
        
    return resized_images

# Example usage:
# Assuming `list_of_images` is a list of Image objects already loaded
# resized_thumbnails = resize_images(list_of_images, 100, 100)
if __name__ == "__main__":
    # Load an image (make sure you have an image named 'sample.jpg' in your folder)
    original_image = Image.open("images/sample.jpg")
    list_of_images = [original_image]  # Add to a list to match our function's input type
    
    # Resize the image to 100x100 pixels
    resized_thumbnails = resize_images(list_of_images, 100, 100)
    
    # Save the resized image to verify
    resized_thumbnails[0].save("images/thumbnail_sample.jpg")
    print("Thumbnail saved as 'thumbnail_sample.jpg'")
