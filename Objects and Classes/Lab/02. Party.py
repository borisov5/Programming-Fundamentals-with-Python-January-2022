class Party:
    def __init__(self):
        self.people = []

    def get_info(self):
        all_people = self.people
        people_res = ", ".join(all_people)
        return f"""Going: {people_res}
Total: {len(self.people)}"""

person_input = input()
party = Party()
while person_input != "End":
    party.people.append(person_input)
    person_input = input()

info = party.get_info()
print(info)
