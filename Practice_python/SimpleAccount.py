class acc():
    def __init__(self,username,password,recovCode):
        self.username=username
        self.__password=password
        self.__recovCode=recovCode
    def showAccData(self):
        print('username:',self.username)
        print('password:',self.__password)
        print('recoverycode:',self.__recovCode)
    def login(self):
        switch1= True
        while switch1:
            password=input('Enter your password')
            if password.lower()=="end":
                print('Login cancel')
                switch1=False
                continue
            if password==self.__password:
                print('Correct password, login successful')
                switch1=False
                continue
            else:
                print('Wrong password, enter again or enter "END" to cancel login.')
    def changePassword(self):
        switch2=True
        while switch2:
            recovCode=input('Enter recovery code to change password or enter "END" to cancel password change.')
            if recovCode.lower()=="end":
                print('Password change cancel')
                switch2=False
                continue
            if recovCode==self.__recovCode:
                switch3=True
                while switch3:
                    new_1=input('Recovery code correct, enter a new password')
                    new_2=input('Please enter new password again')
                    if new_1==new_2:
                        self.__password=new_1
                        print('Password change successful')
                        self.showAccData()
                        switch3=False
                        switch2=False
                        continue
                    else:
                        print('Passwords do not match')
            else:
                print('Wrong recovery code, password change failed')
acc1=acc('user1','abcd1234','123456')
acc1.showAccData()
print('-----------------------------')
acc1.login()
print('-----------------------------')
acc1.changePassword()
print('-----------------------------')
# acc1.showAccData()