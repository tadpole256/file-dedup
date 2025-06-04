# Image Deduplication Tool

## Overview

This project provides a simple yet effective tool for identifying and managing duplicate image files within a directory. It's particularly useful for organizing large collections of images, freeing up disk space, and maintaining a clean file structure.

## Features

- Scans directories recursively for image files (supports .png, .jpg, .jpeg, .gif, .bmp)
- Uses MD5 hashing to identify duplicate images
- Moves duplicate files to a separate 'dupes' folder
- Provides a progress bar for visual feedback during processing
- Allows selecting the target directory through a GUI dialog

## How It Works

1. The script walks through the specified directory and its subdirectories.
2. It calculates an MD5 hash for each image file encountered.
3. If a duplicate hash is found, the corresponding file is moved to a 'dupes' folder.
4. The original files remain in their initial locations.

## Usage

1. Run the script using Python:
   ```
   python dupes.py
   ```
2. When the GUI dialog appears, choose the directory you want to scan.
3. The script will process all images in the chosen directory and its subdirectories.
4. Duplicate images will be moved to a 'dupes' folder within the selected directory.

## Requirements

- Python 3.x
- tqdm library
- tkinter (usually included with Python)

You can install the required libraries using pip.

This is an early version and I'm sure there's a lot of room for improvement. This is an open source project and I'm happy to accept any contributions.
