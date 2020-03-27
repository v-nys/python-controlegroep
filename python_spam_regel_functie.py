def check_spam_line(line):
    words = line.split(" ")
    is_spam = False
    for word in words:
        if word == "lottery" or word == "inheritance" or word == "viagra":
            is_spam = True
    if is_spam:
        print("Dit is spam.")
    else:
        print("Dit is geen spam.")
