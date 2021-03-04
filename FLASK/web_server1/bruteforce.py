


c = 0
i = 1
pw = [32,]
while 1:
    
    
    
    
    

    for t in range(0,len(pw)):
        if t!=len(pw)-1 and pw[t+1] == 40:
            pw[t]+=1
            pw[t+1]= 32
            pw.append(32)
            pw[t-1]+=1
        elif t==len(pw)-1:
            pw[t]+=1
            if(pw[t]==40):
                pw.append(32)
                pw[t]=32
                t -=1
            
    print(pw)
    

