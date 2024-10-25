from opencage.geocoder import OpenCageGeocode
from tkinter import *

from main import window


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru') # результат, который мы получим, отправив запрос
        if results: # Если результат поиска не пустой:
            lat = round(results[0]['geometry']['lat'], 2) # создаем переменные, в которые вкладываем полученные с сайта значения и округляем до двух знаков после запятой
            lon = round(results[0]['geometry']['lng'], 2)
            return f'Широта: {lat}, Долгота: {lon}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates():
    city = entry.get()
    coordinates = get_coordinates(city, key) # получаем координаты
    label.config(text=f'Координаты города {city}: {coordinates}')
key = '7fc16b0ccb324c30944cbf2198b062e9'




window = Tk()
window.title('Координаты городов')
window.geometry('200x100')

entry = Entry()
entry.pack()

button = Button(text='Поиск координат', command=get_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()
