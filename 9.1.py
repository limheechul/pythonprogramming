scores = []

for i in range(3):
    score = int(input(f"#{i+1}? "))
    scores.append(score)

average = sum(scores) / len(scores)

print("\n[점수 출력]")
print("입력 점수:", ' '.join(str(score) for score in scores))
print(f"평균: {average:.1f}")
