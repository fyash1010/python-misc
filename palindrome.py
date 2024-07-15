userInput = str(input("Enter a word: "))
userInputList = []

for x in userInput:
    userInputList.append(x)

userInputListLength = len(userInputList)

for y in range(0, userInputListLength):
    if(userInputList[y] != userInputList[userInputListLength - 1 - y]):
        print("False")
        break