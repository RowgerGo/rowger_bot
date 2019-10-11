import json , requests , sys


async def get_weather(city):

    url = "http://apis.juhe.cn/simpleWeather/query?city="+city+"&key=8aed6c066671acb050993278154b6da3"
    _response = requests.get(url)
    _response.encoding='utf-8'

    _result=requests.get(url);
    print(_result)
    _code = _result.status_code

    _response.close()
    return _result;