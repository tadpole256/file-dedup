import os
import hashlib
from shutil import move
from tqdm import tqdm

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

    image_files = []
    for root, dirs, files in os.walk(directory):
        if 'dupes' in dirs:
            dirs.remove('dupes')
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_files.append(os.path.join(root, file))

    for file_path in tqdm(image_files, desc="Processing images"):
        image_hash = hash_image(file_path)

        if image_hash in image_hashes:
            duplicates.append((file_path, image_hashes[image_hash]))
        else:
            image_hashes[image_hash] = file_path

    return duplicates

def move_with_unique_name(src, dest_dir):
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    dest_path = os.path.join(dest_dir, base)
    counter = 1
    while os.path.exists(dest_path):
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1
    move(src, dest_path)

def main():
    directory = os.getcwd()
    create_directory_if_not_exists(os.path.join(directory, "dupes"))

    duplicate_images = find_duplicate_images(directory)
    
    for duplicate_image, original_image in duplicate_images:
        print(f"Found duplicate: {duplicate_image} (Original: {original_image})")
        move_with_unique_name(duplicate_image, os.path.join(directory, "dupes"))

    print("Finished processing all files.")

if __name__ == "__main__":
    main()
