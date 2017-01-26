string = raw_input("Enter a string ")

string = string.lower()

string = string.split()


for i in range(0,len(string)):
    
    test = 1
    
    for j in range(0,i):
        if string[i] == string[j]:
            test = 0
    
    if test == 0:
        continue
    
    count = 0   
    
    for j in range(0,len(string)):
        if string[i] == string[j]:
            count = count +1
    
    print "%s: %d "%(string[i],count)
    
