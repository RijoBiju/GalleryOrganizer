import subprocess
import json
from datetime import datetime
from typing import Dict


class MediaOrganizer:

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

    def __init__(self, folder_manager):
        self.folder_manager = folder_manager
        self._image_path: str = ''
        self._image_name: str = ''

    @property
    def image_path(self):
        return self._image_path

    @image_path.setter
    def image_path(self, path):
        self._image_path = path
        self._image_name = path.stem

    def get_image_metadata(self) -> Dict:
        try:
            output: bytes = subprocess.check_output(['exiftool', '-j', self._image_path])
            exifdata: Dict = json.loads(output.decode())[0]
            return exifdata
        except FileNotFoundError:
            print("Please check that the exiftool command is installed")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output.decode()}. The exiftool command returned a non-zero exit status")

    def parse_image_datetime(self, img_datetime: str) -> datetime:
        try:
            return datetime.strptime(img_datetime, '%Y:%m:%d %H:%M:%S')
        except ValueError:
            print("Invalid datetime format")
            return None

    def get_image_year(self, img_datetime: str) -> int:
        return self.parse_image_datetime(img_datetime).year

    def get_image_month(self, img_datetime: str) -> int:
        return self.parse_image_datetime(img_datetime).month

    def process_image_exif(self, img: Dict) -> None:
        try:
            img_datetime: str = img["DateTimeOriginal"]
            img_year: int = self.get_image_year(img_datetime)
            img_month: str = MediaOrganizer.months[self.get_image_month(img_datetime)]
            new_image_path: str = self.folder_manager.create_folder_by_month(img_year, img_month)
            self.folder_manager.move_to_folder(self._image_path, new_image_path)
            self.folder_manager.create_all_shortcut(self._image_name, self._image_path, new_image_path)
        except (KeyError, IndexError):
            print("Invalid input data. Check input dictionary")
