import wpilib
import ctre
import magicbot
import math
from components import encodermotor

CONTROLLER_LEFT = wpilib.XboxController.Hand.kLeft
CONTROLLER_RIGHT = wpilib.XboxController.Hand.kRight

self.fullrev=1024
self.starting_position=0
self.current_position=0
self.moveto_position=256

class SwerveModuleTest(magicbot.MagicRobot):

    encodermotor = encodermotor.EncoderMotor

    def createObjects(self):
        self.controller = wpilib.XboxController(0)

        self.drive_motor = ctre.WPI_TalonSRX(1)
        self.encodermotor_motor = ctre.WPI_TalonSRX(5)

        self.current_position = self.starting_position

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass    
        #self.motor_test.set(0.1)
    
    def teleopInit(self):
        self.moveto_position=256
        self.encodermotor.move_incremental(True, self.current_position+self.moveto_position)
        self.current_position=moveto_position

    def teleopPeriodic(self):
        #one motor on right stick (axis 5)
        self.motor_one.set(self.controller.getY(CONTROLLER_RIGHT))

        x_vec = self.controller.getX(CONTROLLER_LEFT)
        y_vec = self.controller.getY(CONTROLLER_LEFT)
        l_trig = self.controller.getTriggerAxis(CONTROLLER_LEFT)

        #magnitude of the left stick
        mag = math.sqrt(x_vec ** 2 + y_vec ** 2)

        #self.steer_motor.set(ctre.WPI_TalonSRX.ControlMode.Position,
        #   5500*math.atan2(y_vec,x_vec)/(math.pi*2))
        
        #0->180 from 0 to 1 radians
        #0->-180 from 0 to -1 radians
        stick_radians=math.atan2(y_vec, x_vec)

        

        #percentage from 0 to 100 for angle of steer motor
        steer_motor_angle=(self.current_position%self.fullrev)/self.fullrev

        



        


        motor_position=self.steer_motor.getSelectedSensorPosition(0)
        print (motor_position, stick_angle, steer_motor_angle, steer_motor_radians)

if __name__ == "__main__":
    wpilib.run(SwerveModuleTest)
    