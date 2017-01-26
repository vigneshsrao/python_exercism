
test = raw_input("Enter a string\n")
pang = list(test)

for i in range(65,91):
    if chr(i) in pang:
        flag = 1
    elif chr(i).lower() in pang:
        flag = 1
    else:
        flag = 0
        break
    
if flag == 0:
    print "This string is not a pangram"
else:
    print "This string is a pangram"
