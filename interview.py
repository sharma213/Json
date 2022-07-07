import json



num=int(input("enter the input :"))
dict={}
dic={}
i=0
while i<num:
    user=input("enter the name :")
    user2=input("enter the state :")
    user3=int(input("enter the age :"))
    user4=int(input("enter the markes :"))
    dic['name']=user
    dic['state']=user2
    dic['age']=user3
    dic['marks']=user4
    i+=1
dict["details1"]=dic
dict["datails2"]=dic
print(dict)
with open("student.txt","w") as json.file:
    json.dump(dict,json.file,indent=4)