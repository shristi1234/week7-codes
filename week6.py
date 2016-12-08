print("Welcome to the Prudent Healthcare Center")
print("Login process")


file="dic.txt"

def writes(patientid, Firstname, Lastname, Address, Gender, Contact):
    fw = open('dic.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s\n" % (patientid, Firstname, Lastname, Address, Gender, Contact))
    fw.close()

textfile="payment.txt"

def cost(name,through,receiptbill):
        fw = open('data.txt', "w")
        fw.write("%1s%20s%20s\n" % (name,through,receiptbill))
        fw.close()


def credit(name,through,creditbill):
    fw = open('payment.txt', "w")
    fw.write("%1s%20s%20s\n" % (name,through,creditbill))
    fw.close()


print("Choose\n1. Physican \n2. Accountant")


def login():

    email=input("Enter your username:")
    print(email)
    password=input("Enter your password:")
    print(password)
    print("login successful")
    print("continue for further process")




def read():
    users = open("dic.txt",'r')
    eee = input("Please input patient ID")
    for each_line in users:
        (patientid, Firstname, Lastname, Address, Gender, Contact) = each_line.split()

        if (patientid == eee):
            print(patientid, Firstname, Lastname, Address, Gender, Contact)
    users.close()



def registration():
    patientid = input("Enter patientid:")
    firstname = input("Enter your firstname:")
    lastname = input("Enter your lastname:")
    address = input("Enter your address:")
    gender = input("Enter your gender: ")
    contact = input("Enter your contact number:")
    writes(patientid, firstname, lastname, address, gender, contact)
    print("THANK YOU!!!")
    print("\nUser created!\n")

def appointment():
    print("Start Appointment process")
    print("List of patients")
    print("N. Nirmiata")
    print("S. Sabiya")


    # This is for patent Nirmita
    select_patient = input("Choose your Patient\n")

    if select_patient == "N":
        print("Nirmita \n a. 08:00AM-09:00AM ")



            # This is for Doctor Sabiya

    elif select_patient == "S":

        print("Sabiya \n a. 09:30AM-10:30AM")




    else:
            print("waiting list")

def payment():
    print("Choose\n1. cash record\n2. credit record")

    payment = input("payment process by cash")
    if payment == "1":
        print("Payment by cash:")
        patientId = input("Idno: ")
        InvoiceNo = input("Invoiceno:")
        name = input("Enter FIrst Name: ")
        lastName = input("Last Name: ")
        address = input("Address: ")
        contact = input("Contact No: ")
        Amount = input("Amount:")
        print("payment  Success\n Thank you for payment")

        payment(patientId, InvoiceNo, name, lastName, address, contact, Amount)
        print("Register Success")

        print("Thank you")

    elif payment == "2":
        print("payment by credit card")
        patientId = input("Idno: ")
        creditcardNo = input("creditcardNo:")
        name = input("Enter First Name: ")
        lastName = input("Last Name: ")
        address = input("Address: ")
        contact = input("Contact No: ")
        Amount = input("Amount:")
        print("payment  Success\n Thank you for payment")

        credit(patientId, creditcardNo, name, lastName, address, contact, Amount)
        print("Register Success")

    else:
        print("Sorry payment is not complete ,go for payment")
        print("Thank You")

def logout():
    print("Logout")
    print("Thank you for your process!!!")


choose= input("User option?")
number= int(choose)
if (number==1):
    login()

    users=input("Choose your patient\n1.new patient\n2.old patient")
    number=int(users)
    if (number==1):
        registration()
    elif(number==2):
        users = input("press enter for patient information")
        read()
    else:
        print("wrong choice")

    users=input("Start your appoinment?\n1.yes\n2.no")
    number=int(users)
    if(number==1):
        appointment()
        logout()
    elif(number==2):
        print("is the patient is\n1.new patient\n2.old patient")

    else:
        print("wrong choice")

elif(number==2):
    login()
    users=input("press enter for patient information")
    read()
    users=input("press enter for payment process")
    payment()
    logout()

else:
    print("Wrong process")
