def total(initial=5,*number,**kewords):
  count = initial
  for num in number:
   count += num
  for key in kewords:
   count += kewords[key]
  return count

print total(10,2,3,vegetable=100,mango=5)
