
table = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

dna = raw_input("Enter the DNA strand ")

if dna in table:
    print "The corresponding RNA complement is %s" %table[dna]
else:
    print "Wrong input"
