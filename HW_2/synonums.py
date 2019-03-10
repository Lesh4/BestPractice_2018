def add():    
    if oper[1] not in syn.keys():
        syn[oper[1]] = set()
    if oper[2] not in syn.keys():
        syn[oper[2]] = set()
    syn[oper[1]].add(oper[2])
    syn[oper[2]].add(oper[1])
    words.append(oper[1])
    words.append(oper[2])
def count():
    print(words.count(oper[1]))
def check(word1,word2):
    if word1 not in syn.keys() or word2 not in syn.keys():
        print("NO") 
    if word1 in syn[word2]:
        print("YES") 
    else:
        print("NO") 
syn = {}
words = []
opers = []
n = int(input())
i = 0
while i < n:
    oper = input().lower().split()
    opers.append(oper)
    i+=1
for oper in opers:     
    if oper[0] == "add":
        add()
    elif oper[0] == "count":
        count()
    elif oper[0] == "check":
        check(oper[1],oper[2])
    else:
        print("Error")
