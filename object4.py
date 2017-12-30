class Student(object):
    __slots__ = ('name', 'age')



"""给实例绑定方法
def set_age(self, age): # 定义一个函数作为实例方法
...     self.age = age
from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

还可以给类绑定方法
Student.set_score = set_score

__slots__ 限定了绑定的属性
仅对当前类实例起作用，对继承的子类是不起作用的
"""

