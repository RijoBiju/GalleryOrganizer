import sys
from src import mediaorganizer, foldermanager
import pathlib
import os

image_extensions = ['.JPG', '.JPEG', '.HEIC']
video_extensions = ['.MP4', '.MOV']


if __name__ == "__main__":
    folder_manager = foldermanager.FolderManager()
    working_directory = sys.argv[1]
    files = os.listdir(working_directory)
    for i in files:
        file_location = f'{working_directory}\\{files[i]}'
        file_extension = pathlib.Path(file_location).suffix
        if file_extension in image_extensions:
            image_parser = mediaorganizer.MediaOrganizer(folder_manager)
            image_parser.image_path = file_location
            exifdata = image_parser.get_image_metadata()
            image_parser.process_image_exif(exifdata)
            print('image')
        elif file_extension in video_extensions:
            print('video')
