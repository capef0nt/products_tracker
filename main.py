import connect
import data_extract

results = connect.get_collection_products(24)

proudt = data_extract.extract_products_from_results(results)

print(len(proudt))