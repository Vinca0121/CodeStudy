sub = int(input())

score_list = input().split()
score_list = [int(i) for i in score_list]
max_score = max(score_list)
score_list = [i/max_score*100 for i in score_list]
print(sum(score_list)/sub)
