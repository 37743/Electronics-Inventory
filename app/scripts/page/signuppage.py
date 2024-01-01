# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Sign-up Page
# ---
# --------
from kivy import utils
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from app.scripts.support import Support
from app.config.settings import VersionInfo
from kivy.core.window import Window

def change_to_screen(*args, screen):
    App.get_running_app().screen_manager.current = screen
    return

# Events
def loginpg_released(instance):
    change_to_screen(screen="Login Page")
    return

def return_released(instance):
    change_to_screen(screen="About Us Page")
    return

def support_released(instance):
    Support()
    return

class Scroll(ScrollView, FloatLayout):
    def __init__(self, **kwargs):
        super(Scroll, self).__init__(**kwargs)
        scrollbox = BoxLayout(orientation="vertical", spacing=-20, padding=(360,16), size_hint_y=None)
        scrollbox.bind(minimum_height=scrollbox.setter('height'))
        # Retailer Data Entry:
        # ---
        # -----
        box0 = BoxLayout(size_hint_y=None)
        self.ieemslogo = Image(source="app/assets/ieemslogo.png",
                           allow_stretch = False,
                           size_hint=(1,1),
                           pos_hint={"center_y": .6})
        box0.add_widget(self.ieemslogo)
        box00 = BoxLayout(size_hint_y=None)
        message = Label(text="Note that you are signing up with our company\n [i] (Electronics Inventory Management System)"\
                        +"[/i]\n as a contracted retailer. Kindly provide your store's location along with your [u]manager's identification information.[/u]\n"\
                            +"[b]Carefully revise your credentials before submitting![/b]",
                    halign="center",
                    valign="center",
                    markup=True,
                    pos_hint={"center_y": .3},
                    text_size=(400,None),
                    color="black")
        box00.add_widget(message)
        scrollbox.add_widget(box0)
        scrollbox.add_widget(box00)
        # First Name
        box1 = BoxLayout(orientation="horizontal", size_hint_y=None)
        ficon = Image(source="app/assets/user-icon.png",
                    size_hint = (.3,.5))
        box1.add_widget(ficon)
        self.firstname = TextInput(multiline=False,
                    size_hint = (1,.3),
                    pos_hint={"center_y": .25},
                    write_tab=False,
                    hint_text = "FIRST NAME")
        box1.add_widget(self.firstname)
        scrollbox.add_widget(box1)

        # Last Name
        box2 = BoxLayout(orientation="horizontal", size_hint_y=None)
        licon = Image(source="app/assets/user-icon.png",
                    size_hint = (.3,.5))
        box2.add_widget(licon)
        self.lastname = TextInput(multiline=False,
                    size_hint = (1,.3),
                    pos_hint={"center_y": .25},
                    write_tab=False,
                    hint_text = "LAST NAME")
        box2.add_widget(self.lastname)
        scrollbox.add_widget(box2)

        # Phone Number
        box3 = BoxLayout(orientation="horizontal", size_hint_y=None)
        picon = Image(source="app/assets/phone-icon.png",
                    size_hint = (.3,.5))
        box3.add_widget(picon)
        self.pnumber = TextInput(multiline=False,
                    input_filter = 'float',
                    write_tab=False,
                    pos_hint={"center_y": .25},
                    size_hint = (1,.3),
                    hint_text = "PHONE NUMBER")
        box3.add_widget(self.pnumber)
        scrollbox.add_widget(box3)

        # Email
        box4 = BoxLayout(orientation="horizontal", size_hint_y=None)
        eicon = Image(source="app/assets/email-icon.png",
                    size_hint = (.3,.5))
        box4.add_widget(eicon)
        self.email = TextInput(multiline=False,
                    write_tab=False,
                    pos_hint={"center_y": .25},
                    size_hint = (1,.3),
                    hint_text = "EMAIL")
        box4.add_widget(self.email)
        scrollbox.add_widget(box4)

        # Location ID
        box4 = BoxLayout(orientation="horizontal", size_hint_y=None)
        eicon = Image(source="app/assets/store-icon.png",
                    size_hint = (.3,.5))
        box4.add_widget(eicon)
        self.location = TextInput(multiline=False,
                    write_tab=False,
                    input_filter = 'float',
                    pos_hint={"center_y": .25},
                    size_hint = (1,.3),
                    hint_text = "LOCATION ID")
        box4.add_widget(self.location)
        scrollbox.add_widget(box4)

        box6 = BoxLayout(orientation="vertical", size_hint_y=None)
        signuperror = Label(text="",
                            halign="center",
                            color = "red",
                            size_hint=(1,1),
                            font_size=12)
        box6.add_widget(signuperror)
        signupbut = Button(text="SIGN-UP", color = "#21d74d",
                            outline_width=2, outline_color ="#ffffff",
                            size_hint=(1,1),
                            font_size=18,
                            background_normal=
                            "app/assets/button.png",
                            background_down=
                            "app/assets/button-down.png")
        box6.add_widget(signupbut)
        scrollbox.add_widget(box6)

        self.size_hint=(1, None)
        self.size=(Window.width, Window.height-140)
        self.pos_hint = {'center_x': 0.5, 'center_y': 0.465}
        self.bar_color = utils.get_color_from_hex("ffffff")
        self.bar_inactive_color = utils.get_color_from_hex("757575")
        self.bar_width = 10
        self.scroll_type = ['bars','content']  
        self.add_widget(scrollbox)
  
