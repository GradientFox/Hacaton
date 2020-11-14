import requests


def parse(html):
    result = requests.get(html).text
    cities = result.split('city name="')
    List = []
    for city in range(1, len(cities)-1):
        List.append(cities[city].split('"')[0])
    return List


def html(lat, lng, radius):
    html = f'https://www.freemaptools.com/ajax/get-all-cities-inside.php?lat={lat}&lng={lng}&sortaplha=0&radius={radius}'
    return parse(html)


if __name__ == '__main__':
    lat, lng = map(str, input().split())
    radius = input()
    html(lat, lng, radius)