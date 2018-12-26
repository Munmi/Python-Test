from sys import argv

script, user_name = argv
prompt = '=> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you few questions."
print "Do you like me %s?" % user_name

likes = raw_input (prompt)

print "where do you live %s?" % user_name

lives = raw_input (prompt)

print "what kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright %r, so you are %r about liking me .
You live in %r.
And you have a %r computer. Nice
""" % (user_name, likes, lives, computer)
