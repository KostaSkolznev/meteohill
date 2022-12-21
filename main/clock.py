from django.shortcuts import render
import datetime

dateclock = datetime.datetime.today()

oclock = {
    'date': dateclock.date,
    'time': dateclock.time
    }