class Signup(Screen, FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(Signup, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source = "app/assets/background.png",
                                size = self.size,
                                pos = self.pos)

        self.bind(size = self._update_bg, pos = self._update_bg)

        self.taskbar = FloatLayout()

        ribbon = Image(source="app/assets/ribbon-taskbar.png",
                            pos_hint={"center_x": .5, "center_y": .94})
        self.taskbar.add_widget(ribbon)

        currDB = Label(text="[b] Selected Database:[/b] {db}".format(db=VersionInfo.get_db()),
                             halign='center',
                             color = "#2f2f2f",
                             markup=True,
                             pos_hint={"center_x": .9, "center_y": .93}, font_size=16)
        self.taskbar.add_widget(currDB)
        loginpgbut = Button(text="[b] LOGIN [/b]", color = "#2f2f2f",
                            markup=True,
                            size_hint=(.12,.08),
                            font_size=16,
                            pos_hint={"center_x": .17, "center_y": .93},
                            background_normal=
                            "app/assets/invis-button.png",
                            background_down=
                            "app/assets/invis-button-down.png")
        loginpgbut.bind(on_release=loginpg_released)
        self.taskbar.add_widget(loginpgbut)

        supportbut = Button(text="[b] SUPPORT [/b]", color = "#2f2f2f",
                            markup=True,
                            size_hint=(.12,.08),
                            font_size=16,
                            pos_hint={"center_x": .29, "center_y": .93},
                            background_normal=
                            "app/assets/invis-button.png",
                            background_down=
                            "app/assets/invis-button-down.png")
        supportbut.bind(on_release=support_released)
        self.taskbar.add_widget(supportbut)
        
        self.add_widget(self.taskbar)

        self.panel = Image(source="app/assets/panel-4.png",
                           allow_stretch = False,
                           pos_hint={"center_x": .5, "center_y": .465})
        self.add_widget(self.panel)
        
        self.add_widget(Scroll())

        returnbut = Button(size_hint=(None,None),
                           size=(75,75),
                           pos_hint={"center_x": .93, "center_y": .8},
                           background_normal="app/assets/back-icon.png",
                           background_down="app/assets/back-icon-down.png")
        returnbut.bind(on_release=return_released)
        self.add_widget(returnbut)

        self.footer = Label(text="This project is exclusively made for CNC-314 Database Systems' Course Project - @github.com/37743",
                             color = "##6ee58b",
                             pos_hint={"center_x": .5, "center_y": .04},
                             font_size=11)
        self.add_widget(self.footer)