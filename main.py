# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

from pydub import AudioSegment
from datetime import datetime
from pydub.playback import play


def breaktime(sound):
    while True:
        time.sleep(1200)
        print('Take a break')
        for i in range(3):
            play(sound)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        t = datetime.now().time()
        time.sleep(60)
        if t.minute == 0 or t.minute == 20 or t.minute == 40:
            soundFile = AudioSegment.from_wav('soundfile.wav')
            print('Starting ...')
            breaktime(soundFile)
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
