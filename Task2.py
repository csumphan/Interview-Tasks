#1487890800 1487896200
#1488052800 1488056400
#1487984400 1487986200
#1487962800 1487986200

#Assume that the date and time will be in timestamp form

events = [("Interview at The Portal",[1487890800,1487896200]),
          ("'Lunch with Cindy'",[1488052800,1488056400]),
          ("Dinner with John",[1487984400,1487986200]),
          ("Conference",[1487962800,1487986200]),
          ("Career Fair",[1487962800,1487986200]),
          ("Lunch with Tom",[1487962800,1487986200]),
          ("Bruch with Jeff",[1487962800,1487986200]),
          ("Work on Project",[1487962300,1487986200])]

def findConflict(events):
    conflict = set()
    for x in range(len(events)):
        for y in range(x+1,len(events)):
            if((events[x][1][0] >= events[y][1][0] and events[x][1][0] <= events[y][1][1])):
                conflict.add(events[x][0])
                conflict.add(events[y][0])
    return conflict
        

ans = list(findConflict(events))

print(ans)
