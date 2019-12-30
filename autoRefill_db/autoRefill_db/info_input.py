# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:16:04 2019

@author: VIJ Global
"""

import pymongo

clientUrl= "mongodb+srv://jessy:kakuma@kakuma-pspkr.mongodb.net/admin?retryWrites=true&w=majority"

client = pymongo.MongoClient(clientUrl)

client.list_database_names()

db = client.sample_training

db.list_collection_names()

collection = db.companies

example = collection.find_one()



#organization = "SIR center"
#
#def my_info(name, contact, course, cohort):  
#  print(" ")
#  print(name)
#  print(contact)
#  print(course)
#  print(cohort)
#  
#name_full = input("Please, provide your names: ")
#age = input("Please, indicate your age: ")
#gender = input("Please, indicate your gender: ")
#  
#nationality = input("Please, provide your nationality: ")
#ind_number = input("Please, provide your individual number: ")
#tel_number = input("Please, share your telephone number: ")
#  
#course_taken = input("Which course would like to study at " + organization + "? ")
#course_level = input("Which level (basic or adavanced)? ")
#  
#month_starting = input("When are you starting? ")
#month_ending = input("When will you finish? ")
#cohort_num = input("In which cohort are you? ")
#
#name_info = name_full
#age_info = age
#gender_info = gender
#nation_info = nationality
#id_info = ind_number
#tel_info = tel_number
#course_info = course_taken
#level_info = course_level
#start_info = month_starting
#end_info = month_ending
#cohort_info = cohort_num
#
##for the input values ... to be retained
#a = name_info + " is " + str(age_info)+ ", " + gender_info
#b = nation_info + ", " + str(id_info)+ ", " + str(tel_info)
#c = course_info + ", " + level_info
#d = start_info + ", " + end_info+ ", " + cohort_info
#
##print(name_info)
#print(my_info(a, b, c, d))