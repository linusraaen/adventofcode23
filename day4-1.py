with open("input4.txt") as f:
    summed=0
    lines=f.readlines()
    for line in lines:
        for i in range(winning):
            
        winning = 0
        win=line[10:41]
        mine=line[42:-1]
        win=win.split()
        mine=mine.split()
        for i in win:
            if i in mine:
                winning+=1
        if winning>0:
            summed+=pow(2,winning-1)
    print(summed)