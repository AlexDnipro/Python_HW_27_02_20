#https://www.codewars.com/kata/53f0f358b9cb376eca001079
#Regular Ball Super Ball

class Ball:
    def __init__(self, *b):
        self.ball_type = b[0] if b else "regular"

#https://www.codewars.com/kata/color-ghost
#Color ghost

import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white","yellow","purple","red"])

#Basic test for Color Ghost:
Test.describe("Basic test")
colors = ["white","yellow","purple","red"]
a=Ghost()
Test.assert_equals(True, colors.count(a.color) > 0)
test.expect(True, a.color in colors)



#https://www.codewars.com/kata/547274e24481cfc469000416
#Basic subclasses - Adam and Eva
def God():
    return (Man(),Woman())

class Human(object):
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

#https://www.codewars.com/kata/classy-classes
#ClassyClasses
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.info = "{}s age is {}".format(self.name,self.age)