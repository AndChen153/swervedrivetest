import wpilib
import ctre
import magicbot
import math
from components import encodermotor

CONTROLLER_LEFT = wpilib.XboxController.Hand.kLeft
CONTROLLER_RIGHT = wpilib.XboxController.Hand.kRight


class SwerveModuleTest(magicbot.MagicRobot):

    steermotor = encodermotor.EncoderMotor

    def createObjects(self):
        self.controller = wpilib.XboxController(0)

        self.drive_motor = ctre.WPI_TalonSRX(1)

        self.steer_motor = ctre.WPI_TalonSRX(5)


    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass    
        #self.motor_test.set(0.1)
    
    def teleopPeriodic(self):
        #one motor on right stick (axis 5)
        self.motor_one.set(self.controller.getY(CONTROLLER_RIGHT))

        x_vec = self.controller.getX(CONTROLLER_LEFT)
        y_vec = self.controller.getY(CONTROLLER_LEFT)
        l_trig = self.controller.getTriggerAxis(CONTROLLER_LEFT)

        #magnitude of the left stick
        mag = math.sqrt(x_vec ** 2 + y_vec ** 2)

        #one full revolution
        position=1024

        #self.steer_motor.set(ctre.WPI_TalonSRX.ControlMode.Position,
        #   5500*math.atan2(y_vec,x_vec)/(math.pi*2))
        

        self.steer_motor.set(ctre.WPI_TalonSRX.ControlMode.Position)

        motor_position=self.steer_motor.getSelectedSensorPosition(0)
        print (motor_position,5500*math.atan2(y_vec,x_vec)/(math.pi*2))

if __name__ == "__main__":
    wpilib.run(SwerveModuleTest)
    