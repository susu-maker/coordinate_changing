# 84轉97
import requests
from bs4 import BeautifulSoup
import pandas as pd
import chardet
import numpy as np
import matplotlib.pyplot as plt

def get_twd97(lng, lat):
    url = "http://gis.thl.ncku.edu.tw/coordtrans/coordtrans.aspx"
    headers = {
        "Upgrade-Insecure-Requests":"1",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    }
    data = {
        "BUTTON1":"轉換",
        "CoordFormat":3,
        "CoordValue":str(lng)+','+str(lat),
        "__EVENTVALIDATION":"/wEWBwLlxrnMAwKyy4GNBwKzy4GNBwKwy4GNBwKxy4GNBwL5muahDAKMm5KEDaYjgdhgAGJ5Ne1L7rPtx+ycuzC/",
        "__VIEWSTATE":"/wEPDwUKMTA0MDk3Njk0Mg9kFgICAQ9kFgICBw8PFgIeBFRleHQFkQNUV0Q2N+e2k+e3r+W6puWdkOaomeWAvCA644CA44CA44CAIOOAgDxiPjEyMDowODoyMS4xMTQwMCwgMjM6MDM6MTAuMTE1MDA8c21hbGw+ICgxMjAuMTM5MTk4MzMzMzMzLDIzLjA1MjgwOTcyMjIyMjIpPC9zbWFsbD48L2I+PGJyPlRXRDY35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8IDrjgIDjgIAg44CAPGI+MTYxNzg4Ljk4NSwgMjU1MDM5OS4yMjA8L2I+PGJyPlRXRDk3KFdHUzg0Kee2k+e3r+W6puWdkOaomeWAvCA6IDxiPjEyMDowODo1MC4xOTIyMCwgMjM6MDM6MDMuNzk2MjQ8c21hbGw+ICgxMjAuMTQ3Mjc1NjExMzcyLDIzLjA1MTA1NDUxMDI2NjMpPC9zbWFsbD48L2I+PGJyPlRXRDk35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8IDrjgIAg44CA44CAPGI+MTYyNjE1LjkzNCwgMjU1MDE5MS4xODI8L2I+PGJyPmRkZG/sibbFSPm1K+nXL2AG/J+PInJM",
        "__VIEWSTATEGENERATOR":"F862B26F"
    }
    res = requests.post(url, headers = headers, data=data)
    soup = BeautifulSoup(res.text, 'html.parser')
    axis = soup.find("span", id="Message").find_all('b')[3].string.split(',')
    print(axis)
    return [float(axis[1]), float(axis[0])]

#97轉84
def get_wgs84(x, y):
    url = "http://gis.thl.ncku.edu.tw/coordtrans/coordtrans.aspx"
    headers = {
        "Upgrade-Insecure-Requests":"1",
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    }
    data = {
        "BUTTON1":"轉換",
        "CoordFormat":4,
        "CoordValue":str(x)+','+str(y),
        "__EVENTVALIDATION":"/wEWBwLlxrnMAwKyy4GNBwKzy4GNBwKwy4GNBwKxy4GNBwL5muahDAKMm5KEDaYjgdhgAGJ5Ne1L7rPtx+ycuzC/",
        "__VIEWSTATE":"/wEPDwUKMTA0MDk3Njk0Mg9kFgICAQ9kFgICBw8PFgIeBFRleHQFkQNUV0Q2N+e2k+e3r+W6puWdkOaomeWAvCA644CA44CA44CAIOOAgDxiPjEyMDowODoyMS4xMTQwMCwgMjM6MDM6MTAuMTE1MDA8c21hbGw+ICgxMjAuMTM5MTk4MzMzMzMzLDIzLjA1MjgwOTcyMjIyMjIpPC9zbWFsbD48L2I+PGJyPlRXRDY35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8IDrjgIDjgIAg44CAPGI+MTYxNzg4Ljk4NSwgMjU1MDM5OS4yMjA8L2I+PGJyPlRXRDk3KFdHUzg0Kee2k+e3r+W6puWdkOaomeWAvCA6IDxiPjEyMDowODo1MC4xOTIyMCwgMjM6MDM6MDMuNzk2MjQ8c21hbGw+ICgxMjAuMTQ3Mjc1NjExMzcyLDIzLjA1MTA1NDUxMDI2NjMpPC9zbWFsbD48L2I+PGJyPlRXRDk35LqM5bqm5YiG5bi25Z2Q5qiZ5YC8IDrjgIAg44CA44CAPGI+MTYyNjE1LjkzNCwgMjU1MDE5MS4xODI8L2I+PGJyPmRkZG/sibbFSPm1K+nXL2AG/J+PInJM",
        "__VIEWSTATEGENERATOR":"F862B26F"
    }
    res = requests.post(url, headers = headers, data=data)
    soup = BeautifulSoup(res.text, 'html.parser')
#     axis = soup.find("span", id="Message").find_all('b')[2].string.split(',')
    axis = soup.find("span", id="Message").find_all('b')[2].find('small').string[2:-2].split(',')
    print(axis)
    axis2 = [float(axis[1]), float(axis[0])]
    return float(axis[1]), float(axis[0])