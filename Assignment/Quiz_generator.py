

import random
questions = [
    {
        "question": "What is the output of: print(type(()))?",
        "options": {
            "a": "<class 'tuple'>",
            "b": "<class 'list'>",
            "c": "<class 'dict'>",
            "d": "<class 'set'>"
        },
        "answer": "a"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "function", "b": "def", "c": "fun", "d": "define"},
        "answer": "b"
    },
    {
        "question": "What is the output of: 3 * '5'?",
        "options": {"a": "15", "b": "555", "c": "Error", "d": "None"},
        "answer": "b"
    },
    {
        "question": "Which data type is immutable?",
        "options": {"a": "list", "b": "dict", "c": "set", "d": "tuple"},
        "answer": "d"
    },
    {
        "question": "How do you start a comment in Python?",
        "options": {"a": "//", "b": "<!--", "c": "#", "d": "**"},
        "answer": "c"
    },
    {
        "question": "What does len() function do?",
        "options": {"a": "Calculates size of int", "b": "Returns length", "c": "Finds memory usage", "d": "Loops items"},
        "answer": "b"
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": {"a": ".pt", "b": ".python", "c": ".py", "d": ".pyt"},
        "answer": "c"
    },
    {
        "question": "Which keyword is used to import a module?",
        "options": {"a": "include", "b": "import", "c": "using", "d": "require"},
        "answer": "b"
    },
    {
        "question": "What is the output of bool(0)?",
        "options": {"a": "True", "b": "False", "c": "0", "d": "None"},
        "answer": "b"
    },
    {
        "question": "What defines a block of code in Python?",
        "options": {"a": "Brackets {}", "b": "Parentheses ()", "c": "Indentation", "d": "Curly braces"},
        "answer": "c"
    },
    {
        "question": "Which method is used to add an item to a list?",
        "options": {"a": "add()", "b": "insert()", "c": "append()", "d": "push()"},
        "answer": "c"
    },
    {
        "question": "What does the 'pass' statement do?",
        "options": {"a": "Exits loop", "b": "Does nothing", "c": "Skips iteration", "d": "Returns a value"},
        "answer": "b"
    },
    {
        "question": "Which operator checks equality?",
        "options": {"a": "=", "b": "==", "c": "!=", "d": "==="},
        "answer": "b"
    },
    {
        "question": "Which function converts a string to an integer?",
        "options": {"a": "str()", "b": "float()", "c": "int()", "d": "chr()"},
        "answer": "c"
    },
    {
        "question": "What is the output of: len([1,2,3])?",
        "options": {"a": "3", "b": "2", "c": "1", "d": "Error"},
        "answer": "a"
    },
    {
        "question": "Which keyword creates a loop?",
        "options": {"a": "repeat", "b": "loop", "c": "for", "d": "iterate"},
        "answer": "c"
    },
    {
        "question": "Which symbol is used for exponent in Python?",
        "options": {"a": "^", "b": "**", "c": "exp()", "d": "%"},
        "answer": "b"
    },
    {
        "question": "What is the output of: type({})?",
        "options": {"a": "<class 'set'>", "b": "<class 'tuple'>", "c": "<class 'dict'>", "d": "<class 'list'>"},
        "answer": "c"
    },
    {
        "question": "How do you create a set in Python?",
        "options": {"a": "[]", "b": "()", "c": "{}", "d": "set()"},
        "answer": "d"
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {"a": "exception", "b": "try", "c": "throw", "d": "error"},
        "answer": "b"
    }
]

random.shuffle(questions)
def run_quiz():
    print("Welcome to the Python Quiz Game!")
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")
        for opt, value in q["options"].items():
            print(f"{opt}) {value}")

        user = input("Your answer (a/b/c/d): ").lower()

        if user == q["answer"]:
            print("✅Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{q['answer']}'")

    print("\nYour Final Score:", score, "/ 20")

    if score == 20:
        print("Outstanding! Python Master!")
    elif score >= 15:
        print("Great job! Keep practicing!")
    elif score >= 10:
        print("Good effort! Improve further!")
    else:
        print("Keep learning! You'll get better!")
run_quiz()

##Output:
##Welcome to the Python Quiz Game!
##
##Question 1: What is the output of: print(type(()))?
##a) <class 'tuple'>
##b) <class 'list'>
##c) <class 'dict'>
##d) <class 'set'>
##Your answer (a/b/c/d): c
##Wrong! The correct answer is 'a'
##
##Question 2: What does len() function do?
##a) Calculates size of int
##b) Returns length
##c) Finds memory usage
##d) Loops items
##Your answer (a/b/c/d): b
##✅Correct!
##
##Question 3: What does the 'pass' statement do?
##a) Exits loop
##b) Does nothing
##c) Skips iteration
##d) Returns a value
##Your answer (a/b/c/d): b
##✅Correct!
##
##Question 4: Which data type is immutable?
##a) list
##b) dict
##c) set
##d) tuple
##Your answer (a/b/c/d): b
##Wrong! The correct answer is 'd'
##
##Question 5: What is the correct file extension for Python files?
##a) .pt
##b) .python
##c) .py
##d) .pyt
##Your answer (a/b/c/d): b
##Wrong! The correct answer is 'c'
##
##Question 6: Which keyword is used to handle exceptions?
##a) exception
##b) try
##c) throw
##bd) error
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'b'
##
##Question 7: Which keyword creates a loop?
##a) repeat
##b) loop
##c) for
##bd) iterate
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'c'
##
##Question 8: How do you start a comment in Python?
##a) //
##bb) <!--
##c) #
##d) **
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'c'
##
##Question 9: Which symbol is used for exponent in Python?
##a) ^
##b) **b
##c) exp()
##d) %
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'b'
##
##Question 10: What defines a block of code in Python?
##a) Brackets {}
##b) Parentheses ()
##bc) Indentation
##d) Curly braces
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'c'
##
##Question 11: What is the output of: type({})?
##a) <class 'set'>
##bb) <class 'tuple'>
##c) <class 'dict'>
##d) <class 'list'>
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'c'
##
##Question 12: Which keyword is used to import a module?
##a) include
##bb) import
##c) using
##d) require
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'b'
##
##Question 13: What is the output of: len([1,2,3])?
##ba) 3
##b) 2
##c) 1
##d) Error
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'a'
##
##Question 14: Which operator checks equality?
##ba) =
##b) ==
##c) !=
##d) ===
##Your answer (a/b/c/d): 
##Wrong! The correct answer is 'b'
##
##Question 15: Which keyword is used to define a function in Python?
##a) function
##b) def
##c) fun
##d) define
##Your answer (a/b/c/d): b
##✅Correct!
##
##Question 16: Which method is used to add an item to a list?
##a) add()
##b) insert()
##c) append()
##d) push()
##Your answer (a/b/c/d): b
##Wrong! The correct answer is 'c'
##
##Question 17: What is the output of: 3 * '5'?
##a) 15
##b) 555
##c) Error
##d) None
##Your answer (a/b/c/d): b
##✅Correct!
##
##Question 18: What is the output of bool(0)?
##a) True
##b) False
##c) 0
##d) None
##Your answer (a/b/c/d): b
##✅Correct!
##
##Question 19: Which function converts a string to an integer?
##a) str()
##b) float()
##c) int()
##d) chr()
##Your answer (a/b/c/d): b
##Wrong! The correct answer is 'c'
##
##Question 20: How do you create a set in Python?
##a) []
##b) ()
##c) {}
##d) set()
##bYour answer (a/b/c/d): 
##Wrong! The correct answer is 'd'
##
##Your Final Score: 5 / 20
##Keep learning! You'll get better!
