# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# OOP IN PYTHON NOTES 
#this is getting started with the basicsin python 

# %%
#CLASS is like a blue print 
#this will let ypu bundle together behaviour and state 
class NbaPlayer():
    #class for all nba players 
    #properties of an nba player 
    name=''
    jearseyNO=0

    #BEHAVIOUR 
    def shoot(self):
        print('shooting')
    def dunk(self):
        print('dunking')
        

#instaces of the class 

pg=NbaPlayer()
pg.name='steph curry'
pg.jearseyNO=30

sf=NbaPlayer()
sf.name='lebron james'
sf.jearseyNO=23
print(pg.name)
print(pg.jearseyNO)
pg.shoot()
print(sf.name)
print(sf.jearseyNO)
sf.dunk()

# %% [markdown]
# ENCAPSULATION
# %% [markdown]
# Encapsulation is one of the fundamentls 
# of oop ..this enables us to hide the complexity of the internal 
# working of the object which is advantageous to the developer 
# in the following ways 
#     simplifies and makes it easy to unserstand to use an object without knowing the internals 
#     managable changes 
# encapsulation provides us the mechanism to restrict the acces s to some of teh objects components this means thatthe interbal implemementatons of the object cant be seen form the outiside of the object 
# 
# this datacan be accessed using getters and setters
# 

# %%
class NBA(object):
    #setter
    def setName(self,name):
        self.name=name
        #getter
    def getName(self):
        return self.name    
        #setter 
    def setPosition(self,pos):
        self.pos=pos
    def getPosition(self):
        return self.pos    
p=NBA()
f=NBA()
f.setName('Kevin Durant')
f.setPosition('small forward')

p.setName('stephcurry') 
p.setPosition('point gaurd')
print(p.getName())
print(p.getPosition())
print(f.getName())
print(f.getPosition())
#this setters only setthe value 
#if it achieves exception handling 
"""
this demostrates howclasses are created methods 
acccessors and the mutators and how to create the instances 
of the specific class which is a type of player 
"""

# %% [markdown]
# 
# CONSTRACTOR
# the init cnstractor is simply called as soon as an object is instanciated 
# THe init stands for initialization as it initializes attributes of the instance 
# it is called the contracto of the class 
# 
# The property that all classes of all objectsmust be defined  in a method called __init__()
# sets the initial state of the of the object by assigning the values of the object  prperties ,that is __init__()initialises each instance of the class 
# 
# one can give __init__() any number of parameters but the first variable will be always self key word 
# 

# %%
class NBA(object):
    def __init__(self,age,pos,name):
        #the constractor 
        self.age=age
        self.pos=pos
        self.name=name
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getposition(self):
        return self.pos
#instance of a playerin the nba 
player_onr=NBA(32,'point gaurd','steph curry')
print(player_onr.getage())
print(player_onr.getposition())
print(player_onr.getname())


"""
demonstartes how the consttrator in py works 
there is no need of the getter and the mutators 
"""

# %% [markdown]
# the __init__() method creates an attribute name and assign it a value name 
# THe attributes created are are instance attribute An instance attribute is specific to 
# a particular instance of a class 
# All objects have some property 
# 
# Class attributes aoutside the __init__() method do not change when assigning new class instances 
# 
# __str__() is a dunder method because they start with double underscores 
# they are self calling methods once the class in instanciated 

# %%
class Dog:
    #class outside the __init__()
    species="Canis familiaris"
    #remains constant 
    def __init__(self,name,breed):
        #this attributes have different value in each instance 
        self.name=name
        self.breed=breed
    def __str__(self):
        #self calling method thatreturns a string 
        return f"{self.name} is a {self.breed}"
bobby=Dog('bobby','germanshepherd')
#printing bobby prints the memory location of the instance 
print(bobby)
print(bobby.name)
print(bobby.breed)
print(bobby)

        

