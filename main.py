import json
from difflib import get_close_matches
from typing import Union


def load_knowledge(file_path: str)->dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data
def save_knowledge(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, question: list[str])-> Union[str, None]:
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge: dict)->Union[str, None]:
    for q in knowledge["question"]:
        if q["question"] == question:
            return q["answer"]

def chat_bot():
    knowledge: dict = load_knowledge('knowledge.json')
    while True:
        user_input: str =input('You:')
        if user_input.lower()=='quit':
            break

        best_match: Union[str, None]= find_best_match(user_input, [q["question"] for q in knowledge["question"]])
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge)
            print(f'Bot: {answer}')
        else:
            print('Bot: I dont know the answer, can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge["question"].append({"question": user_input, "answer": new_answer})
                save_knowledge('knowledge.json', knowledge)
                print('Bot: Thank you I learned a new response!')

if __name__ == '__main__':
    chat_bot()