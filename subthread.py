import threading
import time
import weather_analysis
import params

exitFlag = False
lising_to_weather = True


class WeatherThread(threading.Thread):
    def __init__(self, converser_):
        threading.Thread.__init__(self)
        self.flag = True
        self.converser = converser_

    def run(self):
        print("开始线程：" + self.name)
        while self.flag:
            if lising_to_weather:
                weather_dic = weather_analysis.get_current_weather()
                self.converser.weather = weather_dic
                set_weathers(self.converser)
                # print(weather_dic)
                time.sleep(10)

        print("退出线程：" + self.name)

    def stop(self):
        self.flag = False

    def restart(self):
        self.flag = True
        self.run()


def set_weathers(converser):
    weathers = converser.weather['results'][0]['now']
    print(weathers)
    converser.ui.label_7.setText(weathers['temperature'])
    converser.ui.label_8.setText(weathers['humidity'])
    converser.ui.label_9.setText(weathers['feels_like'])
    converser.ui.label_10.setText(weathers['wind_direction'])
    converser.ui.label_11.setText(weathers['wind_scale'])
    converser.ui.label_12.setText(weathers['wind_speed'])


def print_time(threadname, delay, counter):
    while counter:
        if exitFlag:
            threadname.exit()
        time.sleep(delay)
        print("%s: %s" % (threadname, time.ctime(time.time())) + " count is " + str(counter))
        counter -= 1


if __name__ == '__main__':
    thread1 = WeatherThread(params.Converser())
    thread1.start()
    time.sleep(1)
    thread1.stop()
