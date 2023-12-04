import re

with open("input2.txt",encoding="utf-8") as f:
    cubesums=0
    
    lines=f.readlines()
    for line in lines:
        cubes ={"red":0,"green":0,"blue":0}
        roundsum=1
        rounds=line.split(";")
        rounds[0]=rounds[0][7:]
        for i in rounds:
            
            draws=i.strip()
            draws=draws.split(",")
            for key,value in cubes.items():
                
                for j in draws:
                    if key in j:
                        
                        cubes[key]=int(re.findall(r'\d+',j)[0]) if value<int(re.findall(r'\d+',j)[0]) else value
        for value in cubes.values():
            roundsum=roundsum*value
        cubesums+=roundsum
    print(cubesums)
