with open("input1-1",encoding="utf-8") as f:
    words = ["one","two","three","four","five","six","seven","eight","nine"]
    total_sum=0
    lines=f.readlines()
    skip=False
    for i in lines:
        numarray=[]
        
        for j in range(len(i)):
            if skip:
                skip=False
                continue
            if i[j].isdigit():
                numarray.append(int(i[j]))
                continue
            if j+1!=len(i):
                if i[j+1].isdigit():
                    numarray.append(int(i[j+1]))
                    skip=True
                    continue
            for number in words:
                if j+5>=len(i):
                    if number in i[j:j+4]:
                        numarray.append(words.index(number)+1)
                        break
                if j+4>=len(i):
                    if number in i[j:j+3]:
                        numarray.append(words.index(number)+1)
                        break
                if j+3>=len(i):
                    continue    
                if number in i[j:j+5]:
                    numarray.append(words.index(number)+1)

        total_sum+=(numarray[0]*10)+numarray[-1]
        

    print(total_sum)