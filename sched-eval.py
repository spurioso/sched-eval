import itertools

all_options = itertools.permutations(['M','T','H','F'])

day_values = { 'M' : 1,
               'T' : 2,
               'H' : 4,
               'F' : 5  }

for schedule in all_options:
    print("\n\nEvaluating a '{0}' Schedule".format(''.join(schedule)))
    shortest_span = 15
    longest_span = 0

    for index, value in enumerate(schedule):
        this_meeting = day_values[value]
        next_index = (index + 1) % 4
        next_meeting = day_values[schedule[next_index]]
        days_between = next_meeting + 7 - this_meeting
        print("In week {0} there are {1} days between this meeting and the next.".format(index + 1, days_between))
        if days_between < shortest_span:
            shortest_span = days_between
        if days_between > longest_span:
            longest_span = days_between

    print("The shortest time between meetings is {0} days".format(shortest_span))
    print("The longest time between meetings is {0} days".format(longest_span))
