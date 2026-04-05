import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method_params = ["POST", "GET", "PUT", "DELETE"]

# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response_without_method_param = requests.get(url, verify=False)
print(f"1. Ответ на запрос без параметра method: {response_without_method_param.text}")

# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response_head_without_method_param = requests.head(url, verify=False)
print(f"2.1. Ответ на запрос не из списка - HEAD - без параметра method: {response_head_without_method_param.text}")
response_head_with_method_param = requests.head(url, data={"method": "HEAD"}, verify=False)
print(f"2.2. Ответ на запрос не из списка - HEAD - с параметром method: {response_head_with_method_param}")

# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response_with_method_param = requests.post(url, data={"method": "POST"}, verify=False)
print(f"3. Ответ на запрос с правильным значением method: {response_with_method_param.text}")

# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
for method_param in method_params:
    response_post = requests.post(url, data={"method": method_param}, verify=False)
    print(f"4.1. Ответ на POST-запрос со значением method {method_param}: {response_post.text}")
    response_get = requests.get(url, params={"method": method_param}, verify=False)
    print(f"4.2. Ответ на GET-запрос со значением method {method_param}: {response_get.text}")
    response_put = requests.put(url, data={"method": method_param}, verify=False)
    print(f"4.3. Ответ на PUT-запрос со значением method {method_param}: {response_put.text}")
    response_delete = requests.delete(url, data={"method": method_param}, verify=False)
    print(f"4.4. Ответ на DELETE-запрос со значением method {method_param}: {response_delete.text}")
