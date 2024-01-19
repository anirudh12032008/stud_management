import json


class Students:
    __admin = 'ani'
    with open('stud.json') as fs:
        data = list(json.loads(fs.read()))
        
    def __init__(self,name,username,password,age,skills):
        self.name = name    
        self.username = username    
        self.password = password 
        self.age = age   
        self.skills = skills
        self.data.append(self.__dict__)
        self.db()
        self.info()
    @classmethod
    def db(cls):
        with open('stud.json', 'w') as fs:
            fs.write(json.dumps(cls.data, indent=4))
            
    def info(self):
        print('User Details: ')
        print(f'\t Name: {self.name}')
        print(f'\t Username: {self.username}')
        print(f'\t Age: {self.age}')
        print(f'\t Skills: {self.skills}')
        
    @classmethod
    def login(cls, username, password):
        for student in cls.data:
            if student['username'] == username and student['password']==password:
                print('User Details: ')
                print(f"\t Name: {student['name']}")
                print(f"\t Username: {student['username']}")
                print(f"\t Age: {student['age']}")
                print(f"\t Skills: {student['skills']}")
                return True
        else:
            print('Invalid Credetials')
            return False
    @classmethod
    def update(cls, username, password):
        for student in cls.data:
            if student['username'] == username and student['password']==password:
                student['name']=input("Name:  ")
                student['password']=input("Password: ")
                student['age']=input("Age: ")
                student['skills']=input("Skills: ")
                cls.db()
                return True
        else:
            print('Invalid Credetials')
            return False
    
    @classmethod
    def delete(cls, username, password):
        for student in cls.data:
            if student['username'] == username and student['password']==password:
                print(cls.data.pop(cls.data.index(student)))
                cls.db()
                return True
        else:
            print('Invalid Credetials')
            return False
    
    @classmethod
    def admin(cls, password):
        if password == cls.__admin:
            while True:
                print('0.Exit \t 1.Show Data \t 9.Home Menu')
                x = int(input('Number: '))
                
                if x == 0:
                    exit(0)
                elif x == 1:
                    for i in cls.data:
                        print(i)
                elif x == 9:
                    return True
        else:
            print('Invalid Credentials')
            return False
while(True):
    print('0.Exit \t 1.Register \t 2.Login \t 3.Admin \t 4.Update \t 5.Delete')
    n = int(input('Number: '))
    if n == 0:
        exit(0)
    elif n == 1:
        student = Students(name=input('Name: '),username=input('Username: '),password=input('Password: ') ,age=input('Age: '),skills=input('Skills(seperated by \',\'): ').split(','))
    elif n == 2:
        logged = Students.login(username=input('Username: '),password=input('Password: '))
        if logged==False:
            logged = Students.login(username=input('Username: '),password=input('Password: '))
    elif n == 3:
        admin = Students.admin(password=input('Enter Admin Password: ')) 
        if admin == False:
            admin = Students.admin(password=input('Enter Admin Password: '))
         
            
    elif n == 4:
        logged = Students.update(username=input('Username: '),password=input('Password: '))
        if logged==False:
            logged = Students.update(username=input('Username: '),password=input('Password: '))
    elif n == 5:
        logged = Students.delete(username=input('Username: '),password=input('Password: '))
        if logged==False:
            logged = Students.delete(username=input('Username: '),password=input('Password: '))