
def hey(what):
        
    if what.isupper() == True:
        print "Whoa, chill out!"
    elif what[len(what)-1] == '?':
        print "Sure."
    elif what == ' ':
        print "Fine. Be that way!"
    else:
        print "Whatever."
        
    return

message = raw_input()
message = message.strip()
message = ' '+message 

hey(message)
