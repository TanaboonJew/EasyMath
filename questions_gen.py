import random


def generate_random_number():
    return random.randint(1, 20)


def generate_random_operator():
    return random.choice(['+', '-'])


def generate_addition_question(num):
    operand1 = generate_random_number()
    operand2 = generate_random_number()
    return f"{num:02d}. {operand1} + {operand2} ="


def generate_subtraction_question(num):
    operand1 = generate_random_number()
    operand2 = generate_random_number()
    return f"{num:02d}. {operand1} - {operand2} ="


def generate_multiplication_question(num):
    operand1 = random.randint(0, 12)
    operand2 = random.randint(0, 12)
    return f"{num:02d}. {operand1} x {operand2} ="


def generate_division_question(num):
    divisor = random.randint(3, 12)
    dividend = divisor * random.randint(1, 12)
    return f"{num:02d}. {dividend} ÷ {divisor} ="


def generate_questions(times):
    all_ques = []
    num = 1
    
    for time in range(times):
        questions = []
        for _ in range(4):
            for _ in range(5):
                operator = generate_random_operator()
                if operator == '+':
                    questions.append(generate_addition_question(num))
                else:
                    questions.append(generate_subtraction_question(num))
                num += 1

            for _ in range(10):
                equation_parts = []
                for _ in range(3):
                    equation_parts.append(str(generate_random_number()))
                    equation_parts.append(generate_random_operator())
                equation_parts.pop()  # Remove the last operator
                equation = ' '.join(equation_parts)
                questions.append(f"{num:02d}. {equation} =")
                num += 1

            for _ in range(6):
                questions.append(generate_multiplication_question(num))
                num += 1

            for _ in range(4):
                questions.append(generate_division_question(num))
                num += 1
        all_ques.append(questions)
        
    return all_ques