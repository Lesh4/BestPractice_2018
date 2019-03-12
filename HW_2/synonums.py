""" This program performs some operations with synonums. """
def add():
    """ Adds words to the dictionary """
    if OPER[1] not in SYN.keys():
        SYN[OPER[1]] = set()
    if OPER[2] not in SYN.keys():
        SYN[OPER[2]] = set()
    SYN[OPER[1]].add(OPER[2])
    SYN[OPER[2]].add(OPER[1])
    if OPER[1] not in WORDS or OPER[2] not in WORDS:
        WORDS.append(OPER[1])
        WORDS.append(OPER[2])

def count():
    """ Counts the number of repetitions of a word in the list """
    print(WORDS.count(OPER[1]))

def check(word1, word2):
    """ Check the words for synonums """
    if word1 not in SYN.keys() or word2 not in SYN.keys():
        print("NO")
    elif word1 in SYN[word2]:
        print("YES")
    else:
        print("NO")
SYN = {}
WORDS = []
OPERS = []
N = int(input())
i = 0
while i < N:
    OPER = input().lower().split()
    OPERS.append(OPER)
    i += 1
for OPER in OPERS:
    if OPER[0] == "add":
        add()
    elif OPER[0] == "count":
        count()
    elif OPER[0] == "check":
        check(OPER[1], OPER[2])
    else:
        print("Error")
