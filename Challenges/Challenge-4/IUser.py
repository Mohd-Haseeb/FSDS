from abc import ABC,abstractmethod


class IUser:
    @abstractmethod
    def purchaseCourse(id:int):
        pass
