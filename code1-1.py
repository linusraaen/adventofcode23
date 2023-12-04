with open("input1-1",encoding="utf-8") as f:

    total_sum=0
    lines=f.readlines()
    for i in lines:
        numarray=[]
        for letter in i:
            
            letter=letter.strip()
            if letter.isnumeric():
                numarray.append(int(letter))
        total_sum+=(numarray[0]*10)+numarray[-1]
        

    print(total_sum)