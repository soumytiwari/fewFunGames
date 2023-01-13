#to concatenate, we use following ways---
# print("sentence a " + sentence_b)
# print("sentence a {}".format(sentence_b))
# print(f"sentence a {sentence_b}")
def madlib():

    adj=input("Adjective: ")
    verb1=input("Verb: ")
    verb2=input("Verb: ")
    famous_person=input("Famous person: ")

    print("\n-------------------------------Code-------------------------------\n")

    madlib=f"Computer programming is so {adj}! I Love it so much. It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

    print(madlib)