import requests, csv, json
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
from urllib.parse import urljoin
import argparse

def main():
    parser = argparse.ArgumentParser(description="Парсер новостей CNN")
    parser.add_argument(
        "--format",
        choices=["csv", "json", "html"],
        default="csv",
        help="Формат вывода: csv, json или html (по умолчанию csv)",
    )
    args = parser.parse_args()
    out_type = args.format

    url = "https://edition.cnn.com/"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Не удалось получить страницу: {e}")
        return

    soup = BeautifulSoup(response.text, "lxml")
    titles = soup.find_all("span", class_="container__headline-text")

    data = []
    seen = set()

    for title in titles:
        headline = title.get_text(strip=True)
        if not headline or headline in seen:
            continue

        link_tag = title.find_parent("a")
        full_url = (
            urljoin(url, str(link_tag["href"]))
            if link_tag and link_tag.has_attr("href")
            else "Not found"
        )

        data.append({"headline": headline, "link": full_url})
        seen.add(headline)

    if out_type == "csv":
        with open("output.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["headline", "link"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print("Данные сохранены в output.csv")
    elif out_type == "html":
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('template.html')
        html_content = template.render(data=data)
        with open("output.html", "w", encoding="utf-8") as f:
            f.write(html_content)
    else:
        with open("output.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print("Данные сохранены в output.json")

if __name__ == "__main__":
    main()
