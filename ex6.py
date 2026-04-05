import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True, verify=False)
redirects_quantity = len(response.history)
final_url = response.url
print(f"Количество редиректов: {redirects_quantity}")
print(f"Итоговый url: {response.url}")
