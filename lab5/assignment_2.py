from my_robots import NLinkArm

arm = NLinkArm([2,2], [15, 15])

while True:
    arm.plot()