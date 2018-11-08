# coding: utf-8
# encoding =utf-8
 
import requests
import json
import time
import random

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import json
import urllib
import math

x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方




def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False



"""这一排之后的方法都是将高德地图坐标转换的方法"""
def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return [lng, lat]
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng, lat * 2 - mglat]

def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret

def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


network = open('/Users/xinyilian/Desktop/BusStation/Network.txt', 'r')
path = '/Users/xinyilian/Desktop/BusStation/Location_bus600_609.txt'
location = open(path, 'a')

line = network.readlines()

count = 120
fileNum =1
for i in line:
    count = count + 1
    num = unicode(i,"utf-8")
    if (is_number(num[2:6])):
        number = num[2:6]
    elif (is_number(num[2:5])):
        number = num[2:5]
    elif (is_number(num[2:4])):
        number = num[2:4]

  
        
    # print number
    headers =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
    url = 'https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=50&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=310100&geoobj=121.1284%7C30.9688%7C121.8494%7C31.481428&keywords=' + number + '%E8%B7%AF'
    rand_time_sleep = random.uniform(2, 5)
    time.sleep(rand_time_sleep)
    json_obj = requests.get(url, headers=headers)
    # print json_obj.text

    data = json_obj.json()
    # print data["data"]["lqii"]["change_query_tip"]
    

    # Bus ={}
    # stationList = []
    if(data["data"]["lqii"]["change_query_tip"]==""):
        if (data["data"]["message"]):
            # 车名
            busName = data["data"]["keywords"]
            # print busName
            # 一个stationLists就是一辆车的所有站点
            stationLists = data["data"]["poi_list"]
            # 一个stationList就是一个站点的信息
            for j in stationLists:
                if(count % 10 == 0):
                    location.close()
                    del(location)
                    path = '/Users/xinyilian/Desktop/BusStation/Location_bus' + str(count) +'_'+str(count+9)+ '.txt'
                    location = open(path, 'a')
                lng = j["longitude"]
                lat = j["latitude"]
                result = gcj02_to_wgs84(lng, lat)
                # +j["longitude"]+","+j["latitude"]
                st = busName+","+j["disp_name"]+","+str(result[0])+","+str(result[1])
                print str(st).decode("utf8")
                location.write(str(st))
                location.writelines('\n')
location.close()


