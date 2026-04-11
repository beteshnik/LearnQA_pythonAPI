import requests
class TestHeader:
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        header_name_expected = "x-secret-homework-header"
        header_value_expected = "Some secret value"
        response = requests.get(url, verify=False)
        headers_data = response.headers
        print(headers_data)
        assert header_name_expected in headers_data, f"There is no {header_name_expected} in the response"
        header_value_actual = headers_data[header_name_expected]
        assert header_value_actual == header_value_expected, \
            f"Actual {header_name_expected} value {header_value_actual} differs from {header_value_expected}"
