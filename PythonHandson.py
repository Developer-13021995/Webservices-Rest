class Dog:

	species = "mammal"
	def __init__(self, name, age):
		self.name=name;
		self.age=age
	
	# instance method
	def description(self):
		return "{} is {} years old".format(self.name, self.age)

    # instance method
	def speak(self, sound):
		return "{} says {}".format(self.name, sound)

		
philo = Dog("Philo", 6)
mike = Dog("Mike", 10)

jake = Dog("Jake", 7)
doug = Dog("Doug", 4)
william = Dog("William", 5)

print("{} is {} years old and {} is {} years old".format(philo.name, philo.age, mike.name, mike.age))
print("{0} is {1} years old and {2} is {3} years old".format(philo.name, philo.age, mike.name, mike.age))
print(f"{philo.name} is {philo.age} years old and {mike.name} is {mike.age} years old")

def get_biggest_number(*argv):
	if(argv):
		return max(argv)
	else:
		raise ValueError('Variable arguments should be atleast one')

def get_smallest_number(*argv):
	if(argv):
		return min(argv)
	else:
		raise ValueError('Variable arguments should be atleast one')
print(f"The Oldest dog is {get_smallest_number(philo.age, mike.age, jake.age, doug.age, william.age)} years old")


######################################################To find oldest dog age using Generator expression ##########################################
def get_oldest_dog_using_generator(*argv):
	return max(dog.age for dog in argv)

print(f"The oldest dog is {get_oldest_dog_using_generator(jake, doug,william, philo, mike 	)} years old using generator expression")

##################################################################################################################################################



######################################################To find oldest dog object ##################################################################
def get_oldest_dog(*argv):
	tempAge = 0
	for arg in argv:
		if(isinstance(arg,Dog)):
			if(arg.age > tempAge):
				tempAge = arg.age
				olderDog = arg
	return olderDog

print(f"The oldest dog is {get_oldest_dog(jake, doug,william, philo, mike).name} with age {get_oldest_dog(jake, doug,william, philo, mike).age}")

###################################################################################

from operator import attrgetter
def get_oldest_dog_using_attr_getter(*argv):
	return max(argv, key=attrgetter("age"))
	
print(f"The oldest dog is {get_oldest_dog_using_attr_getter(jake, doug,william, philo, mike 	).age} years old using attr getter")
##################################################################################################################################################


#def get_oldest_dog_using_lamda(*argv):
#	return max(argv, key=lamda item: item.age)

#print(f"The oldest dog is {get_oldest_dog_using_lamda(jake, doug,william, philo, mike 	)} years old using lambda expression")

###################################################### Instance methods ##########################################################################

print(mike.description())
print(mike.speak("Gruff Gruff"))

######################################################## Modifying attributes ########################################################################

class Email:
	
	def __init__(self):
		self.is_sent = False # note: boolean value should start with capital letter otherwise it throws NameError name 'false is not defined'
	
	def send_email(self):
		self.is_sent = True
		
email = Email()
print(email.is_sent)
email.send_email()
print(email.is_sent)

##############################################################################################################################################

#Function Arguments
#You can call a function by using the following types of formal arguments −

#Required arguments - These are the arguments which are to be provided at the time of function call or else we get syntax error from interpretor
#Keyword arguments - These are the optional parameters and they donot maintain a specific order
#Default arguments
#Variable-length arguments

##############################################################################################################################################

def keyword_parameter_usage(name, age, school):
	print(f"Name of student is {name}")
	print(f"Age of student is {age}")
	print(f"School of student is {school}")
	return

keyword_parameter_usage(age=10, name="harish", school="Sri chaitanya")


#The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).

#A keyword argument is where you provide a name to the variable as you pass it into the function.
#One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.
#Example for usage of **kwargs:

def variable_length_keyword_args(**kwargs):
	for key,value in kwargs.items():
		print ("%s == %s" %(key, value))

variable_length_keyword_args(first ='Geeks', mid ='for', last='Geeks')

#########################################

def myFun(arg1, arg2, arg3):
	print("arg1:", arg1) 
	print("arg2:", arg2) 
	print("arg3:", arg3) 
      
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
print(type(args))
myFun(*args) 
  
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
print(type(kwargs))
myFun(**kwargs) 


############################################################Exception Handling#######################################################################################3
import sys
import logging
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
try:
	linux_interaction()
except: 
	print('Linux function was not executed')
	pass
	
try:
	linux_interaction()
except AssertionError as error:
	print(error) 
	print('Linux function was not executed')
	pass
	
	
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as exp:
	logging.exception(f"something wrong has hapend '\n'{exp}")
	print(exp)
	print('Could not open file.log')
