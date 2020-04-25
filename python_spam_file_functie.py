import python_spam_regel_functie

def file_is_spam(answer):
    with open(answer) as fh:
        is_spam = False
        for line in fh.readlines():
            is_spam = is_spam or python_spam_regel_functie.line_is_spam(line.strip())
    return is_spam
