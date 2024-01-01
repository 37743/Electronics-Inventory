# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Support Popup
# ---
# --------
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup 

class Support():
    def __init__(self, **kwargs):
        boxlayout = BoxLayout(orientation="vertical")
        gridlayout = GridLayout(cols=1)
        message = Label(text="Kindly send us an email specifying your problem so we can get you the right help and support.",
                    halign="center",
                    valign="center",
                    text_size=(360,None),
                    color="black")
        # TODO: Change this email to company email. vvv
        suppemail = Label(text="[u]{e}[/u]".format(e="yousef.gomaa@ejust.edu.eg"),
                    markup=True,
                    halign="center",
                    color="#21d74d")
        dismiss = Button(text="OK", color = "#21d74d",
                        outline_width=2, outline_color ="#ffffff",
                        size_hint=(.5,.5),
                        font_size=18,
                        pos_hint={"center_x": .5, "center_y": .325},
                        background_normal=
                        "app/assets/button.png",
                        background_down=
                        "app/assets/button-down.png")
        gridlayout.add_widget(message)
        gridlayout.add_widget(suppemail)
        gridlayout.add_widget(dismiss)
        boxlayout.add_widget(gridlayout)
        popup = Popup(title="Support",
                    title_color="black",
                    background="app/assets/panel.png",
                    content=boxlayout,
                    size_hint=(None, None), size=(400, 360))
        dismiss.bind(on_press=popup.dismiss)
        popup.open()