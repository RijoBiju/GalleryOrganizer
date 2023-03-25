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


class AllFolder(FolderManager):

    image_directory = None
    image_year = None
    image_month = None

    def manage_folders(self):
        self.new_location = FolderManager.create_month_folder(AllFolder.image_year, AllFolder.image_month)
        FolderManager.move_to_folder(AllFolder.image_directory, self.new_location)

    def create_all_shortcut(self):
        self.manage_folders()
        shortcut_path = f'{CURRENT_DIRECTORY}\\All'
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = self.new_location
        shortcut.save()