# %% [markdown]
# Methods in OOP
#     External methods ->other objects can invoke 
#     internal methods ->not reachable by otherobjects 
#     
#     Encapsulation
#     Protecting data 
#     THe data is internam and should be protected from outside manipulatiion 
#     or rather uncontrolled outside manipulation 
#     
#     1.you dont need to know the internals 
#     2.you shouldnt know the internals 
#     
#     Access levels
#         hide data using access modifiers 
#         using an underscore shows that the property is private to the class 
#         with one leading underscore it makes the property protected 
#         with two leading underscores it makes the propety private 
#         _height->protected 
#         __height->private 
#         
#         private property is visible to specific class 
#         protected makes the property visible only to classes that extend or inherit
#         from domain of the property 
#         
#     

# %%
class Square:
    def __init__(self,height,width):
        self._height=height
        self._width=width
    def setSide(newHieght):
        _height=newHieght
    def setWidth(newWidth):
        _width=newWidth    
#instances of class 
sqr=Square(8,9)

print(sqr._height)
print(sqr._width)
#the value will change bacause it is protected 


# %%
class Square:
    def __init__(self):
        self.__height=2
        self.__width=2
    def setSide(self,height):
        self.__height=height
    def getSide(self):
        return self.__height
#instances of class 
sqr=Square()
sqr.setSide(3)

print(sqr.__height)
#throws an error because the property is private and cant be altered outside the class 

# %% [markdown]
# # Getters and setters or Accessors and mutators
# %% [markdown]
# We've said so far that data in general shouldn't be touched from the outside. Data is the concern of the object. As with all rules and strong recommendations, there are exceptions. Sometimes you need to change the data. Or, changing it's simpler than having to add a significant amount of code.
# 
# getters and setters arededicated to reading and changing your data 
# getters play the part of making private data readable to the outside 
#  setters are methods thatcan change the data directly insude the class 
# getters and setters methods are usually public 
# 

# %%
class Square:
    def __init__(self):
        self.__h=2
        self.__w=2
    def setSide(self,nside):
        #set values for new side 
        self.__h=nside
        self.__w=nside
    def getSide(self):
        return self.__h
    def validate(self,h):
        #this methods helps one not to set a negative value for hieght 
        #do this without a decorator eg property
        if self.__h>=0:
            self.__h=h
        else:
              print("value needs to be greater than 0")
s=Square()
s.validate(-2)
print(s.getSide())
            
            

# %% [markdown]
# # Decorators for setters and getters (property)
# 

# %%
class Square:
    def __init__(self,s):
        self.__h=s
        #self.__w=h
        
        
    #decorator     
    @property    
    def setside(self):
        return self.__h
    
    #decorator
    @setside.setter
    def setside(self,s):
        if s>=0:
            #make the initialisation if condition true 
            #this acts as a setter instead of creating two functions like in java 
            
            self.__h=s
            print("set successfully")
        else:
             raise Exception("cant be less than zero")
        
sqr= Square(-20)
sqr.h=30
print(sqr.setside)
        

# %% [markdown]
# Problem description
# Rock, paper, scissors is a game played by two participants. The game consists of rounds. In each round, a participant chooses a symbol from rock, paper, or scissors, and the other participant does the same. Then a winner of the round is determined by comparing the chosen symbols. The rules of the game state that rock wins over scissors, scissors beats (cuts) paper, and paper beats (covers) rock. The winner of the round is awarded a point. The game goes on for as many rounds as the participants agreed on. The winner is the participant with the most points.
# 
# phase  actor behavior data 
# 
# 

# %%
"""
rules of the game 
r wins over s
s beats p
p beats r
the winner of the round is given a point 
"""

