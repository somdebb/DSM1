# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:19:57 2020

@author: sombanerjee
"""

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
from requests.exceptions import ConnectionError
# intial URL to understand the revision number

start_date = 1
end_date = 12
month = 11
os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\Nov Schedule')

if month<10:
    string = '-'+str(0)+str(month)+'-'+str(2020)
else:
    string = "-"+str(month)+"-"+str(2020)
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
 
    
    """
    #ISGS full schedule
    headers = {
    'authority': 'wbes.erldc.in',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=20-06-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=198&scheduleType=1&schTitle=klkklk',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; fileDownloadToken=1595444543369',
}

    params = (
    ('scheduleDate', date),
    ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1595493405571'),
    ('fileType', 'csv'),
    ('schType', '1'),
)

    response = requests.get('https://wbes.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params)
   
    myfile = response
    filename = date + "_ISGS.csv"
    
    open(filename, 'wb' ).write(myfile.content)
    
    #ISGS NET schedule
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
    filename = date + "_ISGS_net.csv"
    #os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\jun schedule')
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
   # os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\jun schedule')
    open(filename, 'wb').write(myfile.content)
   
       
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
    #os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\jun schedule')
    open(filename, 'wb').write(myfile.content)
    
    # URS full schedule
    try:
        headers = {
    'authority': 'wbes.erldc.in',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://wbes.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=20-06-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=198&scheduleType=8&schTitle=klkklk',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cookie': '_ga=GA1.2.383106581.1586066123; ASP.NET_SessionId=wbxqfpnt43yjti0bfu1k0h1l; __RequestVerificationToken=OMUUwlNPO4_3bl8TZw597tuNsKiN1ih5Hx1wHWLREto-xZFoh1qieeuTiB66XPuSXZy2cJ_O2TqWrDCs3cQUkHFR9lEzQiu2Aw1AgMv9EVY1; fileDownloadToken=1595493405571',
}

        params = (
    ('scheduleDate', date),
    ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1595571548814'),
    ('fileType', 'csv'),
    ('schType', '8'),
)

        response = requests.get('https://wbes.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params)
        myfile = response
        filename = date + "_URS.csv"
       # os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\jun schedule')
        open(filename, 'wb').write(myfile.content)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://wbes.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF?scheduleDate=20-06-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=198&getTokenValue=1595571548814&fileType=csv&schType=8', headers=headers)
    except ConnectionError:
        pass
    
    #STOA schedule
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
    ('schType', '3'),
)

    response = requests.get('https://wbes.erldc.in/ReportNetSchedule/ExportNetScheduleDetailToPDF', headers=headers, params=params)
   
    myfile = response
    filename = date + "_STOA.csv"
    #os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\jun schedule')
    open(filename, 'wb').write(myfile.content)
    
    
    