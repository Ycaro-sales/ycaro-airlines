from typing import Dict, List
from uuid import UUID
from random import randint
import peewee 
import models.accounts

db = peewee.SqliteDatabase("airlines.db")
db.create_tables([models.accounts.Account])

def main():

