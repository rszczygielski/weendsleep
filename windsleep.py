import tkinter as tk
import os
import sys
import windsleep_schema
from PIL import Image, ImageTk

class App():
    def __init__(self, windsleepGUI):
        self.root = windsleepGUI
        self.set_root()
        self.set_logo()
        self.slider_objects = self.get_slider_objects()
    
    def set_root(self):
        self.root.title("WindSleep")
        self.root.geometry("900x720")
        icon = Image.open(os.path.join(os.path.join(sys.path[0]), "icon-windsleep.png"))
        test = ImageTk.PhotoImage(icon)
        self.root.wm_iconphoto(False, test)
        self.root.configure(bg="#20bebe")
    
    def set_logo(self):
        logo = tk.PhotoImage(file=os.path.join(os.path.join(sys.path[0]), "logo-color.png"))
        logo_label = tk.Label(self.root, image=logo, bg="#20bebe")
        logo_label.image = logo
        logo_label.pack(padx=0, pady=0)
    
    def set_apply_button(self, command):
        button_apply = tk.Button(self.root, text="Apply", command=command,
        font=("Courier", 20), bg='#20bebe', fg="white")
        button_apply.pack(padx=5, pady=20)
    
    def set_turn_of_button(self, command):
        button_turn_off = tk.Button(self.root, text="Turn Off All", command=command,
        font=("Courier", 20), bg='#20bebe', fg="white")
        button_turn_off.pack(padx=5, pady=10)
            
    def get_slider_objects(self):
        standby_ac = tk.Scale(self.root, from_=0, to=360, orient='horizontal', length=700, label="Standby On battery",
        font=("Courier", 15), highlightbackground="#20bebe", bg="#20bebe", troughcolor="white", fg="white")
        standby_ac.pack(pady=10)
        standby_dc = tk.Scale(self.root, from_=0, to=360, orient='horizontal', length=700, label="Standby On Power",
        font=("Courier", 15), highlightbackground="#20bebe", bg="#20bebe", troughcolor="white", fg="white")
        standby_dc.pack(pady=10)
        monitor_ac = tk.Scale(self.root, from_=0, to=360, orient='horizontal', length=700, label="Monitor On Battery",
        font=("Courier", 15),highlightbackground="#20bebe", bg="#20bebe", troughcolor="white", fg="white")
        monitor_ac.pack(pady=10)
        monitor_dc = tk.Scale(self.root, from_=0, to=360, orient='horizontal', length=700, label="Monitor On Power",
        font=("Courier", 15),highlightbackground="#20bebe", bg="#20bebe", troughcolor="white", fg="white")
        monitor_dc.pack(pady=10)
        return standby_ac, standby_dc, monitor_ac, monitor_dc


if __name__ == "__main__":
    windsleepGUI = tk.Tk()
    appGUI = App(windsleepGUI)
    windsleepInstance = windsleep_schema.SleepMode(appGUI.slider_objects)
    appGUI.set_apply_button(windsleepInstance.run_method)
    appGUI.set_turn_of_button(windsleepInstance.turn_off_all)
    windsleepGUI.mainloop()

    
