from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for x in range(1,10):
    robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
for x in range(8,10):
    robotArm.moveRight()
robotArm.drop()
for x in range(1,6):
    robotArm.moveLeft()
robotArm.grab()
for x in range(6,11):
    robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()