#!/usr/bin/env python
# coding: utf-8

# In[21]:


'''Run the class code and then execute signup for registration and then signin for login  written this code uusing jupyternotebook, class is in cell1, signup is in cell 2, sign in is in cell 3 and forgot password is in cell 3'''
class signup:
    def username(self, x):
        import re
        amprasand=str(re.search("\@",x))
        amprasand_Fullstop=str(re.search("\@.*\.",x))
        if amprasand!="None":
            if amprasand_Fullstop!="None":
                if amprasand_Fullstop!="@.":
                    if x[0] not in "1234567890" and x[0] not in"!@#$%^&*()":
                        return True
                    else:
                        print("username should not begin with numbers or special characters")#change it to invalid username
                else:
                    print("should not contain @.in username")#change it to invalid username
            else:
                print("username is not valid")#change it to invalid username
        else:
            print("@ missing")
    def password(self,y):
        import re
        import string
        special_char=string.punctuation
        uppercase=str(re.search("[A-Z]",y))
        lowercase=str(re.search("[a-z]",y))
        digits=str(re.search("[0-9]",y))
        specialChar=list(map(lambda char:char in special_char,y))
        if len(y)>5 and len(y)<16:
            if uppercase!="None" and lowercase!="None" and digits!="None" and any(specialChar):#checks if the code has any none string or has any special characters.
                    return True
            else:
                print("invalid password")
        else:
            print("lenth of password invalid") 
            
    def usernameExist(self,un):
        import pymongo
        from pymongo import MongoClient
        client=MongoClient("localhost", 27017)
        db=client.test1
        coll=db.users
        counter=0
        for each in coll.find({},{"_id":0}):
            if each["username"]==un:
                counter=0
                print("Username already exist")
                break
            else:
                counter=counter+1
        if counter!=0:
             return True 


#signup
username=input("Enter username:")
obj=signup()#initializing class object
if obj.username(username)==True:#calling class method & checking if username meets all the required conditions
    if obj.usernameExist(username)==True:#checking if email id exists in the system
        password=input("Enter password:")
        if obj.password(password)==True:#checking password
            data=[]#creating an empty list
            data.append({"username": username,"Password": password})#appending data to list
            coll.insert_many(data)#inserting data to MongoDB
            print("Registration successful")
        else:
            print("invalid password")

#signin 
un=input("Enter username:")
pas=input("Enter Password:")
c=0#actual counter
for i in coll.find({},{"_id":0}):
    if i=={'username':un, 'Password':pas}:#finds entered username and password is present in collection
        print("Login successfull")
        c=0
        break
    else:
        c=c+1
if c!=0:
    print("Wrong username of password")

#forgot passowrd
Username=input("Enter username:")
c=0
for i in coll.find({},{"_id":0}):
    if i["username"]==Username:
        print("password is", i["Password"])
        c=0
        break
    else:
        c=c+1
if c!=0:
    print("username do not exist, please register")
