from PIL import Image
import numpy as np

# Function to encode a message into an image
def Encode(src, message, dest):
    # Open the source image
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))

    # Determine the number of color channels (RGB or RGBA)
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    else:
        raise ValueError("Unsupported image mode. Use RGB or RGBA images.")

    total_pixels = array.size // n

    # Append a delimiter to the message
    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])  # Convert to binary

    index = 0
    for p in range(total_pixels):
        for q in range(0, 3):  # Modify R, G, B channels
            if index < len(b_message):
                # Modify the least significant bit (LSB)
                array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                index += 1

    # Reshape the array back to image format
    array = array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)

    # Save the encoded image
    enc_img.save(dest)
    print("Image Encoded Successfully")

# Function to decode a hidden message from an image
def Decode(src):
    # Open the image
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    # Determine the number of color channels (RGB or RGBA)
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    else:
        raise ValueError("Unsupported image mode. Use RGB or RGBA images.")

    total_pixels = array.size // n

    # Initialize a list to store bits
    hidden_bits = []

    # Extract the LSBs from the image
    for p in range(total_pixels):
        for q in range(0, 3):  # Iterate through R, G, B channels
            hidden_bits.append(bin(array[p][q])[-1])  # Append the LSB

            # Check for the delimiter every 8 bits
            if len(hidden_bits) % 8 == 0:
                char_list = [chr(int(''.join(hidden_bits[i:i+8]), 2)) for i in range(0, len(hidden_bits), 8)]
                message = ''.join(char_list)
                if message.endswith("$t3g0"):
                    return message[:-5]  # Remove the delimiter and return the message

    return "No hidden message found or decoding failed."

# Main function to run the program
def main():
    print("---- LSB Steganography ----")
    print("1. Encode message into image")
    print("2. Decode message from image")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        src = input("Enter the source image path: ")
        message = input("Enter the message to encode: ")
        dest = input("Enter the destination image path (with .png extension): ")
        Encode(src, message, dest)
    elif choice == '2':
        src = input("Enter the source image path: ")
        print("Decoding...")
        hidden_message = Decode(src)
        print("Hidden Message:", hidden_message)
    else:
        print("Invalid choice! Please select 1 or 2.")

if _name_ == "_main_":
    main()