answer = input("Welke file moet gecontroleerd worden?\n")
path = answer.split(" ")
with open(answer) as fh:
    is_spam = False
    for line in fh.readlines():
        for word in line.split(" "):
            if word == "lottery" or word == "inheritance" or word == "viagra":
                is_spam = True
if is_spam:
    print("Dit is spam.")
else:
    print("Dit is geen spam.")
