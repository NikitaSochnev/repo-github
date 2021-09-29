
class MainClass:
    __class_number = 20
    def getClassNumber(self):
        return MainClass().__class_number
class TestMainClass:
    def testgetClassNumber(self):
        assert MainClass().getClassNumber() >45,'Число должно быть больше 45'