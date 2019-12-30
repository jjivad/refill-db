# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 12:32:26 2019

@author: VIJ Global
"""
import mongoengine
from pymongo import MongoClient

#server cration and linking
server_sir = MongoClient('localhost', 27017)
#print(server_try1)
sir_db = server_sir.sir_db1
#print(sir_db)
students_col = sir_db.students
#print(students_col)

##function to store input: student data record
def my_student():
  names = str(input('enter student names: '))
  location = str(input('enter student location: '))
  contact = str(input('enter student contact: '))
  nationality = str(input('enter student nationality: '))
  age = str(input('enter student age: '))
  indNum = str(input('enter student individual number: '))
  course = str(input('course registered : '))
  a = names
  b = location
  c = contact
  d = nationality
  e = age
  f = indNum
  g = course
  return {'std_names':a, 'std_location': b,'std_contact': c, 'std_nationality': d, 'std_age': e, 'str_indNum': f, 'std_course': g}

## this function is for accepting if the admin want to resgister or not
def adm_ans(): 
  print('')
  print("Do you want to register a student? ")
  answer = str(input("enter 'y' to record new student or 'n' to stop the program: "))
  return answer

## to record and insert student data in the data base
def std_add():
  std_dic = my_student() # passing the returning dictionary into this variable
  std = students_col.insert_one(std_dic) # adding the dictionary values into the collection
  if std.acknowledged:
    print('')
    print('student has been added to your database. student ID is: ', std.inserted_id)
#    adm_ans()
  else:
    print('')
    print('this student was not added to your database, try later')
#    adm_ans()
    
# the loop to regirster or stop the registration  
while True:
  ans = adm_ans() #storing the admin's answer 
  if ans == 'y' or ans == 'yes':
    std_add()
   
  elif ans == 'n' or ans == 'no':
    print('')
    print("the program will be closed, are you sure you don't want to record more student? ")
    confirm = str(input("enter 'y' to record new student or 'n' to stop the program: "))
    if confirm == 'y' or confirm == 'yes':
      std_add()
    else:
      break
  else:
    print('')
    print("your input is not correct, retry")
#    adm_ans()




























    