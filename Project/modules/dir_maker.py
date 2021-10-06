import pathlib
from datetime import datetime


def create_dir():
    today = datetime.today().strftime("%d_%m")
    folder = "Ad_library_screens"
    subfolder = f"screenshots_{today}"
    final_folder = pathlib.Path.cwd().parent.joinpath(folder, subfolder)
    final_folder.mkdir(parents=True,exist_ok=True)
    return final_folder

def check_dir():
    today = datetime.today().strftime("%d_%m")
    folder = "Ad_library_screens"
    subfolder = f"screenshots_{today}"
    final_folder = pathlib.Path.cwd().parent.joinpath(folder, subfolder)
    return final_folder

if __name__=="__main__":
    dir= create_dir()
    print(dir)
