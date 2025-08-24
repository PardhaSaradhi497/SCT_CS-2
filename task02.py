from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    arr = np.array(img)

    # Apply pixel manipulation (add key to each pixel, mod 256)
    encrypted_arr = (arr + key) % 256

    # Swap pixel values (reverse the array as a simple swap)
    encrypted_arr = np.flip(encrypted_arr, axis=1)

    encrypted_img = Image.fromarray(np.uint8(encrypted_arr))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")


# Function to decrypt the image
def decrypt_image(input_path, output_path, key=50):
    img = Image.open(input_path)
    arr = np.array(img)

    # Reverse the swap
    arr = np.flip(arr, axis=1)

    # Subtract key to restore original
    decrypted_arr = (arr - key) % 256

    decrypted_img = Image.fromarray(np.uint8(decrypted_arr))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")


# Example usage
encrypt_image("input.jpg", "encrypted.png", key=100)
decrypt_image("encrypted.png", "decrypted.png", key=100)
