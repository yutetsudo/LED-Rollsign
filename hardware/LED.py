import os
from database.HardwareData import HardwareDatabase

DEBUG = True

class LED_Driver():
    def __init__(self) -> None:
        self.HardwareData = HardwareDatabase().GetHardwareData()

    def Show(self):
        if DEBUG:
            print(f"led-image-viewer --led-rows={self.HardwareData['Rows']} --led-cols={self.HardwareData['Cols']} --led-chain={self.HardwareData['Chain']} --led-parallel={self.HardwareData['Parallel']} --led-brightness={self.HardwareData['Brightness']} --led-slowdown-gpio={self.HardwareData['SlowdownGPIO']} --led-gpio-mapping={self.HardwareData['GPIOMapping']} --led-rgb-sequence={self.HardwareData['RGBSequence']} --led-daemon -s output.gif")
        else:
            os.system(f"led-image-viewer --led-rows={self.HardwareData['Rows']} --led-cols={self.HardwareData['Cols']} --led-chain={self.HardwareData['Chain']} --led-parallel={self.HardwareData['Parallel']} --led-brightness={self.HardwareData['Brightness']} --led-slowdown-gpio={self.HardwareData['SlowdownGPIO']} --led-gpio-mapping={self.HardwareData['GPIOMapping']} --led-rgb-sequence={self.HardwareData['RGBSequence']} --led-daemon -s output.gif")

    def Clear(self):
        if DEBUG:
            print("pkill -u daemon")
        else:
            os.system("pkill -u daemon")
        pass