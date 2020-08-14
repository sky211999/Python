# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy
data = pandas.read_csv('ool_pds.csv', low_memory=False)
print(len(data)) #Number of Observations(Rows)
print(len(data.columns)) #Number of Variables(Columns)

#Creating a subsetted data with Age cap
sub1=data[(data['PPAGE']>=18) & (data['PPAGE']<=25)]

#make a copy of my new subsetted data
sub2 = sub1.copy()

#counts and percentages (i.e. frequency distributions) for each variable
print("\nThe count of the people who voted Yes:1 \n")
c1 = sub2['W1_A4'].value_counts(sort=False, dropna=True)
print(c1)

print("\nThe percentage of the people who voted Yes:1 \n")
p1 = sub2['W1_A4'].value_counts(sort=False, normalize=True)
print(p1)

print("\nThe count of votes to \n 1: John McCain \n 2: Barack Obama \n 3: Others \n")
c2 = sub2['W1_A5A'].value_counts(sort=False, dropna=True).sort_index()
print(c2)

print("\nThe percentage of votes to \n 1: John McCain \n 2: Barack Obama \n 3: Others \n")
p2 = sub2['W1_A5A'].value_counts(sort=False, normalize=True).sort_index()
print(p2)

print("\nThe count of non-voters support to \n 1: John McCain \n 2: Barack Obama \n 3: Others \n 4: NOTA \n")
c3 = sub2['W1_A5B'].value_counts(sort=False, dropna=True).sort_index()
print(c3)

print("\nThe percentage of non-voters support to \n 1: John McCain \n 2: Barack Obama \n 3: Others \n 4: NOTA \n")
p3 = sub2['W1_A5B'].value_counts(sort=False, normalize=True).sort_index()
print(p3)

print("\nThe count of voters based on ethincity \n 1: White \n 2: Black \n 3: Others \n 4: Hispanic \n 5:2+ races Non Hispanic \n")
c4 = sub2['PPETHM'].value_counts(sort=False, dropna=True)
print(c4)

print("\nThe percentage of voters based on ethincity \n 1: White \n 2: Black \n 3: Others \n 4: Hispanic \n 5:2+ races Non Hispanic \n")
p4 = sub2['PPETHM'].value_counts(sort=False, normalize=True)
print(p4)

print("\nThe count of voters based on religion \n 1:Baptist any denomination \n 2:Protestant (e.g., Methodist, Lutheran, Presbyterian, Episcopal) \n 3 Catholic \n 4 Mormon \n 5 Jewish \n 6 Muslim \n 7 Hindu \n 8 Buddhist \n 9 Pentecostal \n 10 Eastern Orthodox \n 11 Other Christian \n 12 Other non-Christian, please specify: \n 13 None \n")
c5 = sub2['PPETHM'].value_counts(sort=False, dropna=True)
print(c5)

print("\nThe percentage of voters based on religion \n 1:Baptist any denomination \n 2:Protestant (e.g., Methodist, Lutheran, Presbyterian, Episcopal) \n 3 Catholic \n 4 Mormon \n 5 Jewish \n 6 Muslim \n 7 Hindu \n 8 Buddhist \n 9 Pentecostal \n 10 Eastern Orthodox \n 11 Other Christian \n 12 Other non-Christian, please specify: \n 13 None \n")
p5 = sub2['PPETHM'].value_counts(sort=False, normalize=True)
print(p5)