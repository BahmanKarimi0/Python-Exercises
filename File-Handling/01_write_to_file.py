# Program to take user input and append it to txt file
text = input("Enter a string: ")
with open("my_text.tx", "a", encoding="utf-8") as f:
    f.write(text + "\n")
    print("Text saved successfully")