class Robot:
    pass
    #constructor
    def __init__(self, battery, arm_lengh):
        self.battery = battery
        self.arm_lengh = arm_lengh
        self.check_day = 365

    def step_forw(self):
        print("Robot made a step forward!")
        self.check_day -= 1
        print(f"Check day in {self.check_day}")

    def step_back(self):
        print("Robot made a step back!")
        self.check_day -= 1
        print(f"Check day in {self.check_day}")


robot_1 = Robot(24, 0.6)
robot_2 = Robot(36, 1.8)
robot_3 = Robot(50, 2.8)
robot_4 = Robot(255, 3)

robot_1.step_forw()

print(robot_1.battery, robot_1.arm_lengh, robot_1.check_day,
      robot_2.battery, robot_2.arm_lengh, robot_2.check_day)
      # robot_3.battery, robot_3.arm_lengh,
      # robot_4.battery, robot_4.arm_lengh, )