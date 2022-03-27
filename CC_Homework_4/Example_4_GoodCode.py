from logging import raiseExceptions


def main():
    __password = input("Please type in ur password: ")
    page = input("Please enter 'home' to be directed to homepage: ")
    browser = WebBrowserDirectory(__password, page)
    print(browser.__get_password(__password))
    print(__password)
class WebBrowserDirectory:
    def __init__(self, password, page):
        self.__password = password
        self.page = page
        self.get_browser(password, page)
        
    
    def get_browser(self, password, page):
        if self.__get_password(password) and self.get_page(page):
            print("Ur in homepage.")
        else:
            print("Webpage is unable to connect.")
        
    def __get_password(self, password):
        if password == "1234":
            return True
        
    def get_page(self, page):
        if page == "home":
            return True
        



if __name__ == "__main__":
    main()