import aiohttp
import requests
from dotenv import load_dotenv
import os
import json 

load_dotenv()

#Your Bearer token that you have added to your .env 

Authorization = os.getenv("AUTHORIZATION")
#Site pagination uses skip method, skip = 0 == page 1 || skip = 24 == page 2 ... and so on 
skip = 0

request_url = "https://8brcvvnuvxz8dvexp6gzjpmz-fast.searchtap.net/v2"

headers = {
  "Accept": "application/json, text/plain, */*",
  "Accept-Encoding": "gzip, deflate, br, zstd",
  "Accept-Language": "en-US,en;q=0.9",
  "Connection": "keep-alive",
  "Content-Type": "application/json",
  "Host": "8brcvvnuvxz8dvexp6gzjpmz-fast.searchtap.net",
  "Origin": "https://courtorder.co.za",
  "Referer": "https://courtorder.co.za/",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
  "Sec-Fetch-Site": "cross-site",
  "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36",
  "authorization": f"Bearer {Authorization}",
  "sec-ch-ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
  "sec-ch-ua-mobile": "?1",
  "sec-ch-ua-platform": "\"Android\""
}

 

def get_collection_products(skip):
    payload = {
        "query": "",
        "fields": ["*"],
        "textFacets": [
            "system_producttype",
            "option_auto_size",
            "system_vendor",
            "inventoryLocations"
            ],
        "highlightFields": [],
        "searchFields": [
            "title",
            "description",
            "collections",
            "tags",
            "variants.sku",
            "productType"],
            
        "filter": "priorityScore >= 0 AND publishedTimestamp < 1749804936963 AND publishedTimestamp > 0",
        "sort": ["-publishedTimestamp"],
        "skip": skip,
        "count": 24,
        "collection": "GB379H44E9KKW214ER7L1UTH",
        "facetCount": 100,
        "groupCount": 1,
        "typoTolerance": 1,
        "textFacetFilters": {
            "system_producttype": [],
            "option_auto_size": [],
            "system_vendor": [],
            "inventoryLocations": [],
            "price_price_filter": []
            },
        "numericFacets": {
            "price": [
                "[0,100)",
                "[100,200)",
                "[200,300)",
                "[300,400)",
                "[400,500)",
                "[500,2147483647)"
                ],
        "discount": [
            "[0,100)",
            "[100,200)",
            "[200,300)",
            "[300,400)",
            "[400,500)",
            "[500,2147483647)"]
            },
            
        "numericFacetFilters": {},
        "textFacetQuery": None,
        "geo": {},
        "groupBy": "productId"
        }

    response = requests.post(request_url, headers=headers, json=payload).json()
    results = response.get("results", [])
    return results


