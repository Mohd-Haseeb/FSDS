from ineuron import Ineuron
from course import Course

class Courses(Ineuron): # Inheritance
    def __init__(self) -> None:
        super().__init__()
        self._coursesList = []
    
    def addCourse(self,myCourse:str):
        self._coursesList.append(myCourse)
    
    def allCourses(self):
        return self._coursesList




allCourses = Courses()
allCourses.welcome()