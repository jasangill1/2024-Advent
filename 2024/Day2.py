data = """1 3 6 7 9
1 3 6 7 9
1 5 8 9 2
"""


grouped = data.strip().split('\n')

cleaned = [list(map(int, group.split()))for group in grouped]

count = 0

for group in cleaned:
    check = True
    firstNum = group[0]
    increase = all(group[i] > group[i - 1] for i in range(1, len(group)))
    decrease = all(group[i] < group[i - 1] for i in range(1, len(group)))

    inLimit = all(group[i] < group[i - 1] <= 3 for i in range(1, len(group)))

    if (increase or decrease) and inLimit:
        count += 1
    else:
        for num in range(len(group)):
            temp_group = group[:num] + group[num + 1:]
            increasing = all(temp_group[j] > temp_group[j - 1]
                             for j in range(1, len(temp_group)))
            decreasing = all(temp_group[j] < temp_group[j - 1]
                             for j in range(1, len(temp_group)))
            within_limit = all(
                abs(temp_group[j] - temp_group[j - 1]) <= 3 for j in range(1, len(temp_group)))

            if (increasing or decreasing) and within_limit:
                count += 1
                break


print(count)
