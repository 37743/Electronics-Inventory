# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Login Page
# ---
# --------
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
# from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.uix.popup import Popup 
from app.config.settings import VersionInfo

def change_to_screen(*args, screen):
    App.get_running_app().screen_manager.current = screen
    return

def float_effect(widget, yn, d):
    anim = Animation(y=-yn, duration = d, t="in_out_cubic") + Animation(y=0, duration=d, t="in_out_cubic")
    anim.repeat = True
    anim.start(widget)
    return

class Landing(Screen, FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(Landing, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source = "app/assets/landing-background.png",
                                size = self.size,
                                pos = self.pos)

        self.bind(size = self._update_bg, pos = self._update_bg)

        self.taskbar = FloatLayout()

        ribbon = Image(source="app/assets/ribbon-taskbar.png",
                            pos_hint={"center_x": .5, "center_y": .94},
                            allow_stretch = True)
        self.taskbar.add_widget(ribbon)

        currDB = Label(text="[b] Selected Database:[/b] {db}".format(db=VersionInfo.get_db()),
                             halign='center',
                             color = "#2f2f2f",
                             markup=True,
                             pos_hint={"center_x": .9, "center_y": .93}, font_size=16)
        self.taskbar.add_widget(currDB)

        aboutusbut = Button(text="[b] ABOUT US [/b]", color = "#2f2f2f",
                            markup=True,
                            size_hint=(.12,.08),
                            font_size=16,
                            pos_hint={"center_x": .17, "center_y": .93},
                            background_normal=
                            "app/assets/invis-button.png",
                            background_down=
                            "app/assets/invis-button-down.png")
        self.taskbar.add_widget(aboutusbut)

        supportbut = Button(text="[b] SUPPORT [/b]", color = "#2f2f2f",
                            markup=True,
                            size_hint=(.12,.08),
                            font_size=16,
                            pos_hint={"center_x": .29, "center_y": .93},
                            background_normal=
                            "app/assets/invis-button.png",
                            background_down=
                            "app/assets/invis-button-down.png")
        self.taskbar.add_widget(supportbut)

        self.ui = FloatLayout()

        self.panel = Image(source="app/assets/panel-2.png",
                           allow_stretch = False,
                            pos_hint={"center_x": .5, "center_y": .5})
        self.ui.add_widget(self.panel)

        self.ieemslogo = Image(source="app/assets/ieemslogo.png",
                           allow_stretch = False,
                           size_hint=(.13,.13),
                            pos_hint={"center_x": .5, "center_y": .65})
        self.ui.add_widget(self.ieemslogo)

        # Username Textbox
        self.uicon = Image(source="app/assets/user-icon.png",
                    size_hint = (.08,.08),
                    pos_hint={"center_x": 0.36, "center_y": .525})
        self.ui.add_widget(self.uicon)

        self.userBox = TextInput(multiline=False,
                    size_hint = (.25,.05),
                    hint_text = "USERNAME",
                    pos_hint = {"center_x": .52, "center_y": .525})
        self.ui.add_widget(self.userBox)

        # Password Textbox
        self.picon = Image(source="app/assets/password-icon.png",
                    size_hint = (.08,.08),
                    pos_hint={"center_x": 0.36, "center_y": .425})
        self.ui.add_widget(self.picon)
        self.passBox = TextInput(multiline=False,
                    size_hint = (.25,.05),
                    password = True,
                    hint_text = "PASSWORD",
                    pos_hint = {"center_x": .52, "center_y": .425}) 
        self.ui.add_widget(self.passBox)

        loginbut = Button(text="LOGIN", color = "#21d74d",
                            outline_width=2, outline_color ="#ffffff",
                            size_hint=(.16,.08),
                            font_size=18,
                            pos_hint={"center_x": .5, "center_y": .325},
                            background_normal=
                            "app/assets/button.png",
                            background_down=
                            "app/assets/button-down.png")
        self.ui.add_widget(loginbut)
        
        self.hireui = FloatLayout()
        self.hirepanel = Image(source="app/assets/panel-2.png",
                                size_hint=(.3,.2),
                                allow_stretch = False,
                                pos_hint={"center_x": .9, "center_y": .15})
        self.hireui.add_widget(self.hirepanel)

        hirebut = Button(text="APPLY", color = "#21d74d",
                            outline_width=2, outline_color ="#ffffff",
                            size_hint=(.15,.08),
                            font_size=18,
                            pos_hint={"center_x": .9, "center_y": .1},
                            background_normal=
                            "app/assets/button.png",
                            background_down=
                            "app/assets/button-down.png")
        
        hirejobs = Label(text="[b] Hiring Employees \n&\n Workers! [/b]",
                             halign='center',
                             color = "#2f2f2f",
                             markup=True,
                             pos_hint={"center_x": .9, "center_y": .19}, font_size=16)
        
        self.hireui.add_widget(hirejobs)
        self.hireui.add_widget(hirebut)
        float_effect(self.hireui, -10, 2)
        self.add_widget(self.ui)
        self.add_widget(self.hireui)
        self.add_widget(self.taskbar)

        self.footer = Label(text="This project is exclusively made for CNC-314 Database Systems' Course Project - @github.com/37743",
                             color = "##6ee58b",
                             pos_hint={"center_x": .5, "center_y": .04}, font_size=11)
        self.add_widget(self.footer)
