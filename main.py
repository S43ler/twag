import time

fname = input("What is the name of the file?\n")
file = open(fname+".txt", "a")
name = input("What should be the name?\n")
email = input("What should be the email?\n")
usr = input("What should be the username?\n")
pwd = input("What should be the password?\n")
phone = input("What should be the phone number?\n")
data = []
data.append(name)
data.append(email)
data.append(usr)
data.append(pwd)
data.append(phone)

for i in range(len(data)):
	file.write(data[i] + "\n")
	
file.close()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Sta
