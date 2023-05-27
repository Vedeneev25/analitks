import psycopg2
import matplotlib.pyplot as plt
import pandas as pd
import queries as que
import tkinter as tk
from tkinter import *
from tkinter import ttk

conn = psycopg2.connect(dbname='Rent', user='postgres', 
                        password='1234', host='localhost', port = "5432")
cursor = conn.cursor()
# Топ 5 по виду деятельности по году, по месяцам

def query1(lima, date_year, start_date_mon, finish_date_mon):
    conn = psycopg2.connect(dbname='Rent', user='postgres', 
                        password='1234', host='localhost', port = "5432")
    cursor = conn.cursor()
    query1 = ("SELECT " + lima+ " , SUM(revenue) as rev FROM rent " +
               " where date_part('year', rent.date) = " + date_year + 
                " and date_part('month', rent.date) >= " + start_date_mon +
                " and date_part('month', rent.date) <= " +finish_date_mon +
                " group by " + lima + 
                " order by rev desc " +
                " limit 5" )
    cursor.execute(query1)
    record = cursor.fetchmany(size=5)
    cursor.close()
    conn.close()
    return record

def pie (lima, pokaz, date_year, start_date_mon, finish_date_mon):
    query1 =("select " + lima + "."+lima + " as " + lima + ", sum(rent." +pokaz + ") as " + pokaz + " from rent, " + lima +
             " where rent." + lima + "_id = " + lima + "." + lima + "_id")
    if date_year != "":
        query1 += (" and date_part('year', rent.date) = " + date_year)
    if start_date_mon != "":
        query1+= (" and date_part('month', rent.date) >= " + start_date_mon )
    if finish_date_mon != "":
        query1+= (" and date_part('month', rent.date) >= " + finish_date_mon )
    query1 +=(" group by " + lima + 
             " order by " + pokaz + " desc")
    #print(query1)
    cursor.execute( query1)
    record = cursor.fetchmany(size = 10)
    cursor.close()
    conn.close()
    return record



def cities():
    query = "SELECT city from city"
    cursor.execute(query)
    record = cursor.fetchmany(size=5)
    return record
