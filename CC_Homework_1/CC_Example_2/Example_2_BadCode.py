password = input("please input password: ")
login = ""
page = ""


if password == "1234":
    login = "success"
    if login == "success":
        page = input("Please input home: ")
        if page == "home":
            print("Ur in homepage")
        else:
            print("ur not in the homepage please refreshed")
    else:
        login = "unsuccesfull"
else:
    print()
