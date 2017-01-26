strand1 = raw_input("Enter the first strand ")
strand2 = raw_input("Enter the second strand ")

strand1= strand1.replace(' ', '')
strand2= strand2.replace(' ', '')

strand1 = list(strand1)
strand2 = list(strand2)
table = ['G','C','A','T']

t=1

for i in strand1:
    if i not in table:
        t=0
        
for i in strand2:
    if i not in table:
        t=0
        
        
if len(strand1) != len(strand2):
    print "Length don't match"
    
elif t==0:
    print "Wrong input"
    
else:
    count = 0

    for i in range(0,len(strand1)):
        if strand1[i] != strand2[i]:
            count = count+1
    
    print "Hamming distance is %d"%count
        
