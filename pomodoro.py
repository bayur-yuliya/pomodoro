import winsound
import datetime
import time
import logging

logging.basicConfig(level=logging.INFO, filename="history.txt", filemode="a", format="%(asctime)s %(levelname)s %(message)s")

work_time = int(input('Рабочее время, мин: '))
break_time = int(input('Время перерыва, мин: '))
repetition = int(input('Количество повторений: '))

# start
winsound.Beep(300, 1000)

logging.info(f'Start. {repetition} repetition, work time: {work_time}, break time: {break_time}')

while repetition:
    repetition -= 1

    # work time
    time.sleep(work_time * 60)
    winsound.Beep(300, 1000)
    logging.info('Work time end')

    # break time
    time.sleep(break_time * 60)
    winsound.Beep(300, 1000)
    logging.info('Break time end')

logging.info(f'End. {repetition} repetition, work time: {work_time}, break time: {break_time}')
