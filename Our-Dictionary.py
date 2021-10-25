dict1 = {
    "Programming" : "Programming is a way to communicate with computer",
    "Code" : "Basically it is a language to communicate with computer",
    "Python" : "It is a type of language",
    "IDE" : "Tool where we can write the code",
    "Machine Learning" : "Intelligent way to train the computer",
    "Artificial Intelligence" : "Make computer to behave like human brain"
}

input1 = input("Enter the word : ")

for key, item in dict1.items():
    if input1 == key:
        print(dict1[key])
        break
else:
    print("Sorry, We cannot find the meaning of word....")