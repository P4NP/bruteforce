import random
import colorama
from colorama import Fore, Back, Style

import string
from itertools import product
print(f"  {Fore.RED}         welcome ")
print(f"   {Fore.GREEN}   cradit = P4NP")
print("you can suscribe my yt name is =P4NP")
A= input("this is only for educational process[Y/N]: ")
if (A == "Y"):
	print("you are using for educational process")
elif (A == "y"):
	print("you are using for educational process")
elif (A == "N"):
		print("use it in your own risk")
elif (A == "N"):
		print("use it in your own risk")		
else:
			print ("some thing went wrong")
	
min_length = int(input("Enter the minimum length of  password: "))
if (min_length <= 100):
	print("sucessfully summited write another")
else:
	print("something went wrong")
	
max_length= int (input("Enter the maximum length of password: "))
if (max_length <=100) :
	print("sucessfully summited write another")
else:
	print("something went wrong")
print(f"  {Fore.BLUE} Your password list is creating please wait......")
counter =0
character=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
file_open = open("password.txt","w")
for i in range (min_length , max_length+1):
			     	for j in product(character,repeat=i):
			     		word ="".join(j)
			     		file_open.write(word)
			     		file_open.write("\n")
			     		counter+=1
			     		
print("Password  list {} has been generated in password.txt" .format(counter))
			     
