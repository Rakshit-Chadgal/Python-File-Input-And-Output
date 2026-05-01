#Q1: Create a new file “practice.txt” using python. Add some data in it:
'''with open("practice.txt", "w") as file:
    file.write("Hi everyone,\nWe are learning File I/O\nusing Java.\nI love programming in Java.")'''

#Q2: Write a function that replace all occurrences of “java” with “python” in above file.
'''f = "practice.txt"
def replace(f):
    with open(f, "r") as file:
        data = file.read()
    data = data.replace("Java", "Python")
    with open(f, "w") as file:
        file.write(data)
replace(f)'''

#Q3: Search if any word exists in the file or not.
file = "practice.txt"
def search(file, word):
    with open(file, "r") as file:
        data = file.read()
    if word in data:
        print(f"The word '{word}' exists in the file.")
    else:
        print(f"The word '{word}' does not exist in the file.")
n = input("Enter a word to search in the file: ")
search(file, n)