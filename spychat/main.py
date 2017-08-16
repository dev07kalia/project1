print "Let's get started"
spy_name = raw_input("whats your name ?")

if len(spy_name) >0:
    spy_salutation = raw_input("what should i call you Mr. or Miss?")
    print "welcome " + spy_salutation + " " + spy_name + " glad to have you on board "
else:
    print "you have not entered any name"
spy_age = 0
spy_rating = 0.0
Is_spy_online = False
spy_age = raw_input("what is your age agent ??")
spy_age = int(spy_age)
if spy_age > 16 and spy_age < 60 :
    print "you are eligible to be a spy !!"
else:
    print "sorry !! Not the right time to be a spy ."
spy_rating = raw_input("what is the rating given to you ??")
spy_rating = float(spy_rating)
if spy_rating >= 0 and spy_rating <= 3.5 :
    print "Still need to work on that rating . Go to pakistan for next mission ."
elif spy_rating >= 3.5 and spy_rating <= 7 :
    print "you have some experience , deal with ISIS"
elif spy_rating >= 7 and spy_rating <= 10 :
    print "Welcome pro agent .Waiting for your order ."
spy_is_online = True
print "authentication complete, Welcome" +" "+ spy_salutation + " " + spy_name + "you have a  rating of :" + str(spy_rating)
print ""