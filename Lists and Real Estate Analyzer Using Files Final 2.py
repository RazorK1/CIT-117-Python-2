#  Kyle Harris
#  CIT-117/117L Python
#  Lists and Real Estate Analyzer Using Files (REDUX)

import csv
import os

######################## getDataInput Function
def getDataInput(filename):
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return []  # Return an empty list if the file is not found

    records = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Use DictReader to handle named columns
        for row in reader:
            records.append(row) # Append those records
    return records

###################### getMedian Function
def getMedian(price_list):
    sorted_list = sorted(price_list)
    n = len(sorted_list)

# "If the number of entries in the list is odd, divide the count by 2 and use that entry as the median"
# "If the number of entries in the list is even divide the count by 2.  Take that that entry and the entry
# before it and average the two elements and use that as the median."
    if n % 2 == 1:
        return sorted_list[n // 2]
    else:
        mid1 = sorted_list[n // 2]
        mid2 = sorted_list[n // 2 - 1]
        return (mid1 + mid2) / 2

########################### Main function to process the data
def main():
    filename = "RealEstateData.csv" ######### File has to be in the same folder/directory as this program.
    records = getDataInput(filename)

    if not records:
        return

    prices = []
    city_summary = {}
    property_type_summary = {}
    zip_summary = {}

    for record in records: ################ For every record in the record loop
        city = record["city"]
        property_type = record["type"]
        zip_code = record["zip"]

        try:
            price = float(record["price"])  ########### Convert price to float
        except ValueError:
            continue  ########### Skip rows with invalid price data

        prices.append(price) ####### Append that price

        city_summary[city] = city_summary.get(city, 0) + price
        property_type_summary[property_type] = property_type_summary.get(property_type, 0) + price
        zip_summary[zip_code] = zip_summary.get(zip_code, 0) + price

    prices.sort() #Sorts prices

    ############## Calculate summary statistics
    min_price = min(prices)               # Min
    max_price = max(prices)               # Max
    total_price = sum(prices)             # Sum
    avg_price = total_price / len(prices) # Avg
    median_price = getMedian(prices)      # Median

    ############# Output results
    print("Summary of Property Prices:")
    #print(f"Minimum Price: ${min_price:,.2f}")   # Min ########################### Old Code
    #print(f"Maximum Price: ${max_price:,.2f}")   # Max ########################### Old Code
    #print(f"Total Price  : ${total_price:,.2f}")   # Sum ########################### Old Code
    #print(f"Average Price: ${avg_price:,.2f}")   # Avg ########################### Old Code
    #print(f"Median Price : ${median_price:,.2f}") # Median ########################### Old Code
    
    print(f"Minimum Price       : ${min_price:,.2f}")   # Min ########################### New Code (Wasn't able format these properly)
    print(f"Maximum Price       : ${max_price:,.2f}")   # Max ########################### New Code
    print(f"Total Price         : ${total_price:,.2f}")   # Sum ########################### New Code
    print(f"Average Price       : ${avg_price:,.2f}")   # Avg ########################### New Code
    print(f"Median Price        : ${median_price:,.2f}") # Median ########################### New Code

    ############### Output summary by Property Type
    print("\nSummary by Property Type:") ######Print line
    for p_type, total in property_type_summary.items(): ############ For loop
        #print(f"{p_type:12}: ${total:,.2f}") ########################### Old Code
        print(f"{p_type:20s}: ${total:10,.2f}") ########################### New Code (I assume "Unkown" meant "Unknown")

    ################### Output summary by City
    print("\nSummary by City:") ######Print line
    for city, total in city_summary.items(): ######### For loop
        #print(f"{city:15}: ${total:,.2f}") ########################### Old Code
        print(f"{city:20s}: ${total:10,.2f}") ########################### New Code

    ######### Output summary by Zip Code (Uncommented this time)
    print("\nSummary by Zip Code:")
    for zip_code, total in zip_summary.items(): ######### For loop
        #print(f"{zip_code}: ${total:,.2f}") ########################### Old Code
        print(f"{zip_code:20s}: ${total:10,.2f}") ########################### New Code

############################## Main Function
if __name__ == "__main__":
    main()

# Prevents the program from closing.
input("\nPress Enter to exit...")