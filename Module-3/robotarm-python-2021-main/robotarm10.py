from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed=4
i = 1 
for x in range(5):
    for x in range(1,10):
        robotArm.grab()
        robotArm.moveRight()
        robotArm.drop()
        x += x + i

    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()