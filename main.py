import requests
import urllib.parse
from urllib.parse import urljoin


def get_weather_of_places(place):
    base_url = "http://wttr.in/"
    params = {
        "M": "",
        "n": "",
        "Tqu": "",
        "lang": "ru",
    }

    url = urljoin(base_url, place) + "?" + urllib.parse.urlencode(params)
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def main():
    places = [
        "~Череповец",
        "~paris",
        "~svo",
    ]
    for place in places:
        print(get_weather_of_places(place))


if __name__ == "__main__":
    main()
