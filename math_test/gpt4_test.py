from dotenv import load_dotenv

# 환경변수 세팅
load_dotenv("../.env")


import pandas as pd
import random

def get_gpt4_answer(question_text):
    # Placeholder function for GPT-4 API call
    # Replace this with actual GPT-4 API call when running the script in an appropriate environment
    return random.randint(1, 4)

def calculate_accuracy_and_score(file_path):
    data = pd.read_csv(file_path)
    data['답변'] = data['텍스트'].apply(get_gpt4_answer)
    data['Correct'] = data['답변'] == data['정답']
    score = data[data['Correct']]['배점'].sum()
    total_score = data['배점'].sum()
    accuracy = data['Correct'].mean() * 100  # Percentage accuracy

    return data, accuracy, score, total_score


def play():
    data, accuracy, score, total_score = calculate_accuracy_and_score("./2024_questions.csv")
    print(data[['이름', '정답', '답변', 'Correct']])
    print("---------------------")
    print("정답율:", accuracy)
    print("점수:", score)
    print("총점수:", total_score)