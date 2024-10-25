from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city # запрос
    results = geocoder.geocode(query) # результат, который мы получим, отправив запрос

    if results: # Если результат поиска не пустой:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'


key = '7fc16b0ccb324c30944cbf2198b062e9'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')

