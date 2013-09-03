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

# Start a counter to keep track of schedules
# and to enhance readability of results
counter = 0

# Start of list of lists to keep track of schedules, shortest spans between meetings
# and longest spans between meetings
candidates = []

# iterate through each of the possible schedules
for schedule in all_options:
    print("\n\n" + str(counter) + ". Evaluating a {0} Schedule".format(''.join(schedule)))
    
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
    
    meetinggap_differential = longest_span - shortest_span
    
    # Gather information for this particular schedule into a list    
    candidate = [counter, schedule, shortest_span, longest_span, meetinggap_differential] 
    
    # Append the information for this schedule to a growing list of all possible schedules
    candidates.append(candidate)
    
    # Increment the counter    
    counter = counter + 1
    
    # after finising inerating through the proposed schedule, report its
    # largest and smallest gaps between meetings
    print("The shortest time between meetings is {0} days".format(shortest_span))
    print("The longest time between meetings is {0} days".format(longest_span))
    
    # This is the end of the iterator for the schedule.
    # At this point the next proposed schedule will be loaded from all_options
    # and the gaps between its meetings will be checked.

# Set a variable for the longest shortest span
longest_shortest_span = 2

# start a new list of schedules with longest shortest spans
final_candidates = []

for candidate in candidates:
    
    # check each candidate's shortest span against the current longest_shortest_span
    # and add it to a list of final candidates if it's the longest_shortest_span yet
    if candidate[2] > longest_shortest_span:
        longest_shortest_span = candidate[2]    

for candidate in candidates:
    if candidate[2] == longest_shortest_span:
        final_candidates.append(candidate)


        
# output what you've found
print "The longest shortest span for all schedules is {0}, which is found in the following schedules:".format(longest_shortest_span)

# print final_candidates
for candidate in final_candidates:
    schedule = candidate[1]
    print ''.join(schedule)


# out of time. This next bit for evaluating gap differentials. They're all the same anyway!
smallest_meetinggap_differential = 14

    
for candidate in final_candidates:
    if candidate[4] < smallest_meetinggap_differential:
        smallest_meetinggap_differential = candidate[4]
