def total(initial=5, *numbers, **keywords):
 count = initial
 for number in numbers:
  count = count+number
 for key in keywords:
  count  = count+keywords[key]
 return count

print total(10,1,2,3,vg=20,fr=100)
