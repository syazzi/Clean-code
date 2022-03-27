def main():
    password = input("Please type in ur password: ")
    page = input("Please enter 'home' to be directed to homepage: ")
    browser = WebBrowserDirectory(password, page)
    print(browser.get_password(password))
    print(password)

class WebBrowserDirectory:
    def __init__(self, password, page):
        self.password = password
        self.page = page
        self.get_browser(password, page)
        
    
    def get_browser(self, password, page):
        if self.get_password(password) and self.get_page(page):
            print("Ur in homepage.")
        else:
            print("Webpage is unable to connect.")
        
    def get_password(self, password):
        if password == "1234":
            return True
        else:
            return
    def get_page(self, page):
        if page == "home":
            return True
        else:
            return



if __name__ == "__main__":
    main()