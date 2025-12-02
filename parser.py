import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    out_type = input("CSV / JSON?\n")

    url = 'https://edition.cnn.com/'

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        titles = soup.find_all('span', class_='container__headline-text')

        seen = set()
        counter = 1
        for title in titles:
            headline = title.get_text(strip=True)
            if headline and headline not in seen:
                link_tag = title
                for _ in range(3):
                    if link_tag.parent:
                        link_tag = link_tag.parent

                href = link_tag.get('href')
                full_url = urljoin(url, str(href)) if href else "Not found"

                print(f"{counter}. {headline}\nLink: {full_url}\n")
                seen.add(headline)
                counter += 1
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return

if __name__ == "__main__":
    main()
