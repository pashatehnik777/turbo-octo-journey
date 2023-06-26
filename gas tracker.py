import requests

# Make a request to the Etherscan API to retrieve the current gas price
response = requests.get("https://api.etherscan.io/api?module=gastracker&action=gasoracle")

# Parse the JSON data in the response
data = response.json()

# Retrieve the gas price from the data
gas_price_wei = int(data["result"]["SafeGasPrice"])

# Convert the gas price from wei to gwei
gas_price_gwei = gas_price_wei / 1

# Print the gas price to the console
print(f"Current gas price: {gas_price_gwei} gwei")
