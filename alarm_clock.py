class AlarmClock:
    def __init__(self):
       self.current_time = "11:00"
       self.toggler = bool
       self.alarm_time = " "

    def screen(self):
        print("ALARM APP")
        print("Current time is:", self.current_time)

    def alarm_toggle(self):
        self.set_alarm = input("Alarm On/Off?: ").lower()
        if self.set_alarm == "y":
            self.toggler = True
            print("Toggler: ON")
        else:
            self.toggler = False
            print("Toggler: OFF")
        return self.toggler
    
    def set_alarm_time(self):
        self.alarm_time = input("Set alarm time: ")
        return self.alarm_time
