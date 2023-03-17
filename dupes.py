import os
import hashlib
from PIL import Image
from shutil import move

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def hash_image(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        return hashlib.md5(image_data).hexdigest()

def find_duplicate_images(directory):
    image_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                image_hash = hash_image(file_path)

                if image_hash in image_hashes:
                    duplicates.append((file_path, image_hashes[image_hash]))
                else:
                    image_hashes[image_hash] = file_path

    return duplicates

def main():
    directory = os.getcwd()
    create_directory_if_not_exists(os.path.join(directory, "dupes"))

    duplicate_images = find_duplicate_images(directory)
    
    for duplicate_image, original_image in duplicate_images:
        print(f"Found duplicate: {duplicate_image} (Original: {original_image})")
        move(duplicate_image, os.path.join(directory, "dupes", os.path.basename(duplicate_image)))

if __name__ == "__main__":
    main()
