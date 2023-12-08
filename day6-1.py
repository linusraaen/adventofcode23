races ={38:241,94:1549,79:1074,70:1091}

wins=1

for key,value in races.items():
    ways_to_win=0
    for i in range(key):
        speed=i
        distance=speed*(key-i)
        if distance>value:
            ways_to_win+=1
    if ways_to_win!=0:
        wins=wins*ways_to_win
print(wins)