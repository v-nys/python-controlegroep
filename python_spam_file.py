import python_spam_regel_functie

def file_is_spam():
    answer = input("Welke file moet gecontroleerd worden?\n")
    with open(answer) as fh:
        is_spam = False
        for line in fh.readlines():
            is_spam = is_spam or python_spam_regel_functie.line_is_spam(line.strip())
    if is_spam:
        print("Deze file bevat spam!")
    else:
        print("Deze file is in orde!")
