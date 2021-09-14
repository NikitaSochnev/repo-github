class MainClass:
    __Class_String = "Hello, World"
    def getClassString(self):
        return self.__Class_String
class TestMainClass:
    def testGetClassString(self):
        a = (MainClass().getClassString())
        assert("Hello" in a or "hello" in a)


