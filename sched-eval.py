# import the permutations function from the module itertools
from itertools import permutations

# create a list of all possible permutations of the supplied values
# using the permutations function 
all_options = permutations(['M','T','H','F'])

# create a dictionary containing the mathematical values of the days
# corresponding to each letter given above
day_values = { 'M' : 1,
               'T' : 2,
               'H' : 4,
               'F' : 5  }

# iterate through each of the possible schedules
for schedule in all_options:
    print("\n\nEvaluating a {0} Schedule".format(''.join(schedule)))
    
    # set one more than the longest possible value as the shortest span
    shortest_span = 12
    
    # set one less than the shortest possible value as the longest span
    longest_span = 2    

    # iterate through the items in each proposed schedule list
    # using enumerate() to get both an index (= position) and the value
    # (= day_letter) for each one
    for position, day_letter in enumerate(schedule):
        
        # lookup mathematical value of the current meeting in the day_values
        # dictionary
        this_meeting = day_values[day_letter]
        
        # calculate the index of the next meeting date in the series,
        # using modulus (% 4) to accommodate any possible wraparound
        # (i.e. when evaluating the gap between the last meeting in the
        # sequence and the first)
        next_index = (position + 1) % 4
        
        # lookup the mathematical value of the next meeting from day_values
        # ==> that is to say, get the letter of the next item in the series being
        # evaluated, and look up the mathematical value that corresponds to that
        # letter in the day_values dictionary
        next_meeting = day_values[schedule[next_index]]
        
        # calculate the gap between this week's meeting and the next
        gap = next_meeting + 7 - this_meeting
        
        # print out the result of this calculation using the string formatting
        # function, which inserts the items within the .format() appended to the
        # string into the anchor points marked by numbers in curly brackets
        print("Week {0}: There are {1} days between {2} and {3}.".format(position + 1, gap, day_letter, schedule[next_index]))
        
        # check whether the current gap is the shortest or the longest
        # found so far in this particular schedule, and if so, keep track of it
        # by setting shortest_span or longest_span, respectively, equal to it
        if gap < shortest_span:
            shortest_span = gap
        if gap > longest_span:
            longest_span = gap
            
        # End of the loop that evaluates the gap between meetings
        # This section will repeat until the entire schedule has been checked

    # after finising inerating through the proposed schedule, report its
    # largest and smallest gaps between meetings
    print("The shortest time between meetings is {0} days".format(shortest_span))
    print("The longest time between meetings is {0} days".format(longest_span))
    
    # This is the end of the iterator for the schedule.
    # At this point the next proposed schedule will be loaded from all_options
    # and the gaps between its meetings will be checked.
