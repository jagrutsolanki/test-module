poem ='''\prog of python'''
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

f = open('poem.txt')
while True:
 line = f.readline()

if len(line) == 0:
 break

print line,
f.close()
