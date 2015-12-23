try:
 text = raw_input("Enter something")
except EOFError:
 print "Why you do end of file?"
except KeyboardInterrupt:
 print "you cancle operation"
else:
 print 'you entered {}'.format(text)
