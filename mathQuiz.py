import datetime
from threading import Timer
import random as rd
import time

def askQuestions(questions_list: list, qNum: int, mistakes: int) -> bool:
    print(questions_list[qNum][0])
    answer = int(input("Answer : "))
    if answer == questions_list[qNum][1]:
        if qNum == len(questions_list) - 1:
            print("Good job! You have finished every questions")
        else:
            print("Correct! Moving up to the next question")

        return True
    else:
        if qNum == len(questions_list) - 1:
            if mistakes == 1:
                print("Not bad! you AVERAGE")
            elif mistakes == 2 or mistakes == 3:
                print(f"You are so dumb how you have {mistakes} mistakes")
            elif mistakes == 4:
                print("You are a FAILURE you get everything wrong")
            else:
                print("Wrong answer")
        return False


def main():
    questions_list, q_num, mistakes = [
        ("What is 8 + 7?", 15),
        ("What is 2 x 14?", 28),
        ("What is the square root of 49", 7),
        ("What is x in 2x + 3 = 5?", 1)
    ], 0, 0

    rd.shuffle(questions_list)

    def my_function() -> None:
        print("Times up you slow!")
        exit()

    question_timer = Timer(15, my_function)
    question_timer.start()
    while q_num < len(questions_list):
        correct = askQuestions(questions_list, q_num, mistakes)
        if not correct:
            mistakes += 1
            print(f"You have made {mistakes} mistakes")

        q_num += 1

    question_timer.cancel()


if __name__ == '__main__':
    main()
