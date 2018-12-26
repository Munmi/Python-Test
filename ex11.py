from sys import argv

script, filename = argv

file1 = open(filename)

print "Here's your file %r:" % filename
print file1.read()

new_file = raw_input( "Type the filename again:")
file2 = open(new_file)

print file2.read()

