def helloworld(name="World"):
	return name

user_name = raw_input("What is your name ? ")

if(user_name == ""):
	name = helloworld()
else:
	name = helloworld(user_name)
 
print "Hello, %s"% name
