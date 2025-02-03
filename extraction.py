from PIL import Image
import pytesseract
import os
 
USER_IMAGE_DIR = "user_images"
 
# Ensure the directory exists
if not os.path.exists(USER_IMAGE_DIR):
    os.makedirs(USER_IMAGE_DIR)
 
def save_user_image(image):
    """Saves the uploaded image to the user_images directory."""
    try:
        image_path = os.path.join(USER_IMAGE_DIR, image.filename)
        image.save(image_path)
        return image_path
    except Exception as e:
        return f"Error saving image: {str(e)}"
 
def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from an image using Tesseract OCR.
    
    :param image_path: Path to the image file.
    :return: Extracted text as a string.
    """
    try:
        img = Image.open(image_path)
        # Optional: Preprocessing the image (e.g., convert to grayscale)
        img = img.convert('L')
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        return f"Error: {str(e)}"
 
# Example usage:
# extracted_text = extract_text_from_image('data.jpeg')
# print(extracted_text)