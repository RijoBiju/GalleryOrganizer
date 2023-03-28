import sys
from src import mediaorganizer, foldermanager
from pathlib import Path
import os
import mimetypes

image_mime_types = ['image/jpeg', 'image/heic', 'image/x-canon-cr2', 'image/x-nikon-nef', 'image/x-sony-arw', 'image/x-adobe-dng']
video_mime_types = ['video/mp4', 'video/quicktime']


if __name__ == "__main__":
    folder_manager = foldermanager.FolderManager()
    folder_manager.create_all_folder()
    media_organizer = mediaorganizer.MediaOrganizer(folder_manager)
    try:
        working_directory = sys.argv[1]
        files = os.listdir(working_directory)
        if files:
            for file_name in files:
                file_location = Path(working_directory, file_name)
                mime_type, _ = mimetypes.guess_type(file_location)
                if mime_type in image_mime_types:
                    media_organizer.type = 'image'
                elif mime_type in video_mime_types:
                    media_organizer.type = 'video'
                media_organizer.image_path = file_location
                exifdata = media_organizer.get_image_metadata()
                media_organizer.process_image_exif(exifdata)
    except IndexError:
        print("Provide a directory to scan for images and videos")
    except NotADirectoryError:
        print("The specified path is not a directory")
    except PermissionError:
        print("Please check that you have the necessary permissions")
    except AttributeError:
        print("Could not determine the MIME type of the file")
