# import the itertools module to gain access to its functions
import itertools

# create a list of all possible permutations of the supplied values
# using the permutations() function from the itertools module
all_options = itertools.permutations(['M','T','H','F'])

# create a dictionary containing the mathematical values of the letters
# corresponding to days of the week
day_values = { 'M' : 1,
               'T' : 2,
               'H' : 4,
               'F' : 5  }

# iterate through each of the possible schedules
for schedule in all_options:
    print("\n\nEvaluating a '{0}' Schedule".format(''.join(schedule)))
    shortest_span = 13  # set the longest possible value as the shortest span
    longest_span = 0    # set the shortest possible value as the longest span

    # iterate through the weeks in each proposed schedule list
    # using enumerate() to get both an index and a value for each one
    for index, value in enumerate(schedule):
        
        # lookup mathematical value of this meeting in the day_values dictionary
        this_meeting = day_values[value]
        
        # calculate the index of the next meeting, using mod4 to accommodate
        # schedule wraparound (i.e. when evaluating the gap between the last
        # meeting in the sequence and the first)
        next_index = (index + 1) % 4
        
        # lookup the mathematical value of the next meeting from day_values
        # ==> that is to say, get the next day in the candidate schedule being
        # evaluated, and look up the mathematical value that corresponds to that
        # letter in the day_values dictionary
        next_meeting = day_values[schedule[next_index]]
        
        # calculate the gap between this meeting and the next
        days_between = next_meeting + 7 - this_meeting
        
        # print out the result of this calculation using the string formatting
        # function --> inserts whatever is within the .format() at the end into
        # the anchor points marked by numbers between curly brackets
        print("In week {0} there are {1} days between this meeting and the next.".format(index + 1, days_between))
        
        # check whether the current gap is the shortest or the longest yet
        # found in this schedule, and if so, keep track of it by setting
        # it as equal to shortest_span or longest_span
        if days_between < shortest_span:
            shortest_span = days_between
        if days_between > longest_span:
            longest_span = days_between

    # after finising inerating through the proposed schedule, report its
    # largest and smallest gaps between meetings
    print("The shortest time between meetings is {0} days".format(shortest_span))
    print("The longest time between meetings is {0} days".format(longest_span))
