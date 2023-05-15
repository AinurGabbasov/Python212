#  ВИДЕО ПО REQUESTS PYTHON HAB STUDIO
# import json
# import requests
# from fire import API_TOKEN
#
# data = {"custname": "vasya",
#         "custtel": "12312314324",
#         "custemail": "wergeg@mail.ru",
#         "size": "medium",
#         "topping": "bacon",
#         "delivery": "",
#         "comments": ""}
#
# med = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
# }
# variable = requests.Session()
# # response = requests.get("https://www.google.com/search", params=params)
# # response = requests.get("https://httpbin.org/headers", headers=med)
# variable.get("https://httpbin.org/post")
# response = variable.post("https://httpbin.org/post", headers=med, data=data)
#
# # print(response.status_code)
# # print(response.headers)
# # print(response.content)
# print(response.text)
# # print(response.json())
# # x = response.json()
# # print(x["weather"][0]["main"])

# ========================================================================================

# ВИДЕО ПО ПАРСИНГУ САЙТОВ PYTHON HAB STUDIO

# import requests
# from bs4 import BeautifulSoup
# from time import sleep  # чтоб сбереч сайты от перегрузок! и чтоб нас не заблочили!
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
#
#
# def get_url():
#     for count in range(1, 8):
#         url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
#
#         response = requests.get(url, headers=headers)
#
#         soup = BeautifulSoup(response.text, "lxml")  # html.parser тоже можно, но lxml работает реще
#
#         data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
#
#         # for i in data:
#         #     sleep(2)
#         # name = i.find("h4", class_="card-title").text.replace("\n", "")
#         # price = i.find("h5").text
#         # url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
#         #
#         # print(name + "\n" + price + "\n" + url_img + "\n\n")
#
#         for i in data:
#             card_url = "https://scrapingclub.com" + i.find("a").get("href")
#             yield card_url
#
#
# for card_url in get_url():
#     response = requests.get(card_url, headers=headers)
#     sleep(3)  # каждые 3 сек перед запросом на конкретную карточку
#     soup = BeautifulSoup(response.text, "lxml")
#
#     data = soup.find("div", class_="card mt-4 my-4")
#     name = data.find("h3", class_="card-title").text
#     price = data.find("h4").text
#     text = data.find("p", class_="card-text").text
#     url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
#     print(name + "\n" + price + "\n" + text + "\n" + url_img + "\n\n")
