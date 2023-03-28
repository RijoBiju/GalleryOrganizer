# GalleryOrganizer

GalleryOrganizer is a Python script for organizing image and video files by year and month. It uses the ExifTool library to extract metadata from image files and create folders to store them in based on the year and month they were taken.

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies by running 'pip install -r requirements.txt' in the project directory.
3. Install ExifTool by following the instructions for your operating system.

```bash
pip install -r requirements.txt
```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the script using python organizer.py [directory], where [directory] is the path to the directory containing the image and video files you want to organize.
3. The script will create subdirectories for each year and month in which the files were taken, and move the files into their respective directories.

## Supported file types

GalleryOrganizer supports the following image file types:

JPEG (.jpg, .jpeg)

And the following video file types:

MP4 (.mp4)
MOV (.mov)
