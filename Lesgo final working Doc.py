#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib as mp

get_ipython().system('pip install pypdf')


# In[2]:


from pypdf import PdfReader


# In[3]:


reader=PdfReader(r"C:\Users\Adhikansh\Downloads\Minutes_135_IPPC_140_IUPC.pdf")

# print(len(reader.pages))


# In[4]:


page=reader.pages[10]
text=page.extract_text()


# In[5]:


# print(text)


# In[6]:


text=text.split("\n")


# In[ ]:





# In[7]:


for i in text:
    i=i.split(" ")
# print(text)


# In[ ]:





# In[ ]:





# In[8]:


for i in text:
    i = i.strip().split("\n")

# Extract headers (second line)
header = text[1].split()

# Process rows
rows = []
for line in text[1:]:
    line=line.split(" ")
    
    



# In[9]:


papa = []

# Assuming `text` is a list of lines
for line in text:
    grades = []
    name = []

    # Split the line into individual parts
    parts = line.split()

    # Check if the line has enough parts to process
    if len(parts) < 3:
        continue  # Skip lines with insufficient data

    # Extract initial grades (assuming `parts[1]` and `parts[2]` are grades)
    grades.append(parts[1])
    grades.append(parts[2])

    # Start iterating from the 4th element (index 3) to extract grades and names
    for i in range(3, len(parts) - 3):
        if parts[i].isdigit():
            grades.append(int(parts[i]))
        else:
            name.append(parts[i])

    # Append the name and grades to `papa`
    papa.append(name)
    papa.append(grades)

# Print the result
# print("Parsed Data:")
# for entry in papa:
#     print(entry)


# In[10]:


papa = []

# Loop through pages starting from page 6
for i in range(6, len(reader.pages)):
    pagee = reader.pages[i]
    textt = pagee.extract_text()
    textt = textt.split("\n")  # Split text into lines

    # Process each line on the page
    for line in textt:
        grades = []
        name = []
        
        

        # Split the line into individual parts
        parts = line.split(" ")
        
        if(len(parts)<3):
            continue
        
        grades.append(parts[1]+" " +parts[2])
        

        # Start iterating from the 4th element (index 3)
        for j in range(3, len(parts) - 3):
            # Check if the part is numeric (grade)
            if len(parts[j]) == 0:
                grades.append(0)
            elif parts[j].isdigit():
                grades.append(int(parts[j]))
            else:
                name.append(parts[j])

        # Append the name and grades to `papa`
        papa.append(name)
        papa.append(grades)

# Print the result
# print("Parsed Data:")
# for entry in papa:
#     print(entry)


# In[14]:


import matplotlib.pyplot as plt

hehe=input("type")
for i in papa:
    if len(i)>=1:
        if i[0]==hehe:
            arr=[]
            for num in range(1,15):
                arr.append(i[num])
            
print(arr)

print(hehe)



gra=['AS' ,'AA', 'AB' ,'BB' ,'BC', 'CC' ,'CD', 'DD', 'FA', 'FD', 'FP', 'I','B','C']



plt.bar(gra,arr, color='violet')
plt.title('Grades')
for index, value in enumerate(arr):
        plt.text(index, value, str(value), ha='center', va='bottom') 
plt.xlabel('Grade Awarded')
plt.ylabel('Number of Students')
plt.show()




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




