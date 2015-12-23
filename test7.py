number = 23
running = True

while running:
 guess = int(raw_input('Enter an integer:'))

 if guess ==  number:
  print 'You guessed it'
  running = False

 elif guess < number:
   print 'it is little higher than that'
 else:
   print 'it is a little lower than that'
else:
 print 'While loop is over'
 print 'done'

