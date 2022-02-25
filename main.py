import time

import pyscreenshot as ImageGrab
import schedule



from datetime import datetime

def take_screenshot():
    image_name = f"screenshot-{str(datetime.now())}"
    screenshot = ImageGrab.grab()
    
    filepath= f"./screenshot/{image_name}"
    
    screenshot.save(filepath)
    
    return filepath


def main():
    schedule.every(60).seconds.do(take_screenshot)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()