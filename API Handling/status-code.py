import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Everything is fine!")
elif response.status_code == 404:
    print("Resource not found!")
elif response.status_code == 401:
    print("Authentication required!")
elif response.status_code == 500:
    print("Server error!")
elif response.status_code == 403:
    print("Forbidden access!")
else:
    print("Something went wrong!")

if response.ok:
    print("Everything is fine!")
else:
    print(response.raise_for_status())