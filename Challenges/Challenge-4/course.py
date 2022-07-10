class Course:
    def __init__(self,courseName,instructor,startDate,fees) -> None:
        self.__courseName = courseName
        self.__instructor = instructor
        self.__startDate = startDate
        self.__fees = fees
        self.__time = "3:00 PM to 6:00 PM"
    
    def getCourseDetails(self):
        print(f"""
            Course : {self.__courseName}
            Instructor : {self.__instructor}
            Starts From : {self.__startDate}
            Timings : {self.__time}
            Fees : {self.__fees}
        """)
    
    def getCourseName(self):
        return self.__courseName
    
    def getCourseTime(self):
        return self.__time
    
