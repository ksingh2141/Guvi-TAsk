people = [
    {"name": "Rahul", "age": 17},
    {"name": "Amit", "age": 21},
    {"name": "Neha", "age": 19},
    {"name": "Riya", "age": 15},
    {"name": "Karan", "age": 25}
]


adults = filter(lambda person: person['age'] >= 18, people)


adult_names = list(map(lambda person: person['name'], adults))

print(adult_names)