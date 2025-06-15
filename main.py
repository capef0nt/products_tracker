import connect
import data_extract
from db import collection
import time

def scrape_and_store_all():
    skip = 0
    page_size = 24
    while True:
        results = connect.get_collection_products(skip)
        if not results:
            break  # No more products
        products = data_extract.extract_products_from_results(results)
        if products:
            collection.insert_many(products)
            print(f"Inserted {len(products)} products from skip={skip}")
        skip += page_size
        time.sleep(6)

if __name__ == "__main__":
    scrape_and_store_all()
