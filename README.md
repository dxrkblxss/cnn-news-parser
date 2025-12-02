# 📰 CNN News Parser

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A simple Python script to **scrape news headlines** from [CNN](https://edition.cnn.com/) and save them in **CSV** or **JSON** format.

---

## ⚡ Features

- Fetches current headlines from CNN's homepage  
- Filters out duplicate headlines  
- Saves results in CSV or JSON  

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/dxrkblxss/cnn-news-parser.git
cd parser
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

## 📂 Output
| Format | File       |
|--------|------------|
| CSV    | output.csv |
| JSON   | output.json|

Each entry contains:

- headline — news headline
- link — URL to the news

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