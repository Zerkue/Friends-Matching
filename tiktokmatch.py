import pandas as pd
import numpy as np

#Display all the columns
pd.set_option("display.max_columns", 100)

#Read in the data sheet named 'Tik_Tok.csv'
df = pd.read_csv ('Tik_Tok.csv')

#add a position column
df['Position'] = df.index.values + 1

#Rename the columns because the original names are too long to work with
# pc = preferred way of contact
# c = Contact
# PG = preferred gender

df.columns = ['Timestamp', 'Name', 'Age', 'Gender', 'PG', 'C', 'Email', 'Position']

#This code was not needed

Names = df['Name']
Ages = df['Age']
Genders = df['Gender']
GenderP = df['GP']
ContactP = df['PC']
ContactInfo = df['C']
Email = df['Email']
Position = df['Position']

class Player(object):
    def __init__(self,name, age, gender, genderp, contactway, contact, email, position):
        self.name = name
        self.age = age
        self.gender = gender
        self.genderp = genderp
        self.contactway = contactway
        self.contact = contact
        self.email = email
        self.position = position

for person in df:
    players = Player(Names, Ages, Genders, GenderP, ContactP, ContactInfo, Email, Position)


df_under_18 = df[df['Age'] < 18]

#Under 18 Male and Female filter
df_M_under_18 = df_under_18[df_under_18['Gender'] == 'Male']
df_F_under_18 = df_under_18[df_under_18['Gender'] == 'Female']


'''------------------------------Same Gender under 18-----------------------------'''

#Under 18 Males that prefer Males
df_M_under_18_PM = df_M_under_18[df_M_under_18['PG'] == 'Male']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_M_under_PM = {}
k = 0

while len(df_M_under_18_PM) > 1:

    df_M_under_18_PM.reset_index(drop=True, inplace=True)
    dic_M_under_PM["Match_M_under_PM{0}".format(k)] = df_M_under_18_PM.iloc[:2]

    df_M_under_18_PM.reset_index(drop=True, inplace=True)
    df_M_under_18_PM = df_M_under_18_PM.drop([df_M_under_18_PM.index[0], df_M_under_18_PM.index[1]])

    k += 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Under 18 females that Prefer Females
df_F_under_18_PF = df_F_under_18[df_F_under_18['PG'] == 'Female']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_F_under_PF = {}
k = 0
while len(df_F_under_18_PF) > 1:

    df_F_under_18_PF.reset_index(drop=True, inplace=True)
    dic_F_under_PF["Match_F_under_PF{0}".format(k)] = df_F_under_18_PF.iloc[:2]

    df_F_under_18_PF.reset_index(drop=True, inplace=True)
    df_F_under_18_PF = df_F_under_18_PF.drop([df_F_under_18_PF.index[0], df_F_under_18_PF.index[1]])

    k += 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


'''------------------------------Opposite Gender under 18-----------------------------'''

#Under 18 Males that prefer Females
df_M_under_18_PF = df_M_under_18[df_M_under_18['PG'] == 'Female']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Under 18 Females that prefer Males
df_F_under_18_PM = df_F_under_18[df_F_under_18['PG'] == 'Male']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_MF_under_PFM = {}
k = 0
while len(df_M_under_18_PF) > 1 and len(df_F_under_18_PM) > 1:
    df_M_under_18_PF.reset_index(drop=True, inplace=True)
    df_F_under_18_PM.reset_index(drop=True, inplace=True)

    dic_MF_under_PFM["Match_MF_under_PFM{0}".format(k)] = [df_M_under_18_PF.iloc[:1], df_F_under_18_PM.iloc[:1]]

    df_M_under_18_PF.reset_index(drop=True, inplace=True)
    df_F_under_18_PM.reset_index(drop=True, inplace=True)

    df_M_under_18_PF = df_M_under_18_PF.drop([df_M_under_18_PF.index[0]])
    df_F_under_18_PM = df_F_under_18_PM.drop([df_F_under_18_PM.index[0]])

    k += 1

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


'''-----------------------------------Either under 18-------------------------------------------'''


df_E_under_18_PE = df_under_18[df_under_18['PG'] == 'Either']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_E_under_PE = {}
k = 0

