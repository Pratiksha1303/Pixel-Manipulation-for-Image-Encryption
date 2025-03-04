from PIL import Image
import numpy as np

def process_image(image_path, key, output_path):
    img = Image.open(image_path)  
    img_array = np.array(img)  

    # XOR operation for encryption/decryption
    processed_array = img_array ^ key  

    Image.fromarray(processed_array).save(output_path)
    print(f"Saved as {output_path}")

key = 123  # Key
process_image("img.jpg", key, "encrypted.jpg")  # Encrypt
process_image("encrypted.jpg", key, "decrypted.jpg")  # Decrypt
