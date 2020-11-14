from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import parsing


def weather(city, radius):
    geo_data = []
    config = get_default_config()
    config['language'] = 'en'
    owm = OWM('2551509fa0abff6e6e92e5e159ad0f2b', config=config)

    mgr = owm.weather_manager()
    reg = owm.city_id_registry()

    list_of_geopoints = reg.geopoints_for(f'{city}')
    lat = list_of_geopoints[0].lat
    lng = list_of_geopoints[0].lon

    cities = parsing.html(lat, lng, radius)

    for city in cities:
        try:
            place = mgr.weather_at_place(f'{city},RU')
            weather = place.weather
            temp = weather.temperature('celsius')
            geo_data.append([city[0].upper()+city.lower()[1:], temp["temp"], temp["feels_like"]//1, weather.detailed_status[0].upper()+weather.detailed_status[1:]])
            '''
            print(f'Температура в городе {city[0].upper()+city.lower()[1:]} {temp["temp"]}, ощущается как {temp["feels_like"]//1},\
 {weather.detailed_status}')
            '''
        except:
            pass
    return geo_data


if __name__ == '__main__':
    city = input('City: ')
    radius = input('Radius: ')
    print(weather(city, radius))
