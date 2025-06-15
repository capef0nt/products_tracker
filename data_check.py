import db
import json
import asyncio
import aiohttp
import random
from datetime import datetime

# Connect to MongoDB collections
sourced_collection = db.collection
fetched_collection = db.fetched_collection

# Settings
MAX_CONCURRENT_REQUESTS = 5
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

# Fetch product data and immediately insert it into the new collection
async def fetch_details(session, handle, retries=3, backoff=1):
    url = f"https://www.courtorder.co.za/products/{handle}.json"

    for attempt in range(retries):
        try:
            async with semaphore:
                await asyncio.sleep(random.uniform(0.8, 1.7))  # random delay
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        if "product" in data:
                            product = data["product"]
                            product["fetched_at"] = datetime.utcnow()  # optional
                            fetched_collection.update_one(
                                {"handle": product["handle"]},
                                {"$set": product},
                                upsert=True
                            )
                            print(f"✅ Fetched + inserted: {handle}")
                        return data
                    elif response.status == 429:
                        print(f"⏳ Rate limited for {handle} (attempt {attempt+1})")
                        await asyncio.sleep(backoff * (2 ** attempt))
                    else:
                        print(f"⚠️ Failed {handle}: HTTP {response.status}")
                        return None
        except Exception as e:
            print(f"❌ Error fetching {handle} (attempt {attempt+1}): {e}")
            await asyncio.sleep(backoff * (2 ** attempt))

    print(f"🚫 Giving up on {handle} after {retries} attempts")
    return None

# Main runner for all handles
async def main():
    products_handles = [doc["handle"] for doc in sourced_collection.find({}, {"handle": 1, "_id": 0})]

    print(f"\n📦 Found {len(products_handles)} product handles to fetch.")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_details(session, handle) for handle in products_handles]
        await asyncio.gather(*tasks)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
