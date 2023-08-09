# 3. Goals
def find_best_sequence(goals_list):
    best_sequence = [goals_list[0]]
    for goal in goals_list[1:]:
        if goal >= best_sequence[-1]:
            best_sequence.append(goal)
    return best_sequence


goals = input()
goals_list = [int(goal) for goal in goals.split(", ")]
best_sequence = find_best_sequence(goals_list)
print(" ".join(str(goal) for goal in best_sequence))
