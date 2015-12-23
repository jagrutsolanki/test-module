shoplist = ['apple','orange','mango','banana']

print 'I have',len(shoplist),'items to purchase.'
print 'The items are'

for item in shoplist:
 print item

print 'I want append rice in shoplist'
shoplist.append('rice')

print len(shoplist)

print 'My new Shopping list is',shoplist

print 'my shorted shopping list is',shoplist.sort()

print shoplist

print 'i now buy one itme',shoplist[0]
del shoplist[0]

print shoplist

