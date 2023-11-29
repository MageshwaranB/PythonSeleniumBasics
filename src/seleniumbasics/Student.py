import pytest


class Student:
    school_name = "RRR higher secondary school"
    class_no = "10"
    _name=""
    _age=0
    def set_name(self,name):
        self._name=name
    def get_name(self):
        return self._name

    def set_age(self,age):
        self._age=age

    def get_age(self):
        return self._age

    def get_school_name(self):
        return self.school_name

    def get_class_no(self):
        return self.class_no
pytest.student=Student()
pytest.student.set_name("Tommy")
print(pytest.student.get_name())
