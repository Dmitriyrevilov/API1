import requests


def get_weather_of_places(place):
    url = "http://wttr.in/{}?M?n/Tqu&lang=ru"
    url = url.format([place])
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    wheather_places = ["~Череповец", "~paris", "~svo"]
    for place in wheather_places:
        print(get_weather_of_places(place))


if __name__ == "main":
    main()
