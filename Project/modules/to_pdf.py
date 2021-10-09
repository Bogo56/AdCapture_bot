from PIL import Image
from Project.modules.dir_maker import check_dir
import pathlib
from datetime import datetime

today=datetime.today().strftime("%d_%m")
today_folder=check_dir().parts[-1]



class PdfBuilder:

    main_dir = pathlib.Path.cwd().parent.joinpath(f"Ad_library_screens")

    @classmethod
    def _get_files(cls, default=True, specify_folder=None):
        if default:
            final_dir = cls.main_dir.joinpath(f"{today_folder}")
        else:
            final_dir = cls.main_dir.joinpath(f"{specify_folder}")
        all_images = list(final_dir.glob("*.png"))
        return all_images


    @classmethod
    def convert_to_pdf(cls, default=True, specify_folder=None, quality=95):
        try:
            if default:
                images = cls._get_files()
                folder = today_folder
            else:
                images = cls._get_files(default=default,
                                        specify_folder=specify_folder)
                folder = specify_folder
            image_files = [Image.open(image) for image in images]
            final_images = [file.convert('RGB') for file in image_files]
            if len(final_images) > 1:
                destination = f"{cls.main_dir}/{folder}/Ads_Preview_{today}.pdf"
                final_images[0].save(destination,
                                     save_all=True,
                                     append_images=final_images[1:],
                                     quality=quality)
            else:
                destination = f"{cls.main_dir}/{folder}/Ads_Preview_{today}.pdf"
                final_images[0].save(destination)
            return (f"Successfully Created Ads_Preview_{today}.pdf",destination)
        except:
            return ("Folder Not Found or Empty",None)




if __name__ =="__main__":
    res = PdfBuilder.convert_to_pdf(default=True, quality=80, specify_folder="screenshots_49_09")
    print(res)