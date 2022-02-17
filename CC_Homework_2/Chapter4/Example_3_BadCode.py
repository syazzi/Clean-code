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
        self.get_email(email, endingAddress, emailEndingAddress, position)
        
    #the codes below will compare the input email to check whether its a teachers email or students email.
    def get_email(self, email, endingAddress, emailEndingAddress, position):
        if emailEndingAddress != endingAddress:
            print("Unknown")
        elif email[position - 4: position].isnumeric():
            print("Directed to student portal")
        else:
            print("Directed to Teachers portal")
   

if __name__ == "__main__":
    main()