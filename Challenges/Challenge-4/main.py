from user import User
from course import Course



newCourse = Course("FSDS","Sudhanshu Sir","07-05-2022",17000)
# newCourse.getCourseDetails()
newCourse2 = Course("Full Stack JS Dev.","Hitesh Sir","10-07-2022",1699)

user1 = User("Haseeb","haseeb@gmail.com","9876543210")
user1.addCourse(newCourse)
user1.addCourse(newCourse2)

userCorses = user1.allCourses()
print(userCorses)

for c in userCorses:
    c.getCourseDetails()


systemDesing = Course("System Design","Anjali Sheel","25-06-2022","3500")

user2 = User("Shabrez",'someone@yahoo.com','1234567890')
user2.addCourse(systemDesing)

for c in user2.allCourses():
    c.getCourseDetails()


user1.sendMail()
user2.sendMail()

allUsers = User.getAllUsers()
print(allUsers)

user1.welcome()
user2.welcome()

user1.userDetails()
