import random
import datetime

name = []
phno = []
add = []
bookedin = []
bookedout = []
Playground = []
price = []
rc = []
p = []
Playgroundno = []
custid = []
day = []

i = 0


def Home():
	
	print("\t\t\t\t\t\t Welcome To Novel's Playground\n")
	print("\t\t\t 1 Booking\n")
	print("\t\t\t 2 Playground_Info\n")
	print("\t\t\t 3 Payment\n")
	print("\t\t\t 4 Record\n")
	print("\t\t\t 0 Exit\n")

	ch=int(input("->"))
	
	if ch == 1:
		print(" ")
		Booking()
	
	elif ch == 2:
		print(" ")
		Playground_Info()
	
	
	elif ch == 3:
		print(" ")
		Payment()
	
	elif ch == 4:
		print(" ")
		Record()
	
	else:
		exit()


def date(c):
	
	if c[2] >= 2019 and c[2] <= 2021:
		
		if c[1] != 0 and c[1] <= 12:
			
			if c[1] == 2 and c[0] != 0 and c[0] <= 31:
				
				if c[2]%4 == 0 and c[0] <= 29:
					pass
				
				elif c[0]<29:
					pass
				
				else:
					print("Invalid date\n")
					name.pop(i)
					phno.pop(i)
					add.pop(i)
					bookedin.pop(i)
					bookedout.pop(i)
					Booking()
			
			
			
			elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
				pass
			
			
			elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
				pass
			
			
			elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
				pass
			
			
			elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:
				pass
			
			else:
				print("Invalid date\n")
				name.pop(i)
				phno.pop(i)
				add.pop(i)
				bookedin.pop(i)
				bookedout.pop(i)
				Booking()
				
		else:
			print("Invalid date\n")
			name.pop(i)
			phno.pop(i)
			add.pop(i)
			bookedin.pop(i)
			bookedout.pop(i)
			Booking()
			
	else:
		print("Invalid date\n")
		name.pop(i)
		phno.pop(i)
		add.pop(i)
		bookedin.pop(i)
		bookedout.pop(i)
		Booking()


# Booking function
def Booking():
	
		
		global i
		print(" BOOKING playground")
		print(" ")
		
		while 1:
			n = str(input("Name: "))
			p1 = str(input("Phone No.: "))
			a = str(input("Address: "))
			
			
			if n!="" and p1!="" and a!="":
				name.append(n)
				add.append(a)
				break
				
			else:
				print("\tName, Phone no. & Address cannot be empty..!!")
                
        #write date as example: dd/mm/yyyy)
        
		cii=str(input("Booked-In: "))
		bookedin.append(cii)
		cii=cii.split('/')
		ci=cii
		ci[0]=int(ci[0])
		ci[1]=int(ci[1])
		ci[2]=int(ci[2])
		
		coo=str(input("Booked-Out: "))
		bookedout.append(coo)
		coo=coo.split('/')
		co=coo
		co[0]=int(co[0])
		co[1]=int(co[1])
		co[2]=int(co[2])
				
		# Booked-in date
		if co[1]<ci[1] and co[2]<ci[2]:
			
			print("\n\tErr..!!\n\tbooked-Out date must fall after booked-In\n")
			name.pop(i)
			add.pop(i)
			bookedin.pop(i)
			bookedout.pop(i)
			Booking()
		elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
			
			print("\n\tErr..!!\n\tBooked-Out date must fall after booked-In\n")
			name.pop(i)
			add.pop(i)
			bookedin.pop(i)
			bookedout.pop(i)
			Booking()
		else:
			pass
		
		date(co)
		d1 = datetime.datetime(ci[2],ci[1],ci[0])
		d2 = datetime.datetime(co[2],co[1],co[0])
		d = (d2-d1).days
		day.append(d)
		
		print("----SELECT Playground TYPE----")
		print(" 1. Hockey court")
		print(" 2. Basketball court")
		print(" 3. Tennise court")
		print(" 4. Cricket Ground")
		print(("\t\tPress 0 for playground Prices"))
		
		ch=int(input("->"))
		
		
		if ch==0:
			print(" 1. Hockey court - Rs. 3500")
			print(" 2. Basketball court - Rs. 4000")
			print(" 3. Tennise court - Rs. 4500")
			print(" 4. Cricket Ground - Rs. 5000")
			ch=int(input("->"))
		if ch==1:
			Playground.append('Hockey court')
			print("ground Type- Hockey court")
			price.append(3500)
			print("Price- 3500")
		elif ch==2:
			Playground.append('Basketball court')
			print("ground Type- Basketball court")
			price.append(4000)
			print("Price- 4000")
		elif ch==3:
			Playground.append('Tennise court')
			print("ground Type- Tennise court")
			price.append(4500)
			print("Price- 4500")
		elif ch==4:
			Playground.append('Cricket Ground')
			print("ground Type- Cricket Ground")
			price.append(5000)
			print("Price- 5000")
		else:
			print(" Wrong choice..!!")


		
		rn = random.randrange(40)+300
		cid = random.randrange(40)+10
		
		
		
		while rn in Playgroundno or cid in custid:
			rn = random.randrange(60)+300
			cid = random.randrange(60)+10
			
		rc.append(0)
		p.append(0)
			
		if p1 not in phno:
			phno.append(p1)
		elif p1 in phno:
			for n in range(0,i):
				if p1== phno[n]:
					if p[n]==1:
						phno.append(p1)
		elif p1 in phno:
			for n in range(0,i):
				if p1== phno[n]:
					if p[n]==0:
						print("\tPhone no. already exists and payment yet not done..!!")
						name.pop(i)
						add.pop(i)
						bookedin.pop(i)
						bookedout.pop(i)
						Booking()
		print("")
		print("\t\t\t***Playground BOOKED SUCCESSFULLY***\n")
		print("Playground No. - ",rn)
		print("Customer Id - ",cid)
		Playgroundno.append(rn)
		custid.append(cid)
		i=i+1
		n=int(input("0-BACK\n ->"))
		if n==0:
			Home()
		else:
			exit()

