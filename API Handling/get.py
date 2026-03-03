import requests

def get_data(url):

    print("Fetching data from API...")

    response = requests.get(url)  # Hey server, give me this data.

    if response.status_code == 200:
        print("Data fetched successfully!")
        data = response.json() # Convert the response to a Python dictionary

        # Extract information
        name = data["results"][0]["name"]["first"]
        country = data["results"][0]["location"]["country"]
        email = data["results"][0]["email"]

        print("Name:", name)
        print("Country:", country)
        print("Email:", email)
    else:
        print("Failed to fetch data")

# Example usage
url = "https://randomuser.me/api/"
get_data(url)