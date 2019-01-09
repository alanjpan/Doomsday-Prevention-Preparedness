# -*- coding: utf-8 -*-
"""
Created on Wed Jan 9 15:13:01 2019

@author: Alan Jerry Pan, CPA, CSc student
@affiliation: Shanghai Jiaotong University

program framework for description and simulation of macro-level doomsday prevention preparedness

Suggested citation as computer software for reference:
Pan, Alan J. (2019). Doomsday Prevention Preparedness [Computer software]. Github repository <https://github.com/alanjpan/Doomsday-Prevention-Preparedness>

Note this software's license is GNU GPLv3.
"""

doomsday_timer = 10
doomsday_counter = 66
humanity_preparedness = 1

continents = ['north america', 'south america', 'asia', 'africa', 'europe', 'oceania']
population = [579, 422, 4436, 1216, 738, 40]
techlevel = [3, 2, 2, 1, 3, 2]
preparedfordoomsday = [4, 1, 10, 1, 3, 1]
doomsdays = 0
year = 2019
pleasure = 0
while doomsday_timer > 0:
        for i in range(len(preparedfordoomsday)):
                humanity_preparedness += techlevel[i] * preparedfordoomsday[i]
        print('humanity readiness for doomsday event: ' + str(humanity_preparedness))

        if humanity_preparedness > doomsday_counter:
                doomsdays += 1
                print('humanity has prepared for ' + str(doomsdays) + ' doomsdays')
                doomsday_timer += 10
                doomsday_counter = int(str(doomsday_counter) + '6')
                print('next doomsday preparation requirements: ' + str(doomsday_counter))
        print('doomsday comes in ' + str(doomsday_timer) + ' years...')
        humanity_preparedness = 0
        print('prepare for doomsday? unite humanity? war? breed? information?')
        response = input().lower()
        if response.startswith('prep'):
                preparedfordoomsday[0] += preparedfordoomsday[0] * .50
                preparedfordoomsday[1] *= .95
                preparedfordoomsday[2] *= .95
                preparedfordoomsday[3] *= .95
                preparedfordoomsday[4] *= .95
                preparedfordoomsday[5] *= .95
        elif response.startswith('unite'):
                missionaries = preparedfordoomsday[0] * .1
                preparedfordoomsday[0] -= missionaries
                print('with which continent?')
                response2 = input().lower()
                if response2.startswith('sou'):
                        preparedfordoomsday[1] += missionaries * 1.4
                        preparedfordoomsday[2] += missionaries * 1.1
                        preparedfordoomsday[3] += missionaries * 1.1
                        preparedfordoomsday[4] += missionaries * 1.1
                        preparedfordoomsday[5] += missionaries * 1.1
                elif response2.startswith('asi'):
                        preparedfordoomsday[1] += missionaries * 1.1
                        preparedfordoomsday[2] += missionaries * 1.4
                        preparedfordoomsday[3] += missionaries * 1.1
                        preparedfordoomsday[4] += missionaries * 1.1
                        preparedfordoomsday[5] += missionaries * 1.1
                elif response2.startswith('afr'):
                        preparedfordoomsday[1] += missionaries * 1.1
                        preparedfordoomsday[2] += missionaries * 1.1
                        preparedfordoomsday[3] += missionaries * 1.4
                        preparedfordoomsday[4] += missionaries * 1.1
                        preparedfordoomsday[5] += missionaries * 1.1
                elif response2.startswith('eur'):
                        preparedfordoomsday[1] += missionaries * 1.1
                        preparedfordoomsday[2] += missionaries * 1.1
                        preparedfordoomsday[3] += missionaries * 1.1
                        preparedfordoomsday[4] += missionaries * 1.4
                        preparedfordoomsday[5] += missionaries * 1.1
                elif response2.startswith('oce'):
                        preparedfordoomsday[1] += missionaries * 1.1
                        preparedfordoomsday[2] += missionaries * 1.1
                        preparedfordoomsday[3] += missionaries * 1.1
                        preparedfordoomsday[4] += missionaries * 1.1
                        preparedfordoomsday[5] += missionaries * 1.4
        elif response.startswith('war'):
                pleasure += 1
                preparedfordoomsday[0] *= .95
                preparedfordoomsday[1] *= .95
                preparedfordoomsday[2] *= .95
                preparedfordoomsday[3] *= .95
                preparedfordoomsday[4] *= .95
                preparedfordoomsday[5] *= .95
                print('you spoil yourself at the expense of the human race')
        elif response.startswith('breed'):
                print('with which continent?')
                response2 = input().lower()
                mated = 0
                if response2.startswith('sou'):
                        mated = (population[0] + population[1]) * .05
                        population[0] += mated
                        population[1] += mated
                        population[2] += mated * .1
                        population[3] += mated * .1
                        population[4] += mated * .1 
                        population[5] += mated * .1
                elif response2.startswith('asi'):
                        mated = (population[0] + population[2]) * .05
                        population[0] += mated
                        population[2] += mated
                        population[1] += mated * .1
                        population[3] += mated * .1 
                        population[4] += mated * .1
                        population[5] += mated * .1
                elif response2.startswith('afr'):
                        mated = (population[0] + population[3]) * .05
                        population[0] += mated
                        population[3] += mated
                        population[1] += mated * .1
                        population[2] += mated * .1 
                        population[4] += mated * .1
                        population[5] += mated * .1
                elif response2.startswith('eur'):
                        mated = (population[0] + population[4]) * .05
                        population[0] += mated
                        population[4] += mated
                        population[1] += mated * .1
                        population[2] += mated * .1 
                        population[3] += mated * .1
                        population[5] += mated * .1
                elif response2.startswith('oce'):
                        mated = (population[0] + population[5]) * .05
                        population[0] += mated
                        population[5] += mated
                        population[1] += mated * .1
                        population[2] += mated * .1 
                        population[3] += mated * .1
                        population[4] += mated * .1
                print('your nation works with ' + response2 + ' to increase population levels')
                print('world population increased ' + str(mated*2.4) + ' million')
        elif response.startswith('info'):
                print(continents)
                print(population)
                print(preparedfordoomsday)
                print()

        for i in range(len(preparedfordoomsday)):
                if preparedfordoomsday[i] > population[i]*techlevel[i]:
                        preparedfordoomsday[i] = population[i]
                        print()
                        print(continents[i] + ' is fully prepared for the apocalypse')
                        print()
        deaths = 0
        death = 0
        for i in range(len(population)):
                death = population[i] * .017
                deaths += death                
                population[i] -= death
        print(str(deaths) + ' people died this year')
        print()

        doomsday_timer = doomsday_timer - 1
        year += 1
print('it is the end of the world...')
print('you survived until ' + str(year))
print('you managed to sneak in ' + str(pleasure) + ' luxuries before the end of the world')