class Player:
    """
    a player will choose a symbol
    either rock paper or scissors 
    
    """
    def __init__(self):
        self.points=0
        
        #check for win status 
        self.winp1=False
        self.winp2=False
             
    # def choosesymbol(self):
    #     if playerOne.choice=='r' and playerTwo.choice=='s':
    #         #game.endGame=True
    #         self.winp1=True
    #         print("player one won")
    #     elif playerOne.choice=='s'and playerTwo.choice=='p':
    #         #game.endGame=True
    #         self.winp1=True
    #         print("player one won")
    #     elif self.playerOne.choice=='p'and playerTwo.choice=='r':
    #         #game.endGame=True
    #         self.winp1=True
    #         print("player one won")
    #     if playerTwo.choice=='r' and playerOne.choice=='s':
    #         #game.endGame=True
    #         self.winp2=True
    #         print("player Two won")
    #     elif playerTwo.choice=='s'and playerOne.choice=='p':
    #         #game.endGame=True
    #         self.winp2=True
    #         print("player Two won")
    #     elif playerTwo.choice=='p'and playerOne.choice=='r':
    #         #game.endGame=True
    #         self.winp2=True
    #         print("player Two won")
    #     else:
    #         #game.endGame=True
    #         self.winp1=True
    #         self.winp2=True
    #         print("draw")
          
 
    #pass 
class Gameround:
    """
    award points to the players that have won
    compare choices aganist game rules 
    """
    def __init__(self):
        #self.p1=playerOne.points
        #self.p2=playerTwo.points
        self.choice=input("choice:")
        self.playerOne = Player()
        self.playerTwo = Player()
    #pass
   # def getpoints(self):
    #    if playerOne.winp1==True:
      #      self.p1+=1
     #   elif playerTwo.winp2==True:
       #     self.p2+=1
        #elif playerOne.winp1==True and playerTwo.winp2==True: 
         #   self.p2+=1
          #  self.p1+=1
    
    def play(self):
        #run the win checking 
        self.playerOne.choosesymbol()
        self.playerTwo.choosesymbol()
        
rps=Gameround()
rps.play()

class Game:
    """
    contains the game logic 
    cheking for wins and loses 
    
    
    """
    pass
   
        #pass
    
    


        

# %% [markdown]
# # inheritance
# %% [markdown]
# the process by which a class takes the attributes and methods of another 
# newly formaed classes are called child classes 
# THe classes that child classes are derived form are called parent classes 
#  Through inheritance one can override methods and properties 
#  if a motherand a son have black hair ,,the son can dye the hair to red 
#  the son has overriden the black hair property to red 
#  
#  More generally all objects created form a child cass areinstances of the parent 
#  class although theymat not be instances of other hild classes 
#  

# %%
class Dog:
    species="cannis familiaris"
    def __init__(self,name,age,breed):
        self.name=name
        self.age=age
        self.breed=breed
    def walk(self):
        return "dog is walking"
        
    def sound(self):
        return "dog is barking"
    
        
class Cat(Dog):
    #extends class Dog
    #there arealso catbreeds 
    """
    a cat will inherit the properties ofa dog 
    a cat has age 
    breed
    name
    it will also inherit the methods like
    a catcan walk 
    a cat can make a sound 
    the methods will be overriden 
    """
    def __init__(self,name,age,breed,smallsize):
        #super allows the parent class to handle the properties the child class extends
        #super will handle name age and breed 
        #small size will be handled by class catinit method 
        super().__init__(name,age,breed)
        #or parentclassName.__init__(self,name,age,breed)
        #child class init will only handle initialisation of samllsize
        self.smallsize=smallsize
    def walk(self):
        return "cat is walking"
    def sound(self):
        return "cat meows"
            
c=Cat('peps','5','maine','verysmall')    
print(c.name)
print(c.age)
print(c.breed)
print(c.walk())
print(c.sound())
print(c.smallsize)
d=Dog('kambodia','6','labrado')
print(d.name)
print(d.breed)
print(d.walk())
print(d.sound())
#throws an error 
print(d.smallsize)#dog object has no attribute smallsize 
        

# %% [markdown]
# Dunder methods are used for when you dont need an invocaton
# they call them selves they are also used during operator overloading 
# eg the add operation and the concantenation of a string 
# 

# %%
class Dunder(object):
	#use of dunder methods 
	def __init__(self ,firstName,secondName):
		self.firstName=firstName
		self.secondName=secondName
	def __len__(self):
		#can be used to get the length of our objects name 
		return len(self.firstName)
	def __str__(self):
		return f"{self.firstName}{self.secondName}"	
