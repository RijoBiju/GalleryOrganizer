import os
import shutil
import winshell
from win32com.client import Dispatch

CURRENT_DIRECTORY = os.getcwd()


class FolderManager:

    folders = {}

    def create_year_folder(self, year):
        if year not in FolderManager.folders:
            os.mkdir(f'{CURRENT_DIRECTORY}\\{year}')
            FolderManager.folders[year] = []

    def create_month_folder(self, year, month):
        self.create_year_folder(year)
        months = FolderManager.folders.get(year)
        if month not in months:
            new_directory = f'{CURRENT_DIRECTORY}\\{year}\\{month}'
            os.mkdir(new_directory)
            FolderManager.folders[year] = months.append(month)
        return new_directory

    def move_to_folder(self, old_location, new_location):
        shutil.move(old_location, new_location)

    def create_all_shortcut(self, image_new_directory):
        shortcut_path = f'{CURRENT_DIRECTORY}\\Organizer\\All'
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = image_new_directory
        shortcut.save()
