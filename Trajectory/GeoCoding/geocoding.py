#!/usr/bin/env
#-*- coding:utf-8 -*-
'''
利用高德地图/baidu api实现经纬度与地址的批量转换
'''
import requests
 

 
def gaode_geocode(address):
    parameters = {'address': address, 'key': '7ec25a9c6716bb26f0d25e9fdfa012b8','city' :'shanghai'}
    base = 'http://restapi.amap.com/v3/geocode/geo'
    response = requests.get(base, parameters)
    answer = response.json()
    print(answer)
    lng = answer['geocodes'][0]['location'].split(',')[0]
    lat = answer['geocodes'][0]['location'].split(',')[1]
    return answer['status'],float(lng),float(lat)


def baidu_geocode(address):
    url = 'http://api.map.baidu.com/geocoder/v2/'
    ak = 'IkrYTHueRhG0vVpt2XySaaHPGqNNI7eX' # 浏览器端密钥
    uri = url + '?' + 'address=' + address  + 'city=上海市' + '&output=json' + '&ak=' + ak 
    response = requests.get(uri)
    answer = response.json()
    print(answer)
    return answer['status'],answer['result']['location']['lng'],answer['result']['location']['lat']



if __name__=='__main__':
	print(gaode_geocode('周东南路'))
	print(baidu_geocode('周东南路'))