import sys
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

exif_table = {}

if __name__ == "__main__":
    working_directory = sys.argv[1]
    files = os.listdir(working_directory)
    img = Image.open(f'{working_directory}\\{files[8]}')
    for k, v in img.getexif().items():
        tag = TAGS.get(k)
        if tag == 'DateTime':
            exif_table[tag] = v
    for i in exif_table.values():
        date_time_parse = datetime.strptime(i, '%Y:%m:%d %H:%M:%S')

        year = date_time_parse.year
        month = months[date_time_parse.month]
        print(year, month)
