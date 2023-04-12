                                                                            #Aadhar Card details locker
import re#imported the modules to use their classes objects and functions
import mysql.connector
import datetime
db=mysql.connector.connect(host="localhost", user="root", passwd="@LlaNJ@ME$1803")#Start by creating a connection to the database.
cur=db.cursor()
#cur.execute("create database Digital_Locker")
cur.execute("use Digital_Locker")
class Aadhar_Details:
    #cur.execute("create table Aadhar(Aadhar_Num int, Name varchar(20), DOB varchar(10),Address Varchar(100), primary key(Aadhar_Num))")
    cur.execute("ALTER TABLE Aadhar MODIFY Aadhar_Num BIGINT")#we were trying to save value 234142514254, which is more than the maximum INT value: 2147483647. So, we've modified the datatype
    cur.execute("ALTER TABLE Aadhar MODIFY DOB varchar(20)")
    def __init__(self):
        pass

#To display the table:
    def Display_List(self):
        cur.execute('select * from Aadhar')
        for list1 in cur:
            print(list1)

#To display the table by name and id number:
    def Details_by_Name(self):
        cur.execute("select Aadhar_Num, Name from Aadhar")
        for row in cur:
            print(row)
        db.commit()

#To update the address:       
    def update_Address(self, Adrs, Nm):
        ud="UPDATE Aadhar SET Address=%s WHERE Name=%s"#The %s allow us to format or place a string or numerical value within a given string. 
        input_data=(Adrs, Nm)
        cur.execute(ud, input_data)
        db.commit()
        print(cur.rowcount,"record affected")
        
#To update the name:
    def update_Name(self, New_Name,Old_Name):
        ud1="UPDATE Aadhar SET Name=%s WHERE Name=%s"
        input_data=(New_Name,Old_Name)
        cur.execute(ud1, input_data)
        db.commit()
        print(cur.rowcount,"record affected")
        
#To update the date of birth:
    def update_DOB(self, DOB, Aadhar_Number):
        ud2="UPDATE Aadhar SET DOB=%s WHERE Aadhar_Num=%s"
        input_data=(DOB, Aadhar_Number)
        cur.execute(ud2, input_data)
        db.commit()
        print(cur.rowcount,"record affected")

#To make sure that the date of birth is in a pre-defined format: 
    def Date_of_Birth(self,ip_dt):
        try:
            x = datetime.datetime.strptime(ip_dt,"%d/%m/%Y").date()
            return(x.strftime("%d/%m/%Y"))
        except ValueError:
            print("INVALID ENTRY! Make sure you're entering the data in DD/MM/YY format only")
#To check whether aadhar number is of 12 digits or not:
    def test_aadhar(self,AN):
                test=re.findall("\d",AN)
                for i in test:
                    if len(test)==12:
                        result=int(AN)
                        return(result)
#To add records in the table:
    def add_Record(self,Aadhar_Number,Name,DOB,Address):
                sql="insert into Aadhar(Aadhar_Num, Name, DOB, Address) values(%s,%s,%s,%s)"
                val=(Aadhar_Number, Name, DOB, Address)
                cur.execute(sql,val)
                print(cur.rowcount,"record added")
                db.commit()

#To delete unwanted entry:       
    def delete(self,Aadhar_Number):
        dt="DELETE FROM Aadhar WHERE Aadhar_Num=%s" %Aadhar_Number
        cur.execute(dt)
        db.commit()
        print(cur.rowcount,"record deleted")

#creating objects of the class Aadhar_Details:  
obj=Aadhar_Details()#object to make changes
obj2=Aadhar_Details()#object to display content
                                                              #Select from the options given below:
def mainmenu():
    while(True):
        print("\nPress 1 to check the entire aadhar record.")
        print("Press 2 to check records by name and ID number.")
        print("Press 3 to modify the rocords.")
        print("Press 4 to add a record.")
        print("Press 5 to delete a record.")
        print("Press 6 to exit!")
        Aadhar_choice=int(input("Enter your choice..."))

#To display the records:
        if Aadhar_choice==1:
            obj2.Display_List()
            
#To display records by name and aadhar number:
        elif Aadhar_choice==2:
            obj2.Details_by_Name()
            
#To edit the information:
        elif Aadhar_choice==3:
            print("\nHit 1 to edit the address.\nHit 2 to edit the name.\nHit 3 to edit the Date of Birth")
            update=int(input("Enter your choice"))
            
#To edit the address:
            if update==1:
                name=input("Enter the name to change the address")
                new_address=input("Enter the new address")
                obj.update_Address(new_address,name)

#To edit the name:
            elif update==2:
                old_name=input("Enter the name you want to change")
                new_name=input("Enter the new name")
                obj.update_Name(new_name,old_name)

#To edit the date-of-birth:
            elif update==3:
                Adhr_Num=int(input("Enter the 12 digit aadhar number to change the DOB"))
                input_data=input("Enter the updated date of birth in DD/MM/YY format")
                dob=obj.Date_of_Birth(input_data)
                if bool(dob)==True:
                    obj.update_DOB(dob, Adhr_Num)   
#To add a record:
        elif Aadhar_choice==4:
           input_data=(input("Enter the 12 digit aadhar number"))
           A_Num=obj.test_aadhar(input_data)
           string=str(A_Num)
           if(string!=input_data):
               print("INVALID ENTRY!")
               
           elif (string==input_data):                    
               info=input("Enter the Date-of-Birth (in DD/MM/YYYY) ") 
               dob=obj.Date_of_Birth(info)
               if bool(dob)==True:
                   Nm=input("Enter the name")
                   Adrs=input("Enter the address")
                   obj.add_Record(A_Num,Nm,dob,Adrs)
#To delete a record:
        elif Aadhar_choice==5:
              del_record=int(input("Enter the aadhar number to delete the record"))
              obj.delete(del_record)
#Existing the program:
        else:
              print("Exiting")
              break #forcefully terminate the program
mainmenu()
