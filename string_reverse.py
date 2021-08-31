# Project :- String Reverse

class StringReverse:

    def __init__(self, string):
        self.sentence = string

    def convertToReverse(self):
        splited_sentence = self.sentence.split(" ")

        reversed_word = [word[::-1] for word in splited_sentence]

        return " ".join(reversed_word)


sentence = str(input("Write a sentence: "))

print(StringReverse(sentence).convertToReverse())


# ----------------------------------------------------------------



# Reference Code For Practice

# sentence = "Hello Bipin How are you"
#
# list_str = sentence.split(" ")
# empty = []
# for word in list_str:
#     temp = word[::-1]
#     empty.append(temp)
#
# print(" ".join(empty))
#

