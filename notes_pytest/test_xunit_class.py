import pytest

class TestClass:
    @classmethod
    def setup_class(cls):
        print("\nsetup class")

    @classmethod
    def teardown_class(cls):
        print("\nTearing Down class")

    def setup_method(self, function):
        if function == self.test1:
            print("\nSetup Method test1")
        elif function == self.test2:
            print("\nSetup Method test2")
        else:
            print("\nSetup unknown test")
    
    def teardown_method(self, function):
        if function == self.test1:
            print("\nTearing down test1")
        elif function == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unknown test")

    def test1(self):
        print("Test1")
        assert True
    
    def test2(self):
        print("Test2")
        assert True

