from PIL import Image
import numpy as np

# Function to encode a message into an image using MSB
def Encode_MSB(src, message, dest):
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
    message += "$t3g0"  # Delimiter to signify the end of the message
    b_message = ''.join([format(ord(i), "08b") for i in message])  # Convert message to binary

    # Check if the message fits in the image
    if len(b_message) > total_pixels * 3:
        raise ValueError("Message too large to encode in the given image.")

    index = 0
    for p in range(total_pixels):
        for q in range(0, 3):  # Modify R, G, B channels
            if index < len(b_message):
                # Modify the most significant bit (MSB)
                pixel_bin = bin(array[p][q])[2:].zfill(8)  # Convert to 8-bit binary
                array[p][q] = int(b_message[index] + pixel_bin[1:], 2)  # Replace the MSB with the message bit
                index += 1

    # Reshape the array back to image format
    array = array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)

    # Save the encoded image
    enc_img.save(dest)
    print("Image Encoded Successfully")

# Function to decode a hidden message from an image using MSB
def Decode_MSB(src):
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
    hidden_bits = []  # To store the extracted bits
    decoded_message = ""  # To hold the decoded message

    # Extract MSBs from the image
    for p in range(total_pixels):
        for q in range(0, 3):  # Iterate through R, G, B channels
            # Extract the MSB by shifting the pixel value to the right
            msb = (array[p][q] >> 7) & 1
            hidden_bits.append(str(msb))  # Append the extracted MSB

            # Every 8 bits form a character
            if len(hidden_bits) % 8 == 0:
                # Combine the last 8 bits into a byte
                byte_str = ''.join(hidden_bits[-8:])
                byte_int = int(byte_str, 2)  # Convert binary string to an integer
                char = chr(byte_int)  # Convert integer to its corresponding ASCII character

                decoded_message += char  # Append the character to the decoded message

                # Check for the delimiter "$t3g0"
                if decoded_message.endswith("$t3g0"):
                    return decoded_message[:-5]  # Return the message without the delimiter

    return "No hidden message found or decoding failed."

# Main function for user interaction
def main():
    print("---- MSB Steganography ----")
    print("1. Encode message into image")
    print("2. Decode message from image")
    choice = input("Choose an option (1/2): ")

    if choice == '1':
        src = input("Enter the source image path: ")
        message = input("Enter the message to encode: ")
        dest = input("Enter the destination image path (with .png extension): ")
        try:
            Encode_MSB(src, message, dest)
        except Exception as e:
            print("Error during encoding:", str(e))
    elif choice == '2':
        src = input("Enter the source image path: ")
        try:
            print("Decoding...")
            hidden_message = Decode_MSB(src)
            print("Hidden Message:", hidden_message)
        except Exception as e:
            print("Error during decoding:", str(e))
    else:
        print("Invalid choice! Please select 1 or 2.")

if _name_ == "_main_":
    main()