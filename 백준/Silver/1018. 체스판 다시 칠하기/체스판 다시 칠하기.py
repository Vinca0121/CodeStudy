def changeTile(chess):
    changed_count = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and chess[i][j] != 'B':
                chess[i][j] = 'B'
                changed_count += 1
            elif (i + j) % 2 == 1 and chess[i][j] != 'W':
                chess[i][j] = 'W'
                changed_count += 1
    return changed_count

height, width = map(int, input().split())
chess = []
for i in range(height):
    one_row = input()
    one_list = list(one_row)
    chess.append(one_list)

min_changes = float('inf')

for i in range(height - 7):
    for j in range(width - 7):
        sub_chess = [row[j:j+8] for row in chess[i:i+8]]
        changes = changeTile(sub_chess)
        min_changes = min(min_changes, changes, 64 - changes)

print(min_changes)
