# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:16:04 2019

@author: VIJ Global
"""

import pymongo

clientUrl= "mongodb+srv://jessy:kakuma@kakuma-pspkr.mongodb.net/admin?retryWrites=true&w=majority"

client = pymongo.MongoClient(clientUrl)

client.database_names()

db = client.sample_training

db.collection_names()

collection = db.companies

example = collection.find_one()
