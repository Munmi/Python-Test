ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "wait let's get few more items"
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Evening"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "adding", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go:", stuff
print "Let's do few things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])
print '#'.join(stuff[5:9])
print '?'.join(stuff[1:9])
print stuff[0]
