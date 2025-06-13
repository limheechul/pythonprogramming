scores = []

for i in range(3):
    score = int(input(f"#{i+1}? "))
    scores.append(score)

average = sum(scores) / len(scores)

print("\n[점수 출력]")
print("입력 점수:", ' '.join(str(score) for score in scores))
print(f"평균: {average:.1f}")

print('\n[검색]')
s = int(input('찾고자 하는 점수는? '))
if s in scores:
    idx = scores.index(s)
    print(f'{s}점은 {idx + 1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')
