# 🛒 Product Inventory Scraper

This is a Python-based project for scraping and tracking competitor product data for shopify stores . It extracts product listings, transforms them into a structured format, and stores them in MongoDB for monitoring stock, pricing, and metadata over time.

---

## 📦 Features

- Scrapes paginated product data using the SearchTap API
- Cleans and transforms raw JSON into consistent structure
- Saves product records into MongoDB
- Tracks inventory, sizes, conditions, vendor, price, tags, and more
- Supports skip-based pagination for full dataset coverage

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/capef0nt/products_tracker.git
cd products_tracker


pip install -r requirements.txt
```
**Configure Environment Variables**
AUTHORIZATION=your_bearer_token
MONGO_URI=mongodb://localhost:27017
```
products_tracker/
├── main.py                # main logic 
├── connect.py             #(pagination, data fetching)
├── data_extract.py        # Data transformation logic
├── mongodb_client.py      # MongoDB connection + insert
├── .env                   # Local env file (not committed)
└── README.md              # Project documentation

```
What’s Tracked for Each Product
product_id, variant_id

title, handle, vendor, product_type, product_category

price, compare_at_price

inventory: quantity, in_stock, item ID, inventory policy

options: size, condition

image_url, additional_images

tags, collections

published_at, updated_at
```
🛠 Roadmap / To-Do
✅ Initial working scraper

⏳ Async scraping with aiohttp

⏳ Delta tracking for stock changes

⏳ UI dashboard for visualization

⏳ Historical price analysis

📬 Author
Built with ♥ by Cephas M
Questions? Reach out via email: bcm637@gmail.com
