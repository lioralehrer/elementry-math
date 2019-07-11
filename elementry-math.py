import random

def build_exercises_list():
    operators = ["+", "-", "*", "/"]
    exercise_list=[]
    for i in range(11):
      exercise_list.append(str(random.randint(1, 20)) + random.choice(operators) + str(random.randint(1, 11)))
    return exercise_list        
print (build_exercises_list())


