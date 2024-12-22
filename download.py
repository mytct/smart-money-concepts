import requests

# Make the GET request
# Define the symbol as a variable
symbol = "FTM/USD"
f_symbol = "FTM"
start_date = "2024-12-01 00:00:00"
end_date = "2024-12-22 20:30:00"
interval = "15min"

# https://twelvedata.com/account/api-playground

# Create the URL dynamically
url = f"https://api.twelvedata.com/time_series?apikey=4985500cb16646ee94f6ab2b4a90f2a1&interval={interval}&symbol={symbol}&start_date={start_date}&end_date={end_date}&format=CSV"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Replace semicolons with commas if necessary
    csv_data = response.text.replace(";", ",")
    
    # Ensure the 'data' directory exists (create it if not)
    import os
    os.makedirs("data", exist_ok=True)

    # Open a file in write mode and save the response as CSV
    with open(f"data/{f_symbol}.csv", "w") as file:
        file.write(csv_data)
    print(f"Data has been written to data/{f_symbol}.csv")
else:
    print(f"Error: {response.status_code}")
