# 🚀 Smart Web Scraper with Stealth (Playwright)

## 📌 Overview

**Smart Scraper** is a dynamic web scraping project built using Playwright.
It extracts structured data from websites while simulating real user behavior and applying browser-level stealth techniques to reduce detection.

This project demonstrates **real-world scraping practices**, including pagination handling, retry mechanisms, and human-like interaction.

---

## ✨ Features

* 🔄 **Multi-page Scraping** – Automatically navigates through pages
* 🤖 **Human-like Behavior** – Random delays & scrolling
* 🛡️ **Stealth Configuration** – Reduces automation detection signals
* 🔁 **Retry Mechanism** – Handles temporary failures
* 📊 **Structured Data Extraction** – Title, Price, Rating
* 💾 **CSV Export** – Clean dataset generation

---

## 🛠️ Tech Stack

* **Python**
* **Playwright**
* **Pandas**

---

## 📂 Project Structure

```bash
Smart-Scraper/
│
├── main.py             # Main scraping logic
├── check_stealth.py    # Stealth testing script
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aditya131805/Smart-Scraper.git
cd Smart-Scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## ▶️ Usage

### Run the scraper

```bash
python main.py
```

👉 This will generate:

```
books.csv
```

---

### Test stealth configuration

```bash
python check_stealth.py
```

👉 This opens a browser and tests detection signals.

---

## ⚙️ How It Works

1. Launches a Chromium browser using Playwright
2. Applies stealth configurations to reduce automation detection
3. Navigates through paginated pages
4. Extracts structured data from each page
5. Saves results into a CSV file

---

## 📊 Output Format

| Title       | Price | Rating |
| ----------- | ----- | ------ |
| Sample Book | 51.77 | 3      |

👉 The output file (`books.csv`) is generated after running the script.

---

## 💡 Use Cases

* 🛒 E-commerce product scraping
* 📈 Price monitoring
* 📊 Data analysis
* 🧾 Lead generation

---

## ⚠️ Disclaimer

This project is intended for **educational purposes only**.
Always respect a website’s **robots.txt and terms of service** before scraping.

---

## 👨‍💻 Author

**Aditya Gupta**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
