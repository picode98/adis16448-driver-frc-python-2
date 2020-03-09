import wpilib
from adis16448._adis16448 import ADIS16448_IMU
from os import system

class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        print('Starting gyro init...')
        self.myGyro = ADIS16448_IMU()
        print('Gyro init completed.')

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        pass

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        pass

if __name__ == "__main__":
    system("pause")
    wpilib.run(MyRobot)