import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.random.randint(low=1, high=3, size=(5,2))
#checking randint method


def monty_hall():
    
    [[selected_door, winning_door]] = np.random.randint(low=1,high=3,size=(1,2))
    # selecting random integer as door 1,2 and 3
    
    door_options = [1,2,3]
    
    if selected_door == winning_door:
        
        #when the contestant's initial selection is the winning door 
        # monty chosses the two remaining doors at random. Both remaining doors contain goats.
        door_options.remove(selected_door)
        open_door = np.random.choice(door_options)
        
        # the door in which a contestant would switch to contains a goat.
        switching_door = door_options.remove(open_door)
    else:
        
        #when the contestant's initial selection does not contain a car 
        #initial  selection contains a goat. monty then opens the other door containing a goat, 
        #leaving the car behind the switching door.
        door_options.remove(selected_door)
        door_options.remove(winning_door)
        open_door = door_options
        
        switching_door = winning_door

    #win is indicated with a 1 and a loss is indicated with a 0.
    if switching_door == winning_door:
        switch = 1.
        non_switch = 0.
    else:
        switch = 0.
        non_switch = 1.

    return switch, non_switch
    
#this function simulates one go of the problem to test bayes theorem on (switching/non-switching basis) we will sumulate multiple times

def simulate_monty_hall(simulations):
    #number of simulations

    switching_results = []
    not_switching_results = []

    for x in range(100):
        switch, non_switch = monty_hall()

        switching_results.append(switch)
        not_switching_results.append(non_switch)
        
    return switching_results, not_switching_results

switching_results, not_switching_results = simulate_monty_hall(1000000)

print ('The winning percentage when switching was: %s' % str(sum(switching_results) / len(switching_results)))
print ('The winning percentage when not switching was %s' % str(sum(not_switching_results) / len(not_switching_results)))

# cumulative percentages
cumulative_switching = np.cumsum(switching_results) / np.arange(1, 100 + 1) * 100
cumulative_not_switching = np.cumsum(not_switching_results) / np.arange(1, 100 + 1) * 100

#plotting
plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, 100 + 1), cumulative_switching, label='Switching')
plt.plot(np.arange(1, 100 + 1), cumulative_not_switching, label='Not Switching')
plt.xlabel('Number of Simulations')
plt.ylabel('Winning Percentage')
plt.title('Monty Hall Simulation Results')
plt.legend()
plt.show()
