class Person(object):
    def __init__(self, name, age, weight, job):
        self.name = name
        self.age = age
        self.weight = weight
        self.job = job

    def work(self):
        print("%s goes to work" % self.name)

class Employee(Person):
    def __init__(self, name, age, weight, job):
        super(Employee, self).__init__(name, age, weight, job)

    def work(self):
        print("%s is working" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, weight, job):
        super(Programmer, self).__init__(name, age, weight, job)

    def program(self):
        print("%s is coding" % self.name)


jeff = Person("Jeff", 21, 134, "Real Estate Agent")
steve = Employee("Steve", 42, 121, "Cashier")
bob = Programmer("Bob", 33, 199, "Programmer")
