import json 

def extract_products_from_results(results):
    def transform_product(raw):
        return {
            "product_id": str(raw.get("product_id")),
            "variant_id": str(raw.get("id")),
            "title": raw.get("title"),
            "handle": raw.get("handle"),
            "vendor": raw.get("vendor"),
            "product_type": raw.get("productType"),
            "product_category": raw.get("productCategory"),
            "product_category_tree": raw.get("productCategoryTree"),
            "options": {
                "size": raw.get("option1"),
                "condition": raw.get("option2")
            },
            "option_auto_size": raw.get("option_auto_size", []),
            "sku": raw.get("sku"),
            "price": float(raw.get("price", 0)),
            "compare_at_price": float(raw.get("compare_at_price", 0)),
            "inventory": {
                "quantity": raw.get("inventory_quantity"),
                "in_stock": bool(raw.get("in_stock")),
                "inventory_item_id": str(raw.get("inventory_item_id")),
                "inventory_policy": raw.get("inventory_policy"),
                "inventory_management": raw.get("inventory_management")
            },
            "image_url": raw.get("image", {}).get("src"),
            "additional_images": [img.get("src") for img in raw.get("images", []) if img.get("src")],
            "tags": raw.get("tags", []),
            "collections": raw.get("collections", []),
            "published_at": raw.get("publishedAt"),
            "published_timestamp": raw.get("publishedTimestamp"),
            "updated_at": raw.get("updatedAt")
        }

    return [transform_product(product) for product in results]
