# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:50:59 2019

@author: VIJ Global
"""
import mongoengine
from pymongo import MongoClient

#clientUrl= "mongodb+srv://jessy:kakuma@kakuma-pspkr.mongodb.net/admin?retryWrites=true&w=majority"
#
#client1 = MongoClient()
#client2 = MongoClient(clientUrl)
#
##print(client1)
##print("")
##print(client2)
#
#def global_init():
#  mongoengine.register_connection(alias='core', name='snake_bnb')


server_try1 = MongoClient('localhost', 27017)
#print(server_try1)
my_db_sir = server_try1.sir_db
#print(my_db_sir)
students = my_db_sir.students
#print(students)
students_dic ={
    'std_names' : 'Jessy Inga',
    'std_contact' : '0758212077',
    'std_location': 'k4 z2 b3',
    'std_nationality' : 'Congolese',
    'std_age' : '25',
    'std_course' : 'Computer Basic',
    'str_indNum' : '845-00277137'
    }
#print(students_dic)
#std1 = students.insert_one(students_dic)
##print(std1)
#if std1.acknowledged:
#  print('student has been added to your database. student ID is: ', std1.inserted_id)

#input from the admin/students
#names = str(input('enter student names: '))
#location = str(input('enter student location: '))
#contact = str(input('enter student contact: '))
#nationality = str(input('enter student nationality: '))
#age = str(input('enter student age: '))
#indNum = str(input('enter student individual number: '))
#course = str(input('course registered : '))


#function to store input
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

#std_list = my_student()
#print(std_list)
#print(type(std_list))
#for i in range (len(std_list)):
#  my_dic = {
#      'names': std_list[i]
#      'location' : i
#      }

































