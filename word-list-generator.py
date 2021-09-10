
	import random
import colorama
from colorama import Fore, Back, Style
import sys
import string
from itertools import product
from colorama import init

if sys.version_info[0] != 3:
    print('''\t--------------------------------------\n\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 
    fb.py\n\t--------------------------------------''')
    sys.exit()
init(autoreset=True)
print(f"   {Fore.GREEN}  {Style.BRIGHT} WORDLIST GENERATOR")
print("______________________________________")

print(f"{Style.BRIGHT}{Back.BLUE}A tool developer : P4NP")
print("______________________________________")
print(f"{Style.BRIGHT}{Fore.RED}YouTube :P4NP ")
print("______________________________________")

num=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]

A= input(f"{Style.BRIGHT}{Fore.GREEN}This is for educational process[Y/N]: ")
if (A == "Y"):
	print("you are using for educational process")
elif (A == "y"):
	print("you are using for educational process")
elif (A == "N"):
		print("use it in your own risk")
elif (A == "n"):
		print("use it in your own risk")		
else:
			print ("some thing went wrong")
			sys.exit(0)
	 	
min_length = input("Enter the minimum length of  password: ")
if min_length in num:
	 	print("")
else:
	 		print("invalid or large num ")
	 		sys.exit(0)	
max_length= input("Enter the maximum length of password: ")
if max_length in num:
	print("")
else:
	print("invalid or large num ")
	sys.exit(0)
	
mini = int(min_length)	
maxi=int(max_length)

print(f"  {Fore.BLUE} Your password list is creating please wait......")

counter =0
character=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
file_open = open("password.txt","w")
for i in range (mini , maxi+1):
			     	for j in product(character,repeat=i):
			     		word ="".join(j)
			     		file_open.write(word)
			     		file_open.write("\n")
			     		counter+=1
			     		
print("Password  list {} has been generated in password.txt" .format(counter))     
