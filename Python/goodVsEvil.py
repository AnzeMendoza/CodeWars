"""
Description
Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. Different races will certainly be involved. Each race has a certain worth when battling against others. On the side of good we have the following races, with their associated worth:

Hobbits: 1
Men: 2
Elves: 3
Dwarves: 3
Eagles: 4
Wizards: 10
On the side of evil we have:

Orcs: 1
Men: 2
Wargs: 2
Goblins: 2
Uruk Hai: 3
Trolls: 5
Wizards: 10
Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.

Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

Input:
The function will be given two parameters. Each parameter will be a string separated by a single space. Each string will contain the count of each race on the side of good and evil.

The first parameter will contain the count of each race on the side of good in the following order:

Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
The second parameter will contain the count of each race on the side of evil in the following order:

Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

Output:

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
print(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'))
Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of
 Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.
    warrior_good = {"Hobbits": 1, "Men": 2, "Elves": 3, "Dwarves": 3, "Eagles": 4, "Wizards": 10}
    warrior_evil = {"Orcs": 1,"Men": 2,"Wargs": 2,"Goblins": 2,"Uruk Hai": 3,"Trolls": 5,"Wizards": 10}
"""

def goodVsEvil(good, evil):
    warrior_good = [1,2,3,3,4,10]
    warrior_evil = [1,2,2,2,3,5,10]
    good = good.split(' ')
    evil = evil.split(' ')
    acum_evil = 0
    acum_good = 0
 
    for n in range(0, len(good)):
        acum_good += int(good[n])*warrior_good[n]

    for m in range(0,len(evil)):
        acum_evil += int(evil[m])*warrior_evil[m]

    if acum_good > acum_evil:
        return 'Battle Result: Good triumphs over Evil'
    elif acum_good < acum_evil:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'

def goodVsEvil2(good, evil):

    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]
    
    good = sum([int(x)*y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x)*y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '
    
    if good < evil:
        return result +'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'

def goodVsEvil(good, evil):
    good = sum([int(x) * y for x, y in zip(list(good.split(' ')), [1, 2, 3, 3, 4, 10])])
    evil = sum([int(x) * y for x, y in zip(list(evil.split(' ')), [1, 2, 2, 2, 3, 5, 10])])
    result = ['Battle Result: No victor on this battle field', 'Battle Result: Good triumphs over Evil', 'Battle Result: Evil eradicates all trace of Good']
    return result[0] if good == evil else result[1] if good > evil else result[2]
 
 GOOD_WIN = "Battle Result: Good triumphs over Evil"
EVIL_WIN = "Battle Result: Evil eradicates all trace of Good"
DRAW = "Battle Result: No victor on this battle field"

GOOD = [1, 2, 3, 3, 4, 10]
EVIL = [1, 2, 2, 2, 3, 5, 10]

def goodVsEvil(good, evil):
    g = sum(map(lambda x, y: x * y, GOOD, [int(x) for x in good.split(' ')]))
    e = sum(map(lambda x, y: x * y, EVIL, [int(x) for x in evil.split(' ')]))
    return GOOD_WIN if g > e else EVIL_WIN if e > g else DRAW


print(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'))