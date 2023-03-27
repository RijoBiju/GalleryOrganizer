import sys
from src import mediaorganizer, foldermanager
from pathlib import Path
import os
import mimetypes

image_mime_types = ['image/jpeg', 'image/heic']
video_mime_types = ['video/mp4', 'video/quicktime']


if __name__ == "__main__":
    folder_manager = foldermanager.FolderManager()
    working_directory = sys.argv[1]
    files = os.listdir(working_directory)
    media_organizer = mediaorganizer.MediaOrganizer(folder_manager)
    for file_name in files:
        file_location = Path(working_directory, file_name)
        mime_type, _ = mimetypes.guess_type(file_location)
        if mime_type in image_mime_types:
            media_organizer.image_path = file_location
            exifdata = media_organizer.get_image_metadata()
            media_organizer.process_image_exif(exifdata)
