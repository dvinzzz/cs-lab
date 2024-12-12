import numpy as np
import cv2

def calculate_psnr(original_image, compressed_image):
    if original_image is None or compressed_image is None:
        raise ValueError("One or both image files could not be loaded. Check the file paths.")
    
    if original_image.shape != compressed_image.shape:
        raise ValueError("Input images must have the same dimensions.")
    
    # Compute Mean Squared Error (MSE)
    mse = np.mean((original_image - compressed_image) ** 2)
    if mse == 0:
        return float('inf')  # Return infinite PSNR if there is no error (i.e., images are identical)
    
    max_pixel = 255.0  # Maximum pixel value for 8-bit images
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Load images (original and compressed)
original = cv2.imread("C:/path/to/your/original_image.png")
compressed = cv2.imread("C:/path/to/your/compressed_image.png")

if original is None or compressed is None:
    print("Error: One or both images could not be loaded. Please check the file paths.")
else:
    psnr_value = calculate_psnr(original, compressed)
    print(f"PSNR: {psnr_value} dB")