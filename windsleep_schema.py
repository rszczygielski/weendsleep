import os
import argparse

class Slider():
    def __init__(self, mode, type, value):
        self.name = f"{mode}_{type}"
        self.mode = mode
        self.type = type
        self.value = value

class SleepMode():
    def __init__(self, slider_object_tuple):
        self.standby_ac = slider_object_tuple[0]   
        self.standby_dc = slider_object_tuple[1]   
        self.monitor_ac = slider_object_tuple[2]   
        self.monitor_dc = slider_object_tuple[3]

    def get_slider_structs(self, standby_ac, standby_dc, monitor_ac, monitor_dc):
        list_of_slider_stucts = []
        list_of_slider_stucts.append(Slider("standby", "ac", standby_ac.get()))
        list_of_slider_stucts.append(Slider("standby", "dc", standby_dc.get()))
        list_of_slider_stucts.append(Slider("monitor", "ac", monitor_ac.get()))
        list_of_slider_stucts.append(Slider("monitor", "dc", monitor_dc.get()))
        return list_of_slider_stucts

    def set_sleep_timer(self, mode:str, type:str,  value:int):
        os.system(f"powercfg /change {mode}-timeout-{type} {value}")
    
    def turn_off_all(self):
        os.system("powercfg /change standby-timeout-ac 0")
        os.system("powercfg /change standby-timeout-dc 0")
        os.system("powercfg /change monitor-timeout-ac 0")
        os.system("powercfg /change monitor-timeout-dc 0")

    def run_method(self):
        list_of_slider_structs = self.get_slider_structs(self.standby_ac, self.standby_dc, self.monitor_ac, self.monitor_dc)
        for slider_struct in list_of_slider_structs:
            if slider_struct.value == 0:
                continue
            else:
                self.set_sleep_timer(slider_struct.mode, slider_struct.type, slider_struct.value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Program sets the computer sleep options")
    parser.add_argument("-st", metavar="sleep_type", dest="sleep_type", choices=["standby", "monitor"])
    parser.add_argument("-pt", metavar="power_type", dest="power_type", choices=["ac", "dc"], default="ac")
    parser.add_argument("-t", metavar="time", dest="time", default=0)
    args = parser.parse_args()
    print(args)
    sleep_type = args.sleep_type
    power_type = args.power_type
    time = args.time

    print(sleep_type, power_type, time)
    sleepMode = SleepMode()
    sleepMode.set_sleep_timer("standby", "ac", 0)