emp1=Dunder('Richard ','Hendricks')
#returns the legth of the firt name 

print(len(emp1))	
print(emp1)		
#used to print the conatenated format of the last name and the mlast name 


# %%


# %% [markdown]
# The @classmethod decoator is a biuilt in function decorator that is an expression that gets eveluated after your function is defined
# The eresults of that evaluiation shadows your function definition 
# A class method rev=cieves the class as implicit first argumentjust like an instance method recieves the instance 
# A class method is bound to the class and not the object of the class 
# They have access to the state of the class as it takes a class arameter thatpoints to the class and not the object instance 
# It could moify a class var thatwill be applicable to all the instnces 
# 
# STATIC METHODS 
# @staticmethod
# is bound to the class and not the object instance 
# 
# class methods vs static methods 
# ->class methods take cls as the first param
# ->class methods can modify the class state 
# ->we use @class method decoator and @staticmethod decorator to create them 
# 

# %%
#demonstartion
from datetime import date
class NbaPlayer(object):
	def __init__(self,name,vertical,age):
		self.name=name
		self.vertical=vertical
		self.age=age
	@classmethod
	def fromBithYear(cls,name,year):
		return cls(name,2020-year)

	#a static methos to check any persons age 	
	@staticmethod
	def isAdult(age):
		if age>18:
			return 'he is an adult'
		else:
			return 'he is a minor'			
p1=NbaPlayer('steph',10,32)
p2=NbaPlayer('klay',40,30)
#p2=NbaPlayer.fromBithYear('steph',2000)
print(p1.isAdult(32))
print(p2.age);


# %%
#property decorator 
'''
property decorator 
@property 
part1
1.allow as to use class methods as attributes 
2.create the setter method and the getter method 
'''
class PropertDEmostratiion(object):
	#demonstarion of the property decorator 
	def __init__(self,name,grade):
		self.name=name
		self.grade=grade

	@property	
	def message(self):	
		#allow the usage of a method as an attribute 
		return self.name+"got grade"+self.grade
	@message.setter	
	def message(self,msg):
		sent=msg.split(" ")
		self.name=sent[0]
		self.grade=sent[-1]

stud1=PropertDEmostratiion('richard','A')	
#stud1.grade="B"
stud1.message='Gilfoyle got an A'
print(stud1.name)
print(stud1.grade,'\n')
print(stud1.message)	


# %%
"""
property decorator 
allows data encapsulation 
use two underscores  to signify that the varis private
allows as to use a method as aan attribute 

part2 

"""
class Student(object):
	def __init__(self,mark):
		self.__mark=mark
	def percentage(self):
		return (self.__mark/600)*100
	@property
	def marks(self):
		return self.__mark	
	@marks.setter		
	def marks(self,val):
		self.__mark=val


stud=Student(400)
#the method marks can now be used as an attribute 
#plus achieving encapsulation through data hiding 
stud.marks=500
#print(stud.__mark)		
print(stud.percentage(),"%")


# %%


# %% [markdown]
# ---Error Handling In Python---
# Error in python can be of two types syntax and exceptions 
# Exceptions are raised when internal events occur which changes the normal floww 
# of the program 
# 

# %%
class Quontient(object):
	def __init__(self,num,val):
		self.val=val
		self.num=num
	@property
	def calculate(self):
		try:
			return self.num/self.val	
		except :
			return 'zero division'
		# finally:
		# 	return "you cant devide a number by zero "		
	@calculate.setter
	def calculate(self,val):
		try:
			if val<1:
				self.val=1
				print(self.val)

			else:
				self.val=val	 	
		except:
			return 'error!'
q=Quontient(45,0)
q.calculate='6'
print(q.calculate)

# %% [markdown]
# KEY WORD ARGUMENTS 
# 
# Parameters are input variables boundes by paranthensis
# arguments are values assighned 
# 

