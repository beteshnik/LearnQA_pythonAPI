import requests

class TestCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        cookie_name_expected = "HomeWork"
        cookie_value_expected = "hw_value"
      
        response = requests.get(url, verify=False)
        cookies_data = response.cookies
        print(cookies_data)
      
        assert cookie_name_expected in cookies_data, f"There is no {cookie_name_expected} in the response"
        cookie_value_actual = cookies_data[cookie_name_expected]
        assert cookie_value_actual == cookie_value_expected, \
            f"Actual {cookie_name_expected} value {cookie_value_actual} differs from {cookie_value_expected}"
