statement = input("Enter your intoduction:")
print (statement)
charactercount = 0
wordcount = 1
for i in statement:
    charactercount = charactercount+1
    if(i==" "):
        wordcount=wordcount+1
print(charactercount)
print(wordcount)
