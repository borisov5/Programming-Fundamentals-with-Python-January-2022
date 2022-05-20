command = input().split(" -> ")
companies = {}

while command[0] != "End":
    company = command[0]
    id = command[1]
    if company not in companies:
        companies[company] = [id]
    else:
        if id not in companies[company]:
            companies[company].append(id)
    command = input().split(" -> ")

for company, ids in companies.items():
    print(company)
    for id in ids:
        print(f"-- {id}")
