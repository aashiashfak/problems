events = [
    (1, 5),
    (6, 10),
    (4, 7),
    (11, 13)
]
end = 0 
for start, finish in events:
    if start < end:
        print(f"({start}, {end}) break the interval" )
    end = max(end, finish)