while len(df_E_under_18_PE) > 1:

    df_E_under_18_PE.reset_index(drop=True, inplace=True)
    dic_E_under_PE["Match_E_under_PE{0}".format(k)] = df_E_under_18_PE.iloc[:2]

    df_E_under_18_PE.reset_index(drop=True, inplace=True)
    df_E_under_18_PE = df_E_under_18_PE.drop([df_E_under_18_PE.index[0], df_E_under_18_PE.index[1]])

    k += 1

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
df_over_18 = df[df['Age'] > 18]

#Over 18 Male and Female filter
df_M_over_18 = df_over_18[df_over_18['Gender'] == 'Male']
df_F_over_18 = df_over_18[df_over_18['Gender'] == 'Female']


'''------------------------------Same Gender over 18-----------------------------'''

#over 18 Males that prefer Males
df_M_over_18_PM = df_M_over_18[df_M_over_18['PG'] == 'Male']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_M_over_PM = {}
k = 0

while len(df_M_over_18_PM) > 1:
    df_M_over_18_PM.reset_index(drop=True, inplace=True)
    dic_M_over_PM["Match_M_over_PM{0}".format(k)] = df_M_over_18_PM.iloc[:2]

    df_M_over_18_PM.reset_index(drop=True, inplace=True)
    df_M_over_18_PM = df_M_over_18_PM.drop([df_M_over_18_PM.index[0], df_M_over_18_PM.index[1]])

    k += 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#over 18 females that Prefer Females
df_F_over_18_PF = df_F_over_18[df_F_over_18['PG'] == 'Female']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_F_over_PF = {}
k = 0
while len(df_F_over_18_PF) > 1:

    df_F_over_18_PF.reset_index(drop=True, inplace=True)
    dic_F_over_PF["Match_F_over_PF{0}".format(k)] = df_F_over_18_PF.iloc[:2]

    df_F_over_18_PF.reset_index(drop=True, inplace=True)
    df_Fover_188_PF = df_F_over_18_PF.drop([df_F_over_18_PF.index[0], df_F_over_18_PF.index[1]])

    k += 1
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


'''------------------------------Opposite Gender over 18-----------------------------'''

#over 18 Males that prefer Females
df_M_over_18_PF = df_M_over_18[df_M_over_18['PG'] == 'Female']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#over 18 Females that prefer Males
df_F_over_18_PM = df_F_over_18[df_F_over_18['PG'] == 'Male']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_F_over_PM = {}
k = 0
while len(df_M_over_18_PF) > 1 and len(df_F_over_18_PM) > 1:
    df_M_over_18_PF.reset_index(drop=True, inplace=True)
    df_F_over_18_PM.reset_index(drop=True, inplace=True)

    dic_F_over_PM["Match_MF_over_PFM{0}".format(k)] = [df_M_over_18_PF.iloc[:1], df_F_over_18_PM.iloc[:1]]

    df_M_over_18_PF.reset_index(drop=True, inplace=True)
    df_F_over_18_PM.reset_index(drop=True, inplace=True)

    df_M_over_18_PF = df_M_over_18_PF.drop([df_M_over_18_PF.index[0]])
    df_F_over_18_PM = df_F_over_18_PM.drop([df_F_over_18_PM.index[0]])

    k += 1

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


'''-----------------------------------Either over 18-------------------------------------------'''


df_E_over_18_PE = df_over_18[df_over_18['PG'] == 'Either']
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
dic_E_over_PE = {}
k = 0

while len(df_E_over_18_PE) > 1:

    df_E_over_18_PE.reset_index(drop=True, inplace=True)
    dic_E_over_PE["Match_E_over_PE{0}".format(k)] = df_E_over_18_PE.iloc[:2]

    df_E_over_18_PE.reset_index(drop=True, inplace=True)
    df_E_over_18_PE = df_E_over_18_PE.drop([df_E_over_18_PE.index[0], df_E_over_18_PE.index[1]])

    k += 1

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print(dic_M_under_PM)
print(dic_F_under_PF)
print(dic_MF_under_PFM)
print(dic_E_under_PE)


print(dic_M_over_PM)
print(dic_F_over_PF)
#print(dic_MF_over_PFM)
print(dic_E_over_PE)


