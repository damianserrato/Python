heads = 0
tails = 0

import random
for i in range(1, 501):
    chance = random.random()*1
    chance = round(chance)
    if chance == 1.0:
        heads += 1
        print "Attempt #: ", i, "Throwing a coin... it's a head!... Got ", heads, " head(s) so far and ", tails, "tail(s) so far"
    elif chance == 0.0:
        tails += 1
        print "Attempt #: ", i, "Throwing a coin... it's a tail!... Got ", heads, " head(s) so far and ", tails, "tail(s) so far"