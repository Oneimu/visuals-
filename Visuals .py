#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd


# In[46]:


hit_list = pd.read_csv(r"C:\Users\Blessing\Documents\Country.csv")
g = pd.read_csv(r"C:\Users\Blessing\Downloads\Uworld\countries.csv")


# In[172]:


region = pd.read_csv(r"C:\Users\Blessing\Downloads\Uworld\Region.csv")
region


# In[119]:


italy = pd.read_csv(r"C:\Users\Blessing\Documents\Itay.csv")
russia = pd.read_csv(r"C:\Users\Blessing\Documents\russia.csv")
brazil = pd.read_csv(r"C:\Users\Blessing\Documents\brazil.csv")
india = pd.read_csv(r"C:\Users\Blessing\Documents\India.csv")
uk = pd.read_csv(r"C:\Users\Blessing\Documents\UK.csv")
spain = pd.read_csv(r"C:\Users\Blessing\Documents\spain.csv")
us = pd.read_csv(r"C:\Users\Blessing\Documents\United_states.csv")


# In[ ]:





# In[264]:


#create plot_data function to plot the covid_cases
def plot_data(x):
    for i in x.Country.unique():
        name = i 
    title = f"{name} Coronavirus Cases Per_14days"
    plt.figure(figsize=(15,7))
    plt.plot( x.Date, x.cases_per_14days, 'r', marker='>')
    plt.title(title.upper(), size=18)
    plt.ylabel("Number of cases", size=18)
    plt.xlabel("Date", size=18)
    plt.savefig(r"C:\Users\Blessing\Downloads\Uworld"  + f"\\{name}.png" )

plot_data(spain)
plot_data(uk)
plot_data(us)
plot_data(italy)
plot_data(russia)
plot_data(india)
plot_data(brazil)


# In[ ]:





# In[126]:


def plot(x):
    for i in x.Country.unique():
        name = f'{i} COVID-19'
    title = f"{name} Deaths Per Week"
    plt.figure(figsize=(15,7))
    plt.plot(x.Date, x.deaths_per_14days, color= "black",marker=">")
    plt.title(title, size=18)
    plt.ylabel(name, size=18)
    plt.xlabel("Date", size=18)
    plt.savefig(r"C:\Users\Blessing\Downloads\Uworld"  + f"\\{name}.png" )
plot(us)


# In[ ]:





# In[156]:


#create a function that plots each country's covid cases
def covid_bar(x):
    for i in x.Country.unique():
        name = f'{i}'
    save_as = name + 'report'    
    fig = plt.figure(figsize=(12,7), dpi = 200)
    left, bottom, width, height = 0.1, 0.3, 0.8, 0.6
    ax = fig.add_axes([left, bottom, width, height])

    width = 0.45
    ticks = np.arange(len(x.Date))
    ax.bar(ticks, x.cases_per_14days, width, label = 'Corona cases', color='orange')
    ax.bar(ticks + width, x.deaths_per_14days, width, align = 'center', label = 'Deaths', color='black')
    ax.set_ylabel(f"victims of covid19".upper())
    ax.set_title(f'{name} COVID19_per_14days'.upper())
    ax.set_xticklabels(x.Date)
    plt.savefig(r"C:\Users\Blessing\Downloads\Uworld"  + f"\\{save_as}.png")
    ax.legend(loc='best')
#covid_bar(us)
#covid_bar(uk)
#covid_bar(italy)
#covid_bar(spain)
#covid_bar(russia)
#covid_bar(india)
covid_bar(brazil)


# In[174]:


region.head()


# In[250]:


plt.figure(figsize=(12,7))
rerun = 0
lists = []
for i in region:
    lists.append(i)

while rerun < len(lists):

    if rerun > 0:
        if rerun % 2 == 0 :
            #plt.figure(figsize=(15,7))
            plt.plot(region['Date'], region[lists[rerun]], marker=">", label = lists[rerun])
            plt.legend(loc='best')
            plt.title("Covid across 6 regions".upper(), size=18)
            plt.ylabel('Covid cases_per_14days', size=18)
            plt.xlabel("Date", size=18)
            plt.savefig(r"C:\Users\Blessing\Downloads\Uworld\c\region_cases.png" )


    rerun += 1


# In[262]:


plt.figure(figsize=(12,7))

lists = []
for i in region:
    lists.append(i)
rerun = 0    
while rerun < len(lists):

    if rerun > 1:
        if rerun % 2 != 0 :
            #plt.figure(figsize=(15,7))
            plt.plot(region['Date'], region[lists[rerun]], marker="*", label = lists[rerun])
            plt.legend(loc='best')
            plt.title("Covid across 6 regions".upper(), size=18)
            plt.ylabel('Covid deaths_per_14days', size=18)
            plt.xlabel("Date", size=18)
            plt.savefig(r"C:\Users\Blessing\Downloads\Uworld\c\region_deaths.png" )


    rerun += 1


# In[284]:


data = [13586963, 4592952, 443522, 1982146, 1078662, 513045]
regions = ['Americas', 'South-East Asia','Europe', 'Eastern Mediterranean', 'Africa', 'Western Pacific' ]


total = 0
label = []
#sum the data
for i in data:
    total += i

rerun = 0 
for i in regions:  
    percentage = round(data[rerun] / total * 100) 
    label.append(f"{i} {percentage}% ")
    rerun += 1    

plt.figure(figsize=(12, 7))
plt.title("COVID19 Cases (September 5th)")
plt.pie(data, labels = label, )
plt.savefig(r"C:\Users\Blessing\Downloads\Uworld\c\pie_covid.png" )


# In[299]:


covid_data = [7134546, 889682, 19144732]
names = ["Active Cases", "Deaths", "Recovered/Cured" ]
label_name = []
rerun = 0
for i in names:  
    percentage = round(covid_data[rerun] / sum(covid_data) * 100) 
    label_name.append(f"{i} {percentage}% ")
    rerun += 1    
plt.figure(figsize=(12, 7))
plt.title("Global COVID19 Report (Sept 5th)")    
plt.pie(covid_data, labels = label_name)
plt.savefig(r"C:\Users\Blessing\Downloads\Uworld\c\gobal_pie.png")


# In[297]:


covid_data[0] - covid_data[1] - covid_data[2]


# In[ ]:




