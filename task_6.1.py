from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        r = 0
        while r < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[r]}')
            if r == 0:
                sleep(7)
            elif r == 1:
                sleep(5)
            elif r == 2:
                sleep(3)
            r += 1


TrafficLight = TrafficLight()
TrafficLight.running()


