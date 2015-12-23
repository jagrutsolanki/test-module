number=23
guess = int(raw_input('Enter any integer:'))
if guess == number:

	print 'congratulation you guesseed it.'
	print '(but you did not win prizes)'
elif guess<number:
	print 'it is little higher'
else:
	print 'it is little lower'
print 'done'
