intervals = [[1, 3], [8,10], [2, 6], [15, 18]]

def find_overlaps (intervals):
    l = len(intervals)
    if l == 0:
        return []
    intervals.sort(key=lambda x: x[0])
    overlaps = []
    start , end = intervals[0]

    for i in range(1, l):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            overlaps.append([start, end])
            start, end = intervals[i]  
    overlaps.append([start, end])
    return overlaps

print( find_overlaps(intervals) )  
