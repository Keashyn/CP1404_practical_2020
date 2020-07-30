"""
CP1404 Practical 2
Do all of the following in a single file called files.py:
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that
name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt” (You can create a simple text file in PyCharm with Ctrl+N, choose
“File” and save it in your project). Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the
result, which should be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers.
"""
def main():
    #Number 1 is asking for the user name and write it to a file.
    out_file = open("name.txt", 'w')
    user_name = input("what is your name:")
    print('{}'.format(user_name),file=out_file)

    out_file.close()

    #Number 2 is asking the program to read the user name and output it in a string.
    out_file=open("Name.txt",'r')
    for line in out_file:
        print('{}'.format(user_name))

    #Number 3 is asking the program to create a number file and write two numbers in it on seperate line ,read those number and then add it together to get 59.
    number_file=open("Numbers.txt",'w')

    number_file.write("17\n")
    number_file.write("42\n")
    number_file.write("400\n")

    number_file.close()
    # Number 4 is asking the program to read the number text file that has numbers in it and add it altogether to get the total number.
    number_file = open("Numbers.txt", "r")
    number1 = int(number_file.readline())
    number2 = int(number_file.readline())
    number_file.close()
    print(number1 + number2 )

    number_file= open("Numbers.txt",'r')
    total=0
    for line in number_file:
        number= int(line)
        total += number
    number_file.close()
    print(total)
main()

