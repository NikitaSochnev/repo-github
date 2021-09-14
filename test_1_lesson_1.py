import pytest
class MainClass:
    def getLocalNumber(self):
       return 14

class TestMainClass:
    def testGetLocalNumber(self):
        assert (MainClass().getLocalNumber()) == 14, 'Не равняется 14'

#Если MainClass возвращает другое число, то сообщает что не равняется 14







