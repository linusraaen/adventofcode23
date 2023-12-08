races ={38:241,94:1549,79:1074,70:1091}


ways_to_win=0

for i in range(38947970):
    speed=i
    distance=speed*(38947970-i)
    if distance>241154910741091:
            ways_to_win+=1
    
print(ways_to_win)