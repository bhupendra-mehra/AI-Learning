# ========== SALES REPORT ==========

# Total Products : 4

# Total Quantity : 12

# Total Sales : 3415

# Highest Sale : Laptop ($2400)

# Lowest Sale : Mouse ($125)

# Average Sale : 853.75

# =================================

import csv
import json
from pathlib import Path

path = Path("sales.csv")

try:
    if not path.exists():
        raise FileNotFoundError("File not found")

    total_products = 0
    total_qty = 0
    total_sales = 0
    total_price = 0
    price_dist = {}
    name = ''
    with open(path,"r") as sales:

        reader = csv.reader(sales)
        next(reader)
        for row in reader:
            name = row[0]
            total_qty += int(row[1])
            price_dist[name] = int(row[1]) * float(row[2])
            total_sales += price_dist[name]
            total_products += 1  

    price_dist = dict(sorted(price_dist.items(), key=lambda item: item[1], reverse=True))
    price_dist_keys = list(price_dist.keys())
    report_lines = ["========== SALES REPORT ==========\n",
    "Total Products :" + str(total_products) + "\n",
    "Total Quantity :"+ str(total_qty)+"\n",
    "Total Sales : "+str(total_sales)+"\n",
    "Highest Sale :"+str(price_dist_keys[0])+" ($"+str(max(price_dist.values()))+")\n",
    "Lowest Sale :"+str(price_dist_keys[-1])+" ($"+str(min(price_dist.values()))+")\n",
    "Average Sale : "+str(sum(price_dist.values())/len(price_dist))+"\n",
    "================================="
    ]

    for line in report_lines:
        print(f"{line}")

    with open("Save Report.txt","w") as report:
        report.writelines(report_lines)

    with open("Save Report.json","w") as report_json:
        json.dump(report_lines,report_json,indent=4)

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e)


