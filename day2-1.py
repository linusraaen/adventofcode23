import re

with open("input2.txt",encoding="utf-8") as f:
    gameidsum=0
    notworking=False
    cubes ={"red":12,"green":13,"blue":14,}
    lines=f.readlines()
    for line in lines:
        rounds=line.split(";")
        rounds[0]=rounds[0][7:]
        for i in rounds:
            if notworking:
                break
            draws=i.strip()
            draws=draws.split(",")
            for key,value in cubes.items():
                if notworking:
                    break
                for j in draws:
                    if key in j:
                        if value<int(re.findall(r'\d+',j)[0]):
                            notworking = True
                            break
        if notworking:
            notworking=False
        else:
            gameidsum+=lines.index(line)+1
    print(gameidsum)


