import re

text_string = input()

regex = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
destinations = []
travel_points = 0
for match in re.finditer(regex, text_string):
    destinations.append(match.group(2))
    travel_points += len(match.group(2))

all_destinations = ", ".join(destinations)
print(f"Destinations: {all_destinations}")
print(f"Travel Points: {travel_points}")
