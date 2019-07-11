import random


no_answers = ["no", "NO", "n", "N", "No"]
yes_answers = ["yes", "YES", "Yes", "Y", "y"]
wrong_exercises = []
correct_answers = []


# def build_exercises_list():
#     operators = ["+", "-", "*", "/"]
#     exercise_list = []
#     for i in range(11):
#         exercise_list.append(str(random.randint(1, 20)) +
#                              random.choice(operators) + str(random.randint(1, 11)))
#     return exercise_list


def start_play():
    ans = input(
        "Hey freind, Ready to start exercise on your math elementry skill ?  (write yes or no, please) ")
    if ans in no_answers:
        print("Well.... try some other time :)")
    if ans in yes_answers:
        play()


def play():
    exercise = build_new_ex()
    answer = input(exercise+"= ")
    print (exercise+answer)
    if eval(exercise) == eval(answer):
        correct_answers.append(exercise + "="+answer)
        ans = input("Correct!  Next exercise ?")
        while ans != None:
            if ans in no_answers:
                ans = None
                return results()
            if ans in yes_answers:
                ans = None
                return play()
            else: ans = input("Do you want the next exercise ? insert yes or no  ")
    else: print("Uncorrect!")            

def build_new_ex():
    operators = ["+", "-", "*"]
    return (str(random.randint(1, 20)) + random.choice(operators) + str(random.randint(1, 11)))


def results():
    # give the results of the play
    print (correct_answers)
    print("THE END")

start_play()
