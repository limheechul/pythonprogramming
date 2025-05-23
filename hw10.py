import os
import pickle

FILENAME = "score.bin"

def input_scores():
    scores = []
    while True:
        score = int(input(f"#{len(scores)+1}? "))
        if score < 0:
            break
        scores.append(score)
    return scores

def get_average(scores):
    return sum(scores) / len(scores) if scores else 0

def show_scores(scores):
    print("\n[점수 출력]")
    print("개인점수:", ' '.join(str(score) for score in scores))
    print(f"평균: {get_average(scores):.1f}")

def save_scores(scores):
    with open(FILENAME, "wb") as f:
        pickle.dump(scores, f)

def load_scores():
    with open(FILENAME, "rb") as f:
        return pickle.load(f)

def main():
    if os.path.exists(FILENAME):
        print("[파일 읽기]")
        scores = load_scores()
    else:
        scores = input_scores()
        save_scores(scores)

    show_scores(scores)

main()
