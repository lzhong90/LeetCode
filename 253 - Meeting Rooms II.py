def meeting_room(l):
    s = sorted(l, key=lambda b: b[1])
    rooms =[]
    
    for i in s:
        if not rooms:
            heappush(rooms, i[1])
            continue
        if i[0] < heap[0]:
            heappush(rooms, i[1])
        else:
            heappushpop[rooms, i[1]]
    
    return len(rooms)

a = [[0, 30],[5, 10],[15, 20]]

print(meeting_room(a))
