# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:57:07 2020

@author: sombanerjee
"""

import requests
import io
import pandas as pd
import re
import os
from requests.exceptions import ConnectionError
# intial URL to understand the revision number

for i in range(1,30,1):

    a = i
    if i<=9:
        date = str('0')+str(a) + "-02-2020"
    else:
        date = str(a) + "-02-2020"
        
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
    
    
    cookies = {
    '_ga': 'GA1.2.383106581.1586066123',
    'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
    '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
}

    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://schedule.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=05-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=208&scheduleType=3&schTitle=klkklk',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

    params = (
    ('scheduleDate', date),
    ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1594063599014'),
    ('fileType', 'csv'),
    ('schType', '3'),
)

    response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF?scheduleDate=05-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=208&getTokenValue=1594063599014&fileType=csv&schType=3', headers=headers, cookies=cookies)
    myfile = response
    filename = date + "_APNRL.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\feb schedule')
    open(filename, 'wb').write(myfile.content)
    
    cookies = {
    '_ga': 'GA1.2.383106581.1586066123',
    'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
    '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
    'fileDownloadToken': '1594063599014',
}

    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://schedule.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=04-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=205&scheduleType=1&schTitle=klkklk',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

    params = (
    ('scheduleDate', date),
    ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1594066469396'),
    ('fileType', 'csv'),
    ('schType', '1'),
)

    response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF?scheduleDate=04-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=205&getTokenValue=1594066469396&fileType=csv&schType=1', headers=headers, cookies=cookies)
    myfile = response
    filename = date + "_ISGS.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\feb schedule')
    open(filename, 'wb').write(myfile.content)
    try:
        cookies = {
        '_ga': 'GA1.2.383106581.1586066123',
        'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
        '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
        'fileDownloadToken': '1594066469396',
    }
    
        headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://schedule.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=04-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=205&scheduleType=8&schTitle=klkklk',
        'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    }
    
        params = (
        ('scheduleDate', date),
        ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
        ('revisionNumber', a1[0]),
        ('getTokenValue', '1594235401205'),
        ('fileType', 'csv'),
        ('schType', '8'),
    )
    
        response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params, cookies=cookies)
  
        
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF?scheduleDate=04-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=205&getTokenValue=1594235401205&fileType=csv&schType=8', headers=headers, cookies=cookies)
        myfile = response
        filename = date + "_URS.csv"
        os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\feb schedule')
        open(filename, 'wb').write(myfile.content)
    except ConnectionError:
          pass
    cookies = {
    '_ga': 'GA1.2.383106581.1586066123',
    'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
    '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
    'fileDownloadToken': '1594236142328',
}

    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://schedule.erldc.in/ReportFullSchedule/GetFullDrawalDetailsIndex?regionId=1&scheduleDate=05-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=208&scheduleType=4&schTitle=klkklk',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

    params = (
    ('scheduleDate', date),
    ('buyerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1594238069643'),
    ('fileType', 'csv'),
    ('schType', '4'),
)

    response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://schedule.erldc.in/ReportFullSchedule/ExportFullScheduleDrawalDetailToPDF?scheduleDate=05-02-2020&buyerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=208&getTokenValue=1594238069643&fileType=csv&schType=4', headers=headers, cookies=cookies)
    myfile = response
    filename = date + "_LTA.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\feb schedule')
    open(filename, 'wb').write(myfile.content)
    
    cookies = {
    '_ga': 'GA1.2.383106581.1586066123',
    'ASP.NET_SessionId': 'dgvstuyrikf04rtkbrjxr33t',
    '__RequestVerificationToken': 'KOt9JRt4FeC7EBm3r_ueey-s2TGE2aDlp_-3iT3Z41DhUEMckiKvbqDj_0OEH1we9h0KqSVh54w1xYQTKlGtEoWtNvgMh7ixXLqZwN_ZX1I1',
    '_gid': 'GA1.2.54755704.1594315076',
}

    headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://schedule.erldc.in/ReportNetSchedule/GetNetScheduleIndex',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
}

    params = (
    ('scheduleDate', date),
    ('sellerId', 'b7637616-a238-4737-b813-22d9336bfcb2'),
    ('revisionNumber', a1[0]),
    ('getTokenValue', '1594318070057'),
    ('fileType', 'csv'),
    ('regionId', '1'),
    ('byDetails', '1'),
    ('isBuyer', ['1', '1']),
)

    response = requests.get('https://schedule.erldc.in/ReportNetSchedule/ExportNetScheduleSummaryToPDF', headers=headers, params=params, cookies=cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://schedule.erldc.in/ReportNetSchedule/ExportNetScheduleSummaryToPDF?scheduleDate=29-02-2020&sellerId=b7637616-a238-4737-b813-22d9336bfcb2&revisionNumber=199&getTokenValue=1594318070057&fileType=csv&regionId=1&byDetails=1&isBuyer=1&isBuyer=1', headers=headers, cookies=cookies)

    myfile = response
    filename = date + "_total.csv"
    os.chdir(r'C:\Users\sombanerjee\Documents\power purchase MIS\feb schedule')
    open(filename, 'wb').write(myfile.content)
