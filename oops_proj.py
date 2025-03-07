class chitchat:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        #self.menu()
    
    def menu(self):
        user_input=input("""welcome to chitchat!! how would you like to proceed?
                         1. Press 1 to signup
                         2. Press 2 to singin
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any other key to exit
                          -> """)
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email=input("enter you email: ")
        password=input("setup your password: ")
        self.username=email
        self.password=password 
        print("you have signed up successfully")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            username1=input("enter your email/username: ")
            password1=input("enter your password: ")
            if self.username==username1 and self.password==password1:
                print("you have signed in succesfully")
                self.loggedin=True
            else:
                print("please input correct credentials")

        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt=input("enter your message: ")
            print(f"following content has been posted ",txt)
        else:
            print("you need to signin first to post something")

        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin==True:
            txt=input("enter your message: ")
            frnd=input("whom to send msg? ") 
            print(f"your msg has been sent to ", frnd)
        else:
            print("you need to signin first to post something")

        print("\n")
        self.menu()


#obj = chitchat()
