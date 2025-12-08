# 📰 CNN News Parser

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple Python script to **scrape news headlines** from [CNN](https://edition.cnn.com/) and save them in **CSV** or **JSON** format.

---

## ⚡ Features

- Fetches current headlines from CNN's homepage  
- Filters out duplicate headlines  
- Saves results in CSV, JSON, or HTML using a template

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/dxrkblxss/cnn-news-parser.git
cd cnn-news-parser
```

2. (Recommended) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> [!WARNING]
> Using a virtual environment is recommended, especially on Linux distributions like Arch/Manjaro, to avoid system package conflicts (PEP 668).

---

## 🚀 Usage
By default, output is saved in CSV:

```bash
python parser.py
```

To save in JSON:

```bash
python parser.py --format json
```

To save in HTML (uses template.html):

```bash
python parser.py --format html
```

You can also specify a custom output file name:

```bash
python parser.py --format csv --output my_news
```

## 📂 Output
| Format | File       |
|--------|------------|
| CSV    | output.csv |
| JSON   | output.json|
| HTML   | output.html|

Each entry contains:

- headline — news headline
- link — URL to the news

---

## 🖼 HTML Template
The script uses **Jinja2** to render HTML output. A default template `template.html` is already included in the project, but you can **modify it** to fit your needs.

Example structure of `template.html`:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Scraped Content</title>
</head>

<body>
    <h1>Scraped CNN Titles</h1>
    {% if data %}
        {% for title in data %}
        <ul>
            <li><a href="{{ title.link }}">{{ title.headline }}</a></li>
        </ul>
        {% endfor %}
    {% else %}
    <p>No titles found.</p>
    {% endif %}
</body>

</html>
```

The `data` variable (list of dictionaries with `headline` and `link`) contains all the scraped headlines and links.

---

## Example `output.csv`:

| headline                     | link                                |
|-------------------------------|------------------------------------|
| CNN Top Story Example         | https://edition.cnn.com/news/xyz  |

---

> [!IMPORTANT]
> - The script uses BeautifulSoup and requests.
>
> - CNN's website structure may change, which could break the parser.
>
> - Python 3.9+ is required.

## 📄 License
MIT License
