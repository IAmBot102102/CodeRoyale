import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    my_score = int(input())
    enemy_score_1 = int(input())
    enemy_score_2 = int(input())
    my_rage = int(input())
    enemy_rage_1 = int(input())
    enemy_rage_2 = int(input())
    unit_count = int(input())
    for i in range(unit_count):
        inputs = input().split()
        unit_id = int(inputs[0])
        unit_type = int(inputs[1])
        player = int(inputs[2])
        mass = float(inputs[3])
        radius = int(inputs[4])
        x = int(inputs[5])
        y = int(inputs[6])
        vx = int(inputs[7])
        vy = int(inputs[8])
        extra = int(inputs[9])
        extra_2 = int(inputs[10])

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("WAIT")
    print("WAIT")
    print("WAIT")