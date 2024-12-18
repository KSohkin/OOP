'''
E = int(input("What code do you wish to run?, :"))

match E:
    case 1:


     num = int(input("Enter your number: "))
     sum = 0
     prod = 1
     original_Number = num

     while(num != 0):
       rem = num%10
       sum=sum+rem
       prod=prod*rem
       num=num//10

     if (sum + prod == original_Number):
      print("Spy number")

     else:
      print("Not an spy number")
    case 2:
     num = int(input("Enter your number: "))
     sum = 0
     prod = 1
     original_Number = num

     while(num != 0):
         rem = num%10
         sum=sum+rem
         prod=prod*rem
         num=num//10

     if (sum + prod == original_Number):
         print("Special number")

     else:
         print("Not an special number")


num = int(input("Enter your number: "))
sum = 0
prod = 1
original_Number = num

while(num != 0):
         rem = num%10
         if rem == 0:
                 count+=1
         num=num//10

if count>0:
         print("duck number")

else:
         print("Not a duck number")


num = int(input("Enter a number: "))
sum = 0
sqr = num * num

while (sqr != 0):
    rem = sqr%10
    sum = sum+rem
    num = num//10

if (sum == num):
    print("N3on number")
else:
    print("Nein N3on number")

#Factorial

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

avg = (num1 + num2) / 2

print("Average is, ",avg )


def add_sum(num1, num2):
    sum=num1+num2
    average=sum/2
    return sum, average
    

print(add_sum(num1=20, num2=30))


def find_factorial(n):
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
find_factorial(5)

#Emp

class Employee:
    pass
emp1=Employee()
emp2=Employee()
emp1.first="Alex"
emp1.last="Kass"
emp1.email="Alex.Kass@company.com"
emp1.age="25"
emp1.pay=5000

emp2.first="David"
emp2.last="Tobias"
emp2.email="David.Tobias@company.com"
emp2.age="28"
emp2.pay=4000


class Employee:
    def __init__(self, first, last, age, pay):
        self.first=first
        self.last=last
        self.age=age
        self.pay=pay
    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def email(self):
        return '{}.{}'.format(self.first, self.last+'@company.com')
emp1 = Employee(first="Alex", last="Kass", age=25, pay=5000)
emp2 = Employee(first="David", last="Tobias", age=28, pay=4000)
#print(emp1.first)
#print(emp1.pay)
#print(emp2.age)
print(emp1.email()) 

#Car

class Car:
    def __init__(self, Manufacture, model, year, price,):
        self.Manufacture=Manufacture
        self.model=model
        self.year=year
        self.price=price

    def drive(self):
        return(f"you drive {self.Manufacture} car")
    def stop(self):
        return(f"you stop {self.model} car")
    def Car_details(self):
        return("{} {} {} {}".format(self.Manufacture, self.model, self.year, self.price))

Firstcar = Car(Manufacture="Mitusbishi", model="Evo", year=2015, price=31050)
Secondcar = Car(Manufacture="Nissan", model="GT-R", year=2023, price=156251)
Thirdcar = Car(Manufacture="Ferrari", model="F40", year=1987, price=138600)
Fourthcar = Car(Manufacture="Bugatti", model="Chiron", year=2023, price=2900000)
Fifthcar = Car(Manufacture="Rolls Royce", model="Phantom", year=2023, price=460000)



print(Thirdcar.Car_details())

#Calc

class calculation:
    def __init__(self, a, b, c, d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

class calculation1(calculation):
    def calculation1(self):
        add = self.a + self.b + self.c + self.d
        print("The answer of the first calculation is: ", add)

class calculation2(calculation):
    def calculation2(self):
        add = self.a - self.b + self.c - self.d
        print("The answer of the second calculation is: ", add)
        
class calculation3(calculation):
    def calculation3(self):
        add = self.a * self.b + self.c / self.d
        print("The answer of the third calculation is: ", add)
        
class calculation4(calculation):
    def calculation4(self):
        add = self.a / self.b + self.c * self.d
        print("The answer of the fourth calculation is: ", add)

Calculation1 = calculation1(1, 2, 3, 4)
Calculation2 = calculation2(1, 2, 3, 4)
Calculation3 = calculation3(1, 2, 3, 4)
Calculation4 = calculation4(1, 2, 3, 4)

print()
print("Calculation")

Calculation1.calculation1()
Calculation2.calculation2()
Calculation3.calculation3()
Calculation4.calculation4()


#Animal

class Animal:
    def __init__(self, name):
        self.name=name

    def eat(self):
        print(f"{self.name} is eating")
        
    def sleeping(self):
        print(f"{self.name} is sleeping")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
    
class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")
class Rabbit(Prey):
    pass
class Hawk(predator):
    pass
class Fish(Prey, predator):
    pass

fish = Fish("kala")
rabbit = Rabbit("Jänes")
hawk = Hawk("kull")

print()
print("Animal")

fish.hunt()
fish.sleeping()
fish.flee()
fish.eat()
print("--")
hawk.hunt()
hawk.sleeping()
hawk.eat()
print("--")
rabbit.sleeping()
rabbit.eat()
rabbit.flee()



class calculation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        sum = self.a + self.b 
        print("Sum is", sum)

class calculation1(calculation):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d
    def add1(self):
        sum = self.a + self.b + self.c + self.d
        print(f"{self.a} + {self.b} + {self.c} + {self.d} = ", sum)

class calculation2(calculation1):
    def __init__(self, a, b, c, d, e):
        super().__init__(a, b, c, d)
        self.e=e
    def add2(self):
        sum = self.a + self.b + self.c + self.d + self.e
        print(f"{self.a} + {self.b} + {self.c} + {self.d} + {self.e} = ", sum)
class calculation3(calculation2):
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c, d, e)
        self.f=f
    def add3(self):
        sum = self.a + self.b + self.c + self.d + self.e + self.f
        print(f"{self.a} + {self.b} + {self.c} + {self.d} +  + {self.f} = ", sum)
        

calc1 = calculation1(1, 2, 3, 4)
calc2 = calculation2(2, 3, 4, 5, 7)
calc3 = calculation3(2, 3, 4, 5, 7, 8)

print()
print("Calcuation2")

calc1.add1()
calc2.add2()
calc3.add3()



class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

class Einstein(Human):
    def __init__(self, name, age, height, iq):
        super().__init__(name, age, height)
        self.iq = iq

    def Einsteindata(self):
        print(f"{self.name} {self.age} {self.height} {self.iq}")

class Alex(Einstein):
    def __init__(self, name, age, height, iq, smart):
        super().__init__(name, age, height, iq)
        self.smart = smart

    def Alexdata(self):
        print(f"{self.name} {self.age} {self.height} {self.iq} {self.smart}")

class Newton(Einstein):
    def __init__(self, name, age, height, iq, smart, formula):
        super().__init__(name, age, height, iq)
        self.smart = smart
        self.formula = formula

    def Newtondata(self):
        print(f"{self.name} {self.age} {self.height} {self.iq} {self.smart} {self.formula}")

#objects
einstein = Einstein("Albert", 79, 167, 134)
alex = Alex("Nazarenko", 17, 180, 200, "Yes")
newton = Newton("John", 67, 176, 120, "Yes", "No")

# Print data
einstein.Einsteindata()
alex.Alexdata()
newton.Newtondata()



class vehicle:
    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name

    def Vehicledata(self):
        print(f"{self.vehicle_name}")

class car(vehicle):
    def __init__(self, car_name, vehicle_name, car_brand, car_model):
        super().__init__(vehicle_name)
        self.car_name = car_name
        self.car_brand = car_brand
        self.car_model = car_model

    def Cardata(self):
        print(f"{self.vehicle_name} {self.car_name} {self.car_brand} {self.car_model}")
        


class electricCar(car):
    def __init__(self, car_name, vehicle_name, car_brand, car_model, battery_type, battery_duration):
        super().__init__(car_name, vehicle_name, car_brand, car_model)
        self.battery_type = battery_type
        self.battery_duration = battery_duration

    def ECardata(self):
        print(f"{self.vehicle_name} {self.car_name} {self.car_brand} {self.car_model} {self.battery_type} {self.battery_duration}")
        

Vehicle = vehicle("Car")
Car = car("Honda civic", "Car", "Honda", "Civic")
eCar = electricCar("Car", "Tesla Cybertruck", "Tesla", "Cybertruck", "Lithium", "200 Miles")

# Print data
Vehicle.Vehicledata()
Car.Cardata()
eCar.ECardata()



class human:
    def __init__(self, name, age, IDNumber, salary):
         self.name = name
         self.age = age
         self.IDNumber = IDNumber
         self.salary = salary

    def Humandata(self):
        print(f"{self.name} {self.age} {self.IDNumber} {self.salary}")


class boy(human):
    def __init__(self, name, age, IDNumber, salary, bonus):
        super().__init__(name, age, IDNumber, salary)
        self.bonus = bonus

    def Boydata(self):
        print(f"{self.name} {self.age} {self.IDNumber} {self.salary} {self.bonus}")

    
    def totalsalary(self):
        totalsalary = self.salary + self.bonus
        print(f"{self.name}: ", totalsalary)


class girl(human):
    def __init__(self, name, age, IDNumber, salary, tips):
        super().__init__(name, age, IDNumber, salary,)
        self.tips = tips

    def Girldata(self):
        print(f"{self.name} {self.age} {self.IDNumber} {self.salary} {self.tips}")

    def totalsalary(self):
        totalsalary = self.salary + self.tips
        print(f"{self.name}: ", totalsalary)


Human = human("John Wick", 28, 505012506, 2000)
Boy = boy("Mark Smith", 25, 5025812585, 2600, 300)
Girl = girl("Lissandra Woman", 24, 5025862585, 2200, 150)

# Print data

Human.Humandata()
Boy.Boydata()
Girl.Girldata()

Boy.totalsalary()
Girl.totalsalary()




class Device:
    def __init__(self, name, year, brand, battery):
        self.name = name
        self.year = year
        self.brand = brand
        self.battery = battery

class Elec_car(Device):
    def __init__(self, name, year, brand, battery, power):
        super().__init__(name, year, brand, battery)
        self.power = power

class Smartphone(Device):
    def __init__(self, name, year, brand, battery, price):
        super().__init__(name, year, brand, battery)
        self.price = price

class Laptop(Device):
    def __init__(self, name, year, brand, battery, model):
        super().__init__(name, year, brand, battery)
        self.model = model





from abc import ABC, abstractmethod;

class Employee(ABC):
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
    @abstractmethod
    def calculate_pay(self):
        pass


class Full_time_employee(Employee):
    def __init__(self, name, age, id, salary, hours, bonus):
        super().__init__(name, age, id, salary)
        self.hours = hours
        self.bonus = bonus
    def calculate_pay(self):
        if self.hours > 200:
            self.salary += self.bonus
            print(f"Your salary is {self.salary}" )
        else:
            print(f"You get bonus so normal salary  {self.salary}")


class Part_time_employee(Employee):
    def __init__(self, name, age, id, salary, hourly_wage, hours_worked):
        super().__init__(name, age, id, salary)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    def calculate_pay(self):
        print(f"Your pay is {self.hourly_wage * self.hours_worked}")

class Intern(Employee):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age, id, salary)
    def calculate_pay(self):
        print(f"You are a internt NO PAY")
    
       


Andri = Full_time_employee("Andri", 10, "Elf", 100, 217, 10)
Joseph_Marinho = Part_time_employee("Joseph", 20, 15, 234, 5.50, 56)
Andreas = Intern("Andreas", 6, 20000, 0)


Andri.calculate_pay()
Joseph_Marinho.calculate_pay()
Andreas.calculate_pay()


class car:
    def __init__(self, brandname, color, speed):
        self.brandname = brandname
        self.color = color
        self.speed = speed

    def details(self):
        print(f"Brandname: {self.brandname}\n color: {self.color}\n speed: {self.speed}\n ")
    
toyota = car("Toyota", "Black", 160)
toyota.details()
print("New info")
toyota.color = "Blue"
toyota.speed= 200
toyota.details()



class electronic:
    def __init__(self, cost, name, type,):
        self.cost = cost
        self.name = name
        self.type = type
    
    def details(self):
        print(f"Cost: {self.cost}\n Name: {self.name}\n Type: {self.type}\n ")

phone = electronic("499$", "Xiaomi 13T", "Phone")
phone.details()
print("New Info")
phone.cost = "299$"
phone.name = "Xiaomi Redmi Note 13"
phone.type = "Phone"
phone.details()


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def details(self):
        print(f"Name: {self.name}\n position: {self.position}")

class Department:
    def __init__(self, name):
        self.name = name
        self.employee = []
    def add_employee(self, employee):
        self.employee.append(employee)
        print(f"{employee.name} added to {self.name} department")

    def list_employees(self):
        print(f"Employee in {self.name} department")
        for emp in self.employee:
            emp.details()

emp1 = Employee("Alex", "Software developer")
emp2 = Employee("Andri", "Hardware Developer")

department = Department("Software developer")
department.add_employee(emp1)
department.add_employee(emp2)
department.list_employees()

'''


class Professor:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def details(self):
        print(f"Name: {self.name}\n position: {self.department}")

class University:
    def __init__(self, name):
        self.name = name
        self.professor = []
    def add_professor(self, professor):
        self.professor.append(professor)
        print(f"{professor.name} added to {self.name} department")

    def list_professor(self):
        print(f"professor in {self.name} department")
        for emp in self.professor:
            emp.details()

Pro1 = Professor("Alex", "TKTK")
Pro2 = Professor("Andri", "TalTech")

university = University("Software developer")
university.add_professor(Pro1)
university.add_professor(Pro2)
university.list_professor()