# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Electronics Inventory Management System for Suppliers
# Driver Code
# ---
import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
from app.config import settings
from app.scripts.page import loginpage
from app.scripts.page import aboutpage

from kivy.core.window import Window
Window.size = (1024, 640)
Window.minimum_width = 768
Window.minimum_height = 512

class App(App):
    def build(self):
        self.title = settings.VersionInfo.get_title()
        self.icon = "app/assets/ejust-project-icon.png"
        self.login = loginpage.Login(name="Login Page")
        self.about = aboutpage.About(name="About Us Page")
        self.screen_manager = ScreenManager(transition = WipeTransition())

        for screen in [self.about, self.login]:
            self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__ == '__main__':  
    main = App()
    main.run()