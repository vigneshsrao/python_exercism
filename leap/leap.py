def leap(year):
    if (year%4)==0:
	if (year%100)==0:
	  if (year%400)==0:
	    res = "leap"
	  else:
	    res = "not leap"
	else:
	  res = "leap"
    else:
	res = "not leap"
    return res

year1 = input("Enter a year ")
ans = leap(year1)
print "The year %d is %s "% (year1,ans)
