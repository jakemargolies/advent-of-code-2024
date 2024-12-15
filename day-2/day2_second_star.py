def is_safe(row_list):
    diffs = [(j-i) for i, j in zip(row_list[:-1], row_list[1:])]
    return (all([diff > 0 for diff in diffs]) | all([diff < 0 for diff in diffs])) & all([abs(diff) in [1,2,3] for diff in diffs])

input = []
with open('input.txt') as file:
    for line in file:
        line = line.strip().split(" ")
        line = [int(x) for x in line]
        input.append(line)

safe_count = 0
for row in input:
    if is_safe(row):
        safe_count += 1
        continue
    for idx, num in enumerate(row):
        tmp_row = row.copy()
        tmp_row.pop(idx)
        if is_safe(tmp_row):
            safe_count += 1
            break

print(safe_count)