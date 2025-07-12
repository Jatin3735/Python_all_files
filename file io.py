def check_for_line():
    word = input("Enter the word that you want to see : ")
    line_no = 1
    with open("practice.txt","r") as f:
        for line in f:
            if word in line:
                return f"Found At \nLine number : {line_no}"
            line_no+= 1
    return "Not found. Please find on another file\nThankYou! "
result = check_for_line()
print(result)



