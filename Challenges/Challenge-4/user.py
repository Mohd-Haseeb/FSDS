from courses import Courses

class User(Courses): # Multi level Inheritance (Ineuron -> Courses -> User)
    __id = 1
    __allUsers = {}
    def __init__(self,name,email,phone) -> None:
        super().__init__()
        self.__userId = User.__id
        self.__name = name
        self.__email = email
        self.__phone = phone
        User.__allUsers[self.__userId] = self.__email
        User.__id += 1
    

    
    def sendMail(self):
        for c in self._coursesList:
            print(f"""
                To : {self.__email}

                Hi {self.__name}, 

                User ID : {self.__userId}

                Your class for {c.getCourseName()} is on {c.getCourseTime()}
            """)
    @staticmethod
    def getAllUsers():
        return User.__allUsers

    
    def welcome(self):
        print(f"Hey {self.__name}, Welcome to Ineuron")

    def userDetails(self):
        coursesEnrolled = [c.getCourseName() for c in self._coursesList]
        print(f"""
            User Name : {self.__name}
            Email : {self.__email}
            Phone : {self.__phone}

            Courses Enrolled :
                -> {coursesEnrolled}

        """)

