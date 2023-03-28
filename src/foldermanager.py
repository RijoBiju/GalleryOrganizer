import shutil
import win32com.client as win32
from pathlib import Path

CURRENT_DIRECTORY = str(Path(str(Path.cwd()), 'Organizer'))
ORGANIZER_DIRECTORY = str(Path(CURRENT_DIRECTORY, 'All'))


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
        month_directory = Path(CURRENT_DIRECTORY, str(year), month)
        if month not in months:
            month_directory.mkdir()
            self.created_folders[year].append(month)
            print(self.created_folders)
        return str(month_directory)

    @staticmethod
    def create_all_folder() -> None:
        all_path = Path(ORGANIZER_DIRECTORY)
        all_path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def move_to_folder(old_image_path: str, new_image_path: str) -> None:
        shutil.move(old_image_path, new_image_path)

    @staticmethod
    def create_all_shortcut(image_name, old_image_path, new_image_path: str) -> None:
        shortcut_path = Path(ORGANIZER_DIRECTORY, f'{image_name}.lnk')
        file_name = old_image_path.name
        shortcut = win32.Dispatch('WScript.Shell').CreateShortCut(str(shortcut_path))
        shortcut.TargetPath = str(Path(new_image_path, file_name))
        shortcut.save()
