"""
P1.2 气象处理子系统
"""
import requests
import json


def get_current_weather(city="nanjing"):
    url = 'https://api.seniverse.com/v3/pro/weather/grid/moment.json?key=Sd6gaZ2xGZEoyZ197&location=' + city + '&language=zh-Hans&unit=c&advanced=2.1'
    r = requests.get(url)
    r_dic = r.json()  # 这个是字典对象

    if __name__ == '__main__':
        print(r_dic)
        # 写入样例文件
        with open("assets/current_weather_sample.json", "w") as jsn:
            json.dump(r_dic, jsn, indent=4)

    return r_dic


if __name__ == '__main__':
    get_current_weather()
