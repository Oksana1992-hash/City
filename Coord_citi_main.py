from opencage.geocoder import OpenCageGeocode
from tkinter import *


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


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key) # получаем координаты
    label.config(text=f'Координаты города {city}:\n{coordinates}')


key = '7fc16b0ccb324c30944cbf2198b062e9'

window = Tk()
window.title('Координаты городов')
window.geometry('400x200')

entry = Entry(font=('Arial', 16))
entry.pack(pady=5)
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', font=('Arial', 16), command=show_coordinates)
button.pack(pady=5)

label = Label(text='Введите город и нажмите на кнопку', font=('Arial', 16))
label.pack(pady=5)

window.mainloop()