# PLAYGROUND INFO
def Playground_Info():
	print("1).Hockey court")
	print("---------------------------------------------------------------")
	print("---Well maintained court,")
	print("---3 to 5 star feedback given by customer")
    
	print("2).Basketball court")
	print("---------------------------------------------------------------")
	print("---Well maintained court,")
	print("---3 to 5 star feedback given by customer")
	
    
	print("3).Tennise court")
	print("---------------------------------------------------------------")
	print("---Well maintained court,")
	print("---3 to 5 star feedback given by customer")
    
	print("4).Cricket Ground")
	print("---------------------------------------------------------------")
	print("---Well maintained court,")
	print("---3 to 5 star feedback given by customer")
	print()
	n=int(input("0-BACK\n ->"))
	if n==0:
		Home()
	else:
		exit()


# PAYMENT FUNCTION			
def Payment():
	
	ph=str(input("Phone Number: "))
	global i
	f=0
	
	for n in range(0,i):
		if ph==phno[n] :
			
			
			if p[n]==0:
				f=1
				print(" Payment")
				print(" --------------------------------")
				print(" MODE OF PAYMENT")
				
				print(" 1- Credit/Debit Card")
				print(" 2- Paytm/PhonePe")
				print(" 3- Using UPI")
				print(" 4- Cash")
				x=int(input("-> "))
				print("\n Amount: ",(price[n]*day[n])+rc[n])
				print("\n		 Pay For Novel")
				print(" (y/n)")
				ch=str(input("->"))
				
				if ch=='y' or ch=='Y':
					print("\n\n --------------------------------")
					print("		 Novel's Playground")
					print(" --------------------------------")
					print("			 Bill")
					print(" --------------------------------")
					print(" Name: ",name[n],"\t\n Phone No.: ",phno[n],"\t\n Address: ",add[n],"\t")
					print("\n Booked-In: ",bookedin[n],"\t\n Booked-Out: ",bookedout[n],"\t")
					print("\n Playground Type: ",Playground[n],"\t\n Playground Charges: ",price[n]*day[n],"\t")
					
					print(" --------------------------------")
					print("\n Total Amount: ",(price[n]*day[n])+rc[n],"\t")
					print(" --------------------------------")
					print("		 Thank You")
					print("		 Visit Again :)")
					print(" --------------------------------\n")
					p.pop(n)
					p.insert(n,1)
					
					
					Playgroundno.pop(n)
					custid.pop(n)
					Playgroundno.insert(n,0)
					custid.insert(n,0)
					
			else:
				
				for j in range(n+1,i):
					if ph==phno[j] :
						if p[j]==0:
							pass
						
						else:
							f=1
							print("\n\tPayment has been Made :)\n\n")
	if f==0:
		print("Invalid Customer Id")
		
	n = int(input("0-BACK\n ->"))
	if n == 0:
		Home()
	else:
		exit()

# RECORD FUNCTION
def Record():
	
	# checks if any record exists or not
	if phno!=[]:
		print("	 *** PLAYGROUND RECORD ***\n")
		print("| Name	 | Phone No. | Address	 | Booked-In | Booked-Out	 | Playground Type	 | Price	 |")
		print("----------------------------------------------------------------------------------------------------------------------")
		
		for n in range(0,i):
			print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",bookedin[n],"\t|",bookedout[n],"\t|",Playground[n],"\t|",price[n])
		
		print("----------------------------------------------------------------------------------------------------------------------")
	
	else:
		print("No Records Found")
	n = int(input("0-BACK\n ->"))
	if n == 0:
		Home()
		
	else:
		exit()


Home()
