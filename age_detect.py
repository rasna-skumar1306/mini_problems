from datetime import datetime as date
def detect():
	if (dy-int(yyyy)) >= 18:
		if int(mm) < dm:
			print("you are eligible to vote")
		elif int(mm) == dm:
			if int(dd) <= da:
				print("you may proceed to vote")
				
		print("you may proceed to vote")
	else:
		print("you are not allowed to vote") 
	
da = date.now().day
dm = date.now().month
dy = date.now().year
print("enter your dob with \'-\' as separation")
dd,mm,yyyy = input("enter your DOB").split("-")
detect()

