#!/usr/bin/python3.7
# UTF8
# Date: Fri 30 Aug 2019 14:41:01 CEST
# Author: Nicolas Flandrois
# License: MIT License
# Version: v1

    # MIT License - Copyright (c) 2019 Nicolas Flandrois

    # Permission is hereby granted, free of charge, to any person obtaining
    # a copy of this software and associated documentation files
    # (the "Software"), to deal in the Software without restriction, including
    # without limitation the rights to use, copy, modify, merge, publish,
    # distribute, sublicense, and/or sell copies of the Software, and to permit
    # persons to whom the Software is furnished to do so, subject to the
    # following conditions:

    # The above copyright notice and this permission notice shall be included
    # in all copies or substantial portions of the Software.

    # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    # OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    # MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    # IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    # CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    # TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    # SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# DESCRIPTION: cf 'The indisputable existence of Santa Claus' by Dr Hannah Fry,
# Chapter 4 'Secret Santa' (p.46 to 54; ISBN 9781784162740).
# This exercice tends to define a Random Hat Picking assignment of
# a Secret Santa, to another participant.

# In this short exercice, we just simply create a pool, according to the number
# of participants, a randomly paired number ID with some other number ID.
# Then a pair is Randomly pulled out of the Bag (Pool list),
# and printed to the screen. (User Scenario 1, Here commented Lines 66 to 70)

# That way each Santa is randomly assigned to a participant.

# (User Scenario 2, Outcome of this current script)
# In a real life situation, we should print out the Secret Santa Pairing list,
# cut the different strips of pairs. People picks in a sorting hat.
# Then We just list Who they are (not who they offer to),
# either right after sorting their pairs,
# or right before opening presents (Adding a bit of mistery).

# Nota Benne: As it is all managed and randomised by a computer, we could
# create a script with names assignements. Same random pairing script, then
# email/sms each pairs to the concerned secret santa, leaving no traces.
# (User Scenario 3, not developped here.)

import random

participants = int(input('How many participants?\t'))

numlist = [i+1 for i in range(participants)]
random.shuffle(numlist)
pair = {}

for n in numlist:
    pair[n] = numlist[numlist.index(n)-1]

scrtsanta = [f'\tI am Secret Santa n° {i}. \tI Annonymously/Secretly offer a \
gift to n° {v}' for i, v in pair.items()]

# print()  # Secret Santa Hat Picking Simulation
# for i in range(len(scrtsanta)):
#     choice = random.choice(scrtsanta)
#     scrtsanta.remove(choice)
#     print(choice)

with open('secretsanta.txt', 'w') as secretsanta:
    text = ['List of participants (please write your name with your number)']

    for i in range(len(scrtsanta)):
        text.append(f'\n\n\t{i+1}.\t........................................')

    text.append('\n\n\n\nSecret Santa Pairing Tickets (Cut, then Hat Picked):')

    for i in scrtsanta:
        text.append(f'\n\n...........................................\n\n{i}')

    textview = " ".join([str(i) for i in text])
    secretsanta.write(str(textview))

print('Finished Process')
