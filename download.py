import requests

# Make the GET request
# Define the symbol as a variable
symbol = "BTC/USD"
start_date = "2024-12-01 00:00:00"
end_date = "2024-12-22 20:30:00"
interval = "2024-12-22 20:30:00"

# https://twelvedata.com/account/api-playground

# Create the URL dynamically
url = f"https://api.twelvedata.com/time_series?apikey=4985500cb16646ee94f6ab2b4a90f2a1&interval={interval}&symbol={symbol}&start_date={start_date}&end_date={end_date}&format=CSV"

# Check if the request was successful
if response.status_code == 200:
    csv_data = response.text.replace(";", ",")
    # Open a file in write mode and save the response as CSV
    with open("data/btc.csv", "w") as file:
        file.write(response.text)
    print("Data has been written to btc_data.csv")
else:
    print(f"Error: {response.status_code}")
