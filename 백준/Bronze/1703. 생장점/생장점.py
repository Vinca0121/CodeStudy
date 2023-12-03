def calculate_leaves(tree_info):
    for tree in tree_info:
        age, *data = tree
        if age == 0:
            break
        
        leaves = 1
        for i in range(age):
            splitting_factor = data[2*i]
            branches_cut = data[2*i + 1]
            leaves *= splitting_factor
            leaves -= branches_cut
        
        print(leaves)

# 입력 처리
tree_info = []
while True:
    tree = list(map(int, input().split()))
    if tree[0] == 0:
        break
    tree_info.append(tree)

# 나뭇잎 수 계산 및 출력
calculate_leaves(tree_info)
