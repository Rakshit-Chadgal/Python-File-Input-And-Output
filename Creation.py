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
'''file = "practice.txt"
def search(file, word):
    with open(file, "r") as file:
        data = file.read()
    if word in data:
        print(f"The word '{word}' exists in the file.")
    else:
        print(f"The word '{word}' does not exist in the file.")
n = input("Enter a word to search in the file: ")
search(file, n)'''

#Q4: WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
'''def find():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(f"The word '{word}' occurs first in line number {line_no}.")
                return
            line_no += 1
    return -1
print(find())'''

#Q5: From a file containing numbers separated by comma, print the count of even numbers.
'''count = 0
with open("numbers.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10,45,56,78,90,100")
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1
print(f"The count of even numbers in the file is: {count}")'''