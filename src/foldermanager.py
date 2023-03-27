import shutil
import win32com.client as win32
from pathlib import Path

CURRENT_DIRECTORY = str(Path.cwd())
ORGANIZER_DIRECTORY = str(Path(CURRENT_DIRECTORY, 'Organizer', 'All'))


class FolderManager:

    created_folders = {}

    @classmethod
    def create_folder_by_year(self, year: int) -> None:
        if year not in self.created_folders:
            year_directory = Path(CURRENT_DIRECTORY, str(year))
            year_directory.mkdir()
            self.created_folders[year] = []

    @classmethod
    def create_folder_by_month(self, year: int, month: str) -> str:
        self.create_folder_by_year(year)
        months = self.created_folders.get(year)
        if month not in months:
            month_directory = Path(CURRENT_DIRECTORY, str(year), month)
            month_directory.mkdir()
            self.created_folders[year] = months.append(month)
        return str(month_directory)

    @staticmethod
    def move_to_folder(old_image_path: str, new_image_path: str) -> None:
        shutil.move(old_image_path, new_image_path)

    @staticmethod
    def create_all_shortcut(new_image_path: str) -> None:
        shortcut_path = Path(ORGANIZER_DIRECTORY)
        shortcut = win32.Dispatch('WScript.Shell').CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = str(new_image_path)
        shortcut.save()
