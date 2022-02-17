from turtle import position

from sqlalchemy import false, null, true


def main():
    email = input("Input ur email add: ")
    position = null
    endingAddress = "@syazzi.bn"
    for i in range(len(email)):
        if email[i] == '@':
            position = i
    emailEndingAddress = email[position:len(email)]
    directedTo = Directory(email, endingAddress, emailEndingAddress, position) 

class Directory:
    def __init__(self, email, endingAddress, emailEndingAddress, position):
        self.email = email
        self.endingAddress = endingAddress      
        self.emailEndingAddress = emailEndingAddress  
        self.position = position
        self.isTeachers_or_isStudent(email, endingAddress, emailEndingAddress, position)

    # 4 characters before the sign "@" will decide its a teacher access or student access.    
    def isTeachers_or_isStudent(self, email, endingAddress, emailEndingAddress, position):
        if emailEndingAddress != endingAddress:
            print("Unknown")
        elif email[position - 4: position].isnumeric():
            print("Directed to student portal")
        else:
            print("Directed to Teachers portal")
   

if __name__ == "__main__":
    main()