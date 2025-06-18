import json

import requests
from bs4 import BeautifulSoup

def parsing(url, pages=5):
    try:
        result = []
        for page in range(1, pages + 1):
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article", class_="ad-tile-horizontal")

            for article in articles:
                title = article.find("p", class_="ad-tile-horizontal-header-container")
                if title:
                    title = title.text.strip()
                print(title)

                price = article.find("p", class_="LFSubHeading size-14 weight-700")
                if price:
                    price = price.text.strip()

                image = article.find("img data-scr")
                if image:
                    image = image.get("scr")

                result.append(
                    {
                        "title": title,
                        "price": price,
                        "image": image
                    }
                )

        with open("../lalafo_kyrgyzstan_rabota.json", "w", encoding="utf-8") as file:
            json.dump(result, file, ensure_ascii=False, indent=4)

        return None
    except Exception as e:
        return [f"Ошибка: {e}"]

parsing("https://lalafo.kg/kyrgyzstan/rabota")
