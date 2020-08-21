people = [
    {"name":"Emery", "House": "Gryffindor"},
    {"name":"Earl", "House": "Aberdeen"},
    {"name":"Flora", "House": "Beach"}
]

people.sort(key=lambda person: person["name"])

print(people)