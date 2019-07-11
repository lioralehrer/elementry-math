import random


no_answers = ["no", "NO", "n", "N", "No"]
yes_answers = ["yes", "YES", "Yes", "Y", "y"]
wrong_answers = []
correct_answers = []


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
            else:
                ans = input(
                    "Do you want the next exercise ? insert yes or no  ")
    else:
        correct = eval(exercise)
        wrong_answers.append(exercise+"="+answer+" ("+str(correct)+")")
        ans = input(f"Uncorrect :( the answer is: {correct} \n Next exercise ?")
        while ans != None:
                if ans in no_answers:
                    ans = None
                    return results()
                if ans in yes_answers:
                    ans = None
                    return play()
                else:
                    ans = input( "Do you want the next exercise ? insert yes or no  ")

def build_new_ex():
    operators = ["+", "-", "*"]
    return (str(random.randint(1, 20)) + random.choice(operators) + str(random.randint(1, 11)))


def results():
    precent_correct = len(correct_answers) / (len(correct_answers)+len(wrong_answers))*100
    if wrong_answers[0] != None:
        print(f"“A list of problems answered wrong: ")
        for i in wrong_answers:
            print (i)
    if correct_answers[0] != None:
        print("Your correct answeres : ")
        for i in correct_answers:
            print (i)
    print(
        f"You have answered correctly {len(correct_answers)} out of {len(correct_answers)+len(wrong_answers)} problems ({precent_correct}%)")
    print("THE END")


start_play()
