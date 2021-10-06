from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from Project.model.model import Model
from Project.modules.controller import  CaptureBot
from kivy.config import Config


Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
Config.write()

Builder.load_file("capture_menu.kv")
Builder.load_file("database.kv")


class MainMenuScreen(Screen):
    pass


class CaptureMenuScreen(Screen):
    
    pages_list = set()
    added_pages = ObjectProperty(None)

    def add_to_list(self):
        id = self.ids.id.text
        page = self.ids.page_name.text
        if id and page:
            check_id = self._check_id_input(input=id)
            if check_id:
                id = int(id)
                if len(self.pages_list)>0:
                    id_list = [id[1] for id in self.pages_list]
                    if id in id_list:
                        self.ids.scroll_two.text ="ID Already Added"
                        return None

                page_id = (page,id)
                self.pages_list.add(page_id)
                self._add_page_button(page,id)

                print(page_id)
                print(self.pages_list)
        else:
            self.ids.scroll_two.text = "Must Fill Both Fields"


    def add_from_db(self):
        all_pages=Model.get_all()
        all_pages = [page[1:] for page in all_pages ]
        for page in all_pages:
            self.pages_list.add(page)
            self._add_page_button(page_name=page[0],
                                  page_id=page[1])
        print(all_pages)


    def remove_button(self,btn):
        btn_id=int(btn.id)
        for item in self.pages_list:
            if btn_id in item:
                page = item
        self.pages_list.discard(page)
        self.added_pages.remove_widget(btn)


    def clear_list(self):
        self.pages_list.clear()
        for el in self.added_pages.children:
            self.added_pages.remove_widget(el)


    def capture_pages(self):
        check_options = self._check_options()
        if check_options:
            country = self.ids.country.text
            scrolls = int(self.ids.scroll.text)
            if len(self.pages_list)>0:
                self.ids.scroll_two.color = [0, 0, 0, 1]
                self.ids.scroll_two.text = "Started Capturing...."
                pages=list(self.pages_list)
                res = CaptureBot().capture_pages(pages=pages,
                                               country=country,
                                               scrolls=scrolls)
                self.ids.scroll_two.text = res
            else:
                self.ids.scroll_two.text = "Add a Page First"

    def capture_keyword(self):
        check_1 = self._check_keyword()
        check_2 = self._check_options_key()
        if check_1 and check_2 :
            country = self.ids.key_country.text
            scrolls = int(self.ids.key_scroll.text)
            keyword = str(self.ids.keyword.text)
            res = CaptureBot().capture_keyword(keyword=keyword,
                                                  country=country,
                                                  scrolls=scrolls)
            self.ids.scroll_two.text = res
            print(keyword)

    def convert_to_pdf(self):
        quality = int(self.ids.quality.text)
        if self.ids.folder.text == "":
            folder = None
            default = True
        else:
            folder = self.ids.folder.text
            default = False
            print(folder)
        try:
            res = CaptureBot.to_pdf(default=default,
                              quality=quality,
                              specify_folder=folder)
            self.ids.scroll_two.text = res
        except:
            self.ids.scroll_two.text = res


    def _add_page_button(self,page_name,page_id):
        page_button = Factory.ListButton(text=f"{page_name}")
        page_button.id = page_id
        page_button.bind(on_press=self.remove_button)
        self.added_pages.add_widget(page_button)

    def _check_options(self):
        if self.ids.scroll.text == "Scrolls" or self.ids.country.text == "Country":
            self.ids.scroll_two.text = "Choose Scroll and Country Option"
            return False
        else:
            return True
    
    def _check_options_key(self):
        if self.ids.key_scroll.text == "Scrolls" or self.ids.key_country.text == "Country":
            self.ids.scroll_two.color =  (1,0,0,0.7)
            self.ids.scroll_two.text = "Choose Scroll and Country Option"
            return False
        else:
            return True
    
    def _check_keyword(self):
        if self.ids.keyword.text == "":
            self.ids.scroll_two.text = "Enter a Keyword"
            return False
        else:
            return True

    def _check_id_input(self,input):
        if not input.isnumeric():
            self.ids.scroll_two.text = "Please Enter Only Numbers in the ID Field"
            return False
        else:
            return True

    def _check_quality(self):
        if self.ids.keyword.text == "":
            self.ids.scroll_two.text = "Enter a Keyword"
            return False
        else:
            return True




class DataBaseScreen(Screen):
    pass


class ScreenSwitch(ScreenManager):
    pass

class XBotApp(App):
    def build(self):
        Window.clearcolor = (247/255,247/255,247/255,1)
        return ScreenSwitch()


if __name__ == '__main__':
    XBotApp().run()