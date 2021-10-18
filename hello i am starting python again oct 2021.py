#a simple revision of txt work
#the way it will work is to read the contents of a hard-coded-in folder and list files
#i can chosoe a file to read/edit
#or make a new file too
#this will also be a way for me to learn how to work with github ig

import os 
print(os.getcwd()) #tell directory where stuff is going (stuff ie stuff i create through python)


#make file, empty is fine
f=open("trial stuff.txt", 'w') #in C: Users Omair
f.close()

#read contents and add stuff
with open("trial stuff.txt", 'r+') as f:  #PRESSING ENTER ENDS ENTRY, FIND WAY TO LET TEXT STILL BE TYPED WITH ENTER
	print (f.readlines()) #contents
	text=str(input("you may now enter the new text to (please note that in the current version pressing enter stops the entry and adds it, we shall fix that sometime, for now please just type \\n):\n"))
	f.write(" "+text)


#just to read 
f=open("trial stuff.txt", 'r')
print(f.read())

