#1.mulitpleinheritence basic question
class father:
    def skill(self):
        print(f'skill is the driving')
        
class mother:
    def hobbies(self):
        print(f'the hobbies is cooking')
        
class child(father,mother):
    def study(self):
        print(f"the hobby is child")
        
rohan=child()
rohan.skill()
rohan.hobbies()
rohan.study()



#2. multiple inheritence by using the constructor
class Father:

    def __init__(self, father_name):
        self.father_name = father_name

    def father_info(self):
        print(f"Father name: {self.father_name}")


class Mother:

    def __init__(self, mother_name):
        self.mother_name = mother_name

    def mother_info(self):
        print(f"Mother name: {self.mother_name}")


class Child(Father, Mother):

    def __init__(self, father_name, mother_name, child_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def child_info(self):
        print(f"Child name: {self.child_name}")


child1 = Child("Aman", "Priya", "Rahul")

child1.father_info()
child1.mother_info()
child1.child_info()
    
        
