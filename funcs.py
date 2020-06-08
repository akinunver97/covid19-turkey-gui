import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.ticker as ticker
import numpy as np
from tkinter import *
country = ['Turkey']
df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
df = df[df['Country'].isin(country)]
df['Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis=1)


totald=df['Deaths'].iloc[-1]
totalr=df['Recovered'].iloc[-1]
numcase=df['Confirmed'].iloc[-1]




df1 = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv', parse_dates=['Date'])
df1 = df1[df1['Country'].isin(country)]
df1['Cases'] = df1[['Confirmed']].sum(axis=1)
df1 = df1.pivot(index='Date', columns='Country', values='Cases')
countries = list(df1.columns)
covid = df1.reset_index('Date')
covid.set_index(['Date'], inplace=True)
covid.columns = countries
populations = {'Turkey':86564517}
percapita = covid.copy()
for country in list(percapita.columns):
    percapita[country] = percapita[country]/populations[country]*100000



def death():
	df.plot(x='Date',y='Deaths',color='red')
	plt.show()

def recovered():
	df.plot(x='Date',y='Recovered',color='green')
	plt.show()

def cases():
	df.plot(x='Date',y='Confirmed',color='orange')
	plt.show()

def percapital():
	pcp = percapita.plot(figsize=(8,4.5), color='red', linewidth=5, legend=False)
	pcp.grid(color='#d4d4d4')
	pcp.set_xlabel('Date')
	pcp.set_ylabel('Number of Cases per 100.000 People')
	plt.show()

def aboutus():
	root =Tk()
	root.withdraw()
	messagebox.showinfo("About us","This is a Python Term Project made by three MIS students from FMV Isik University.This project visualize and analyze the disease called Covid-19.Name of those students are Akın, Mert, Altuğ and the instructor named as Dr.Engin Kandiran.")
