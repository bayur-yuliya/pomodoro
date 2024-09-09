import winsound
import datetime
import time

work_time = int(input('Рабочее время, мин: '))
break_time = int(input('Время перерыва, мин: '))
repetition = int(input('Количество повторений:'))

# start
winsound.Beep(300, 1000)

print(f'Start pomodoro {datetime.datetime.now()}. {repetition} repetition, work time: {work_time}, break time: {break_time}')

while repetition:
    repetition -= 1

    # work time
    time.sleep(work_time * 60)
    winsound.Beep(300, 1000)

    # break time
    time.sleep(break_time * 60)
    winsound.Beep(300, 1000)

print(f'End pomodoro {datetime.datetime.now()}. {repetition} repetition, work time: {work_time}, break time: {break_time}')