from alarm_clock import AlarmClock

run_alarm_clock = AlarmClock()
screen = run_alarm_clock.screen()
toggler = run_alarm_clock.alarm_toggle()
while toggler == True:
    print("Alarm will go off at:", run_alarm_clock.set_alarm_time())
    toggler = False
    


        


