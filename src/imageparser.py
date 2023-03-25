import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime

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

    image_name = None
    image_directory = None
    image_year = None
    image_month = None
    exif_table = {}

    def __init__(self, path):
        self.working_directory = path

    def get_image(self):
        files = os.listdir(self.working_directory)
        for image in files:
            ImageParser.image_name = image
            ImageParser.image_directory = f'{self.working_directory}\\{image}'
            img = Image.open(ImageParser.image_directory)
            self.get_exif(img)

    def get_exif(self, img):
        for k, v in img.getexif().items():
            tag = TAGS.get(k)
            if tag == 'DateTime':
                ImageParser.exif_table[tag] = v
                date_time_parse = datetime.strptime(v, '%Y:%m:%d %H:%M:%S')
                ImageParser.image_year = date_time_parse.year
                ImageParser.image_month = months[date_time_parse.month]
