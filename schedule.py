# -*- coding: utf-8 -*-
"""
Created on Sun May  3 23:14:41 2020

@author: sombanerjee
"""

import requests
import io
import pandas as pd
import re
import os
# intial URL to understand the revision number

start_date = 15
end_date = 21
month = 3
if month<10:
    string = '-'+str(0)+str(month)+'-'+str(2021)
else:
    string = "-"+str(month)+"-"+str(2021)
for i in range(start_date,end_date+1,1):

    a = i
    if i<=9:
        date = str('0')+str(a) + string
    else:
        date = str(a) + string

 


    headers = {
    'authority': 'wbes.erldc.in',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'content-type': 'application/json;charset=utf-8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://wbes.erldc.in/ReportNetSchedule/GetNetScheduleIndex',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; _gid=GA1.2.1706269973.1593603547; fileDownloadToken=1593625608984',
}

    params = (
    ('regionid', '1'),
    ('ScheduleDate', date),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/GetFullScheduleList', headers=headers, params=params)
    myfile = response.content
    
    rawdata = pd.read_csv(io.StringIO(myfile.decode('utf-8')))
    s1 = rawdata.columns
    a1 = re.findall("\d+",s1[0])
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wbes.erldc.in/ReportNetSchedule/GetFullScheduleList?regionid=1&ScheduleDate=26-06-2020', headers=headers)
    """
 #full schedule revision request
    cookies = {
        '_ga': 'GA1.2.383106581.1586066123',
        'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
        '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
        'fileDownloadToken': '1591031051711',
    }
    
    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://schedule.erldc.in/ReportNetSchedule/GetNetScheduleIndex',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }
    
    params = (
        ('regionid', '1'),
        ('ScheduleDate', date),
    )
    
    response = requests.get('https://schedule.erldc.in/ReportNetSchedule/GetFullScheduleList', headers=headers, params=params, cookies=cookies)

    
    myfile = response.content
    
    rawdata = pd.read_csv(io.StringIO(myfile.decode('utf-8')))
    s1 = rawdata.columns
    a1 = re.findall("\d+",s1[0])
   
    """
    #Net schedule csv download
    headers = {
    'authority': 'wbes.erldc.in',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportNetSchedule/GetNetScheduleIndex',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; _gid=GA1.2.1706269973.1593603547; fileDownloadToken=1593625608984',
}

    params = (
    ('scheduleDate', date),
    ('sellerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1593628430269'),
    ('fileType', 'csv'),
    ('regionId', '1'),
    ('byDetails', '1'),
    ('isBuyer', ['1', '1']),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/ExportNetScheduleSummaryToPDF', headers=headers, params=params)
      
    myfile = response
    filename = date + "_schedule.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\WEEK 150321-210321\WEEK 150321-210321\JSEB\schedule')
    open(filename, 'wb').write(myfile.content)
    
    
    
    
    
    """
    #ISGS schedule
    headers = {
    'authority': 'wbes.erldc.in',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportNetSchedule/GetNetSchDetailsIndex?regionId=1&scheduleDate=26-06-2020&sellerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=194&scheduleType=1&isJson=false',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; _gid=GA1.2.1706269973.1593603547; fileDownloadToken=1593628430269',
}

    params = (
    ('scheduleDate', date),
    ('sellerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1593628604359'),
    ('fileType', 'csv'),
    ('schType', '1'),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/ExportNetScheduleDetailToPDF', headers=headers, params=params)
   
    myfile = response
    filename = date + "_ISGS.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\0106_0706\New folder\JSEB\schedule1')
    open(filename, 'wb').write(myfile.content)
    
    #Wind schedule
    headers = {
    'authority': 'wbes.erldc.in',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportNetSchedule/GetNetSchDetailsIndex?regionId=1&scheduleDate=26-06-2020&sellerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=194&scheduleType=1&isJson=false',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; _gid=GA1.2.1706269973.1593603547; fileDownloadToken=1593628430269',
}

    params = (
    ('scheduleDate', date),
    ('sellerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1593628604359'),
    ('fileType', 'csv'),
    ('schType', '11'),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/ExportNetScheduleDetailToPDF', headers=headers, params=params)
   
    myfile = response
    filename = date + "_wind.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\0106_0706\New folder\JSEB\schedule1')
    open(filename, 'wb').write(myfile.content)
    
    #URS schedule
    headers = {
    'authority': 'wbes.erldc.in',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportNetSchedule/GetNetSchDetailsIndex?regionId=1&scheduleDate=26-06-2020&sellerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=194&scheduleType=1&isJson=false',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; _gid=GA1.2.1706269973.1593603547; fileDownloadToken=1593628430269',
}

    params = (
    ('scheduleDate', date),
    ('sellerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1593628604359'),
    ('fileType', 'csv'),
    ('schType', '8'),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/ExportNetScheduleDetailToPDF', headers=headers, params=params)
   
    myfile = response
    filename = date + "_URS.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\0106_0706\New folder\JSEB\schedule1')
    open(filename, 'wb').write(myfile.content)
    """