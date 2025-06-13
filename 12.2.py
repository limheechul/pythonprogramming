import pickle
import os
def input_scores():
    scores = []
    while True:
        score = int(input(f"#{len(scores)+1}? "))
        if score < 0:
            break
        scores.append(score)
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("\n[점수 출력]")
    print("개인점수:", ' '.join(str(score) for score in scores))

def save_score(filename,score):
    with open(filename,'wb') as file:
        pickle.dump(score,file)
def load_score(filename):
    with open(filename,'rb') as file:
        score = pickle.load(file)
        return score
def main():
    if os.path.exists('score.bin'):
        print('[파일 읽기]')
        scores = load_score('score.bin')
    else:
        scores = input_scores()

    show_scores(scores)
    average = get_average(scores)
    print(f"평균: {average:.1f}")
    save_score('score.bin',scores)

main()
