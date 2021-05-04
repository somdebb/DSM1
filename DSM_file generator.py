# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 22:29:14 2020

@author: sombanerjee
"""

import pandas as pd
import os



my_cols = [str(j) for j in range(35)]
#frequency_code = pd.read_excel(r"C:\Users\sombanerjee\Documents\power purchase MIS\2303_2903\New folder\JSEB\frequency.csv")
#code = frequency_code.to_dict()
temp = pd.DataFrame()
frequency = pd.DataFrame()
path_original = r"C:\Users\sombanerjee\Documents\power purchase MIS"
#os.chdir(r"C:\Users\sombanerjee\Documents\power purchase MIS\WEEK 140920-200920\WEEK 140920-200920\JSEB")
start_date = 15
end_date = 21
month = 4
if month <= 9:
    file_string = str(0)+str(month)
else:
    file_string = str(month)
if start_date<=9:
    start_date1 = str("0")+ str(start_date)
else: 
    start_date1 = str(start_date)
if end_date <=9:
    end_date1 = str("0") + str(end_date)
else: 
    end_date1 = str(end_date)
folder_name = 'WEEK '+str(start_date1)+file_string+str('21')+"-"+str(end_date1)+file_string+str('21')
destination_folder1 = os.path.join(path_original,folder_name,folder_name,"JSEB")
os.chdir(destination_folder1)
for i in range (start_date,end_date+1,1):
    a = i
    if i<10:
        file = str('0')+str(a) + file_string+"21.JSB"
    else:
        file = str(a) + file_string+"21.JSB"
    df1 =pd.read_csv(file,header = None, sep = "\s+|\t+|\s+\t+|\t+\s+", names = my_cols, engine = "python")
    #column_name = str('0') + str(a)+ str('0320')
    column_name = str(a)+ str(file_string)
    temp[column_name] = df1.iloc[6:102,-3].astype(float)*-4
    column_name =  str(a)+ str(file_string)+ "_f"
    frequency[column_name] = df1.iloc[:,1]
temp_reverse = temp[temp.columns[::-1]]
consumption_filename = str(start_date)+"_"+ str(end_date)+"consumption.csv"
temp_reverse.to_csv(consumption_filename)
#frequency1 = pd.merge(frequency,frequency_code, on = '')
frequency_reverse = frequency[frequency.columns[::-1]]
frequency_filename = str(start_date)+"_"+ str(end_date)+"frequency.csv"
frequency_reverse.iloc[6:102,:].to_csv(frequency_filename)

destination_folder2 = os.path.join(path_original,folder_name,folder_name,"JSEB","schedule")
#dir1 = r"C:\Users\sombanerjee\Documents\power purchase MIS\WEEK 070920-130920\WEEK 070920-130920\JSEB\schedule"
dir1 = destination_folder2
temp1 = pd.DataFrame()

for j in range (start_date,end_date+1,1) :
     #a = j+1
     a =j
     if j<9:
        substring = str('0')+str(a)+"-"+ file_string+"-2021"
     else:
        substring = str(a) + "-"+file_string+"-2021"
       
     for root, subdirs,files  in os.walk(dir1):
        for filename in files:
            if substring in filename:
                name_path2 = os.path.join(root,filename)
     column_name1 = substring
     df_schedule = pd.read_csv(name_path2, encoding= 'UTF-16 LE', header = 0)
     temp1[column_name1] = df_schedule['Net Total']
     

temp1_reverse = temp1[temp1.columns[::-1]].iloc[0:96,:]
schedule_filename = str(start_date)+"_"+ str(end_date)+"schedule.csv"
temp1_reverse.to_csv(schedule_filename)