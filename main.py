import re

greet = input("Welcome to guvi !!! You want 'Login' or 'Register' : ").lower()
file = {}
def emailverifier(email) :
    if re.search(r"^[a-zA-Z]\w+@(\w+\.)?\w+\.(co|com|org|in|us|net)$", email, re.IGNORECASE):
        e = email.index("@")
        t = (email[0:e])
        d = email.index(".")
        f = (email[e+1:d])
        if len(t) >= 4 and len(f) >= 3:
            return email
            pass #file["Email Id"]=email # open one file and store this mail id
        else:
            print("⚠️ Enter a Valid email id ")
    else:
        print("⚠️  Enter a Valid email id ")

def passwordverifier(password):
        x = True
        while x:
            if (len(password) < 5 or len(password) > 16):
                break
            elif not re.search("[a-z]", password):
                break
            elif not re.search("[A-Z]", password):
                break
            elif not re.search("[0-9]", password):
                break
            elif not re.search("\W", password):
                break
            else:
                file[email] =password
                x = False
                return password

        if x:
            print("Enter a strong password. Must have minimum one special character, one digit,one uppercase, one lowercase character. eg: Healthy@1 ")
if greet == "register":
    username = input("Enter your username : ").strip()
    email = input("Enter your email id: ").strip()
    emailverifier(email)
    if email == emailverifier(email) :
        password = input("Enter your password: ").strip()
        if password == passwordverifier(password):
            passwordverifier(password)
            security = input("Security question incase you forgot password. Enter your childhood friend name?: ")
            file[email]=password
            IDS_FILE = open("IDS_FILE.txt", "a")
            for email, password in file.items():
                IDS_FILE.write('%s:%s\n' % (email, password))
                IDS_FILE.close()
            print(f"welcome  {(email[0:5])} you`ve registered successfully ")

elif greet == "login":
    email = (input("Enter email id: "))
    with open(r'C:\Users\User\PycharmProjects\Assignment Task - 1\IDS_FILE.txt') as f:
        d = {mail: pas for line in f for (mail, pas) in [line.strip().split(":")]}
    if email in d:
        password = input("Enter your password: ")
        if d[email] == password:
            print(f"welcome  {(email[0:5])} you`ve logged in successfully")
        else:
            print("⚠ Wrong password ")
            forgot = input("if you want retrieve your password enter 'retrieve' or to reset your password enter 'reset' ")
            if forgot == "retrieve":
                email = input("Enter email id: ")
                if email in d :
                    print(f"your password is {d[email]}")
                else:
                    print("your email id  not registered ")
            elif forgot == "reset":
                email = input("Enter your email id: ")
                if email in d :
                    password = input("Enter your new password: ").strip()
                    file[email] = passwordverifier(password)
                    print("password reset successfully ")
                else:
                    print("your email id  not registered ")
            else:
                print("your email id  not registered ")
    else:
        print("You`re not registered yet. Please register yourself")
else:
    print("⚠ Please select valid option!!!")






