import pathlib
from datetime import datetime

"""
This module contains basic functions for creating a dealing with folder creation in the App
"""


# Creates a folder with the current date, to store the screenshots it takes
def create_dir():
    today = datetime.today().strftime("%d_%m")
    folder = "Ad_library_screens"
    subfolder = f"screenshots_{today}"
    final_folder = pathlib.Path.cwd().parent.joinpath(folder, subfolder)
    final_folder.mkdir(parents=True,exist_ok=True)
    return final_folder


# This functions checks if the folder is created
def check_dir():
    today = datetime.today().strftime("%d_%m")
    folder = "Ad_library_screens"
    subfolder = f"screenshots_{today}"
    final_folder = pathlib.Path.cwd().parent.joinpath(folder, subfolder)
    return final_folder


if __name__ == "__main__":
    directory = create_dir()
    print(directory)
