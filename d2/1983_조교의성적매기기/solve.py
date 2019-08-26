'''
10 2
87 59 88
99 94 78
94 86 86
99 100 99
69 76 70
76 89 96
98 95 96
74 69 60
98 84 67
85 84 91
'''
N, K = map(int, input().split())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
total_score = []
rank = 0

for n in range(N):
    m, f, a = map(int, input().split())
    total_score.append(m * 0.35 + f * 0.45 + a * 0.2)

# 점수 번호 저장
student_score = total_score[K-1]

for n in range(N):
    if student_score < total_score[n]:  # 상대방의 스코어가 나보다 높을 때, 나의 등수는 +1(낮아진다)
        rank += 1
# print(rank)  # 내가 2등

# 점수계산
grade_limit = N // 10

print(grade[rank // grade_limit])
