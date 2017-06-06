# Interview-Tasks

For Task 2, I used Python 3 to program the sceduling script. The data structure used to represent the events is a list containing a tuple of string and a list of Unix timestamps. The string is the title of the event and the list of Unix timestamps contains two timestamps. One for the start time of the event and the second is the end time of the event. The algorithm I used was O(N^2). The algorithm compares each event with all other events in the list. If the events conflict both event titles are added to a set. 
