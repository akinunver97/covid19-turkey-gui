from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from funcs import *
import datetime as dt
import time


root = Tk()
root.title("Stay Home, Stay Safe")
bgcolor="#fce8d5"
root.resizable(width=False, height=False)
root.configure(background=bgcolor)
root.geometry("870x400")

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label='About Us', command=aboutus)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='Menu',menu=filemenu)
root.config(menu=menubar)


top= Label(root, text="Covid-19 Data of Turkey",pady=5,padx=200,font=("Calibri",36),bg=bgcolor).grid(row=1,column=1,columnspan=4)
sh=Label(root, text="Stay Home, Stay Safe",pady=10,font=("Arial",18),bg=bgcolor).grid(row=2,column=1,columnspan=4)
sd=Label(root, text="Source data: https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv ",
font=("Arial",8),pady=10,bg=bgcolor,fg="gray").grid(row=3,column=1,columnspan=4)


b1= Button(root, text="Number of cases", pady=10,command=cases).grid(row=4,column=1)
b2= Button(root, text="Number of recovered",pady=10, command=recovered).grid(row=4,column=2)
b3= Button(root, text="Number of death", pady=10,command=death).grid(row=4,column=3)
b4= Button(root, text="Case per 100.000 people", pady=10,command=percapital).grid(row=4,column=4)

clock = Label(root,pady=10, text=f"{dt.datetime.now(): %d %b %Y}", fg="black", bg=bgcolor, font=("helvetica", 24)).grid(row=5,column=1,columnspan=4)


l1= Label(root,bg=bgcolor, text="Number of cases:",font=("Calibri",15)).grid(row=6,column=2)
l11= Label(root, text=numcase,font=("Calibri",15),bg=bgcolor).grid(row=6,column=3)

l2= Label(root, bg=bgcolor,text="Total recovered:",pady=5,font=("Calibri",15)).grid(row=7,column=2)
l22= Label(root, bg=bgcolor,text=totalr,font=("Calibri",15)).grid(row=7,column=3)

l3= Label(root, bg=bgcolor,text="Total death:",pady=5,font=("Calibri",15)).grid(row=8,column=2)
l33= Label(root, bg=bgcolor,text=totald,font=("Calibri",15)).grid(row=8,column=3)

root.mainloop()

