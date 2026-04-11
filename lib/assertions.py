from requests import Response
import json
class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
            assert name in response_as_dict, f"В ответном json нет ключа {name}"
            assert response_as_dict[name] == expected_value, error_message
        except json.JSONDecodeError:
            assert False, f"В ответе нет json. Ответ: {response.text}"
