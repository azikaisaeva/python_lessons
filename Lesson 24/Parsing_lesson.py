import json

import requests
from bs4 import BeautifulSoup

def parsing(url, pages=1):
    try:
        result = []
        for page in range(1, pages + 1):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article", class_="lf-ad-tile")


            for article in articles:
                title = article.find("p", class_="lf-ad-tile__label")
                if title:
                    title = title.text.strip()

                price = article.find("p", class_="LFSubHeading")
                if price:
                    price = price.text.strip()



                image = article.find("img")
                if image:
                    image = image.get("src")



                result.append(
                {
                    "title": title,
                    "price": price,
                    "image": image
                }
            )

        with open("../lalafo_main_page.json", "w", encoding="utf-8") as file:
                json.dump(result, file, ensure_ascii=False, indent = 4)




        return None
    except Exception as e:
       return [f"Ошибка: {e}"]



parsing("https://lalafo.kg/")

#Работа
