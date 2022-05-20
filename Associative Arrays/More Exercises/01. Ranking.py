def first_contest():
    first_dictionary = {}
    data = input().split(":")
    while data[0] != "end of contests":
        contest = data[0]
        password_for_contest = data[1]
        first_dictionary[contest] = password_for_contest
        data = input().split(":")

    return first_dictionary


def second_contest():
    second_dictionary = {}
    data = input().split("=>")
    while data[0] != "end of submissions":
        contest = data[0]
        password_for_contest = data[1]
        username = data[2]
        points = int(data[3])
        if username not in second_dictionary:
            second_dictionary[username] = [contest, password_for_contest, points]
        else:
            second_dictionary[username].append(contest)
            second_dictionary[username].append(password_for_contest)
            second_dictionary[username].append(points)
        data = input().split("=>")

    return second_dictionary


def candidates():
    result = {}
    first_dictionary = first_contest()
    second_dictionary = second_contest()
    best_candidate = ""
    total_points = 0

    for name, values in second_dictionary.items():
        for i in range(0, len(values), 3):
            if values[i] in first_dictionary.keys():
                if values[i + 1] == first_dictionary[values[i]]:
                    if name not in result:
                        result[name] = [values[i], values[i + 2]]
                    else:
                        if (values[i] in result[name]) and values[i + 2] < result[name][1]:
                            pass
                        else:
                            result[name].append(values[i])
                            result[name].append(values[i + 2])

    for candidate in result.keys():
        user_points = 0
        for point in range(1, len(result[candidate]), 2):
            user_points += result[candidate][point]
        if user_points > total_points:
            total_points = user_points
            best_candidate = candidate
    print(f"Best candidate is {best_candidate} with total {total_points} points.")
    print("Ranking:")
    names = sorted(result.keys())
    for name in names:
        print(name)
        current_result = {}
        for index in range(0, len(result[name]), 2):
            course = result[name][index]
            points = result[name][index + 1]
            current_result[course] = points

        sorted_result = sorted(current_result.items(), key=lambda x: (-x[1], x[0]))
        for i in range(len(sorted_result)):
            print(f"#  {sorted_result[i][0]} -> {sorted_result[i][1]}")


candidates()
