input = {
    "users": [
        {
            "name": "John",
        },
        {
            "name": "Bob",
        },
        {
            "name": "Christophar",
        },
    ]
}

# order by the length of names in descending order
def order_names_fn(input):
    for k , v in input.items() :
        order_names = sorted(v, key=lambda x: len(x['name']), reverse=True)
    return order_names
print(order_names_fn(input))


employees_by_department = {
    "Engineering": [
        {"name": "Alice", "experience": 3},
        {"name": "Zara", "experience": 1},
    ],
    "Marketing": [
        {"name": "John", "experience": 2},
        {"name": "Bob", "experience": 4}
    ],
}

# order employees by their experience in descending order
employees = []
for k, v in employees_by_department.items():
    employees.extend(v)
    sorted_employees = sorted(employees, key=lambda x: x["experience"], reverse=True)
print(sorted_employees)

# find top 3 players with highest scores
teams = {
    "TeamA": [
        {"name": "Alice", "score": 90},
        {"name": "Bob", "score": 75},
    ],
    "TeamB": [
        {"name": "Charlie", "score": 85},
        {"name": "Zara", "score": 95},
        {"name": "John", "score": 70},
    ],
}

players = [player for team in teams.values() for player in team]
top_players = sorted(players, key=lambda x: x["score"], reverse=True) 
print(top_players[:3])
