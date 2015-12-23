def say_hi():
 print 'this is my module'
__version__ = '0.1'

ab = { 
	'jagrut': 'jagrutsolanki1@gmail.com',
	'hardik': 'hardikpatel1701@gmail.com',
	'hard'  : 'hardchavda1201@gmail.com',
	'mihir' : 'mihirmodi91@gmail.com'
}

print 'jagrut email address is:',ab['jagrut']

del ab['mihir']

print '\n There are {} contacts in address-book\n'.format(len(ab)) 

for name,address in ab.items():
 print 'Contact {} at {} '.format(name,address)

ab['jay'] = 'jaypatel01@gmail.com'

if 'jay' in ab:
 print '\n jay address is',ab['jay']
