import json.decoder
from requests import Response
class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"Нет куки {cookie_name} в ответе"
        return  response.cookies[cookie_name]
    def get_header(self, response: Response, header_name):
        assert header_name in response.headers, f"Нет заголовка {header_name} в ответе"
        return response.headers[header_name]
    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
            assert name in response_as_dict, f"В ответном json нет {name}"
            return response_as_dict[name]
        except json.decoder.JSONDecodeError:
            assert False, f"В ответе нет json. Ответ: {response.text}"
