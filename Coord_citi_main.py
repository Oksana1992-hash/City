from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru') # результат, который мы получим, отправив запрос
        if results: # Если результат поиска не пустой:
            lat = round(results[0]['geometry']['lat'], 2) # создаем переменные, в которые вкладываем полученные с сайта значения и округляем до двух знаков после запятой
            lon = round(results[0]['geometry']['lng'], 2)
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}'


key = '7fc16b0ccb324c30944cbf2198b062e9'
city = 'Реутов'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')

