import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from foldermanager import AllFolder, FolderManager


months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}


class ImageParser:

    def __init__(self, path):
        self.working_directory = path

    def get_image(self):
        files = os.listdir(self.working_directory)
        self.folder_manager = FolderManager()
        for image in files:
            self.image_orig_directory = f'{self.working_directory}\\{image}'
            img = Image.open(ImageParser.image_directory)
            self.get_image_details(img)

    def get_image_details(self, img):
        for k, v in img.getexif().items():
            tag = TAGS.get(k)
            if tag == 'DateTime':
                date_time_parse = datetime.strptime(v, '%Y:%m:%d %H:%M:%S')
                image_year = date_time_parse.year
                image_month = months[date_time_parse.month]
                image_new_directory = self.folder_manager.create_month_folder(image_year, image_month)
                self.folder_manager.move_to_folder(self.image_orig_directory, image_new_directory)
                self.folder_manager.create_all_shortcut(image_new_directory)
