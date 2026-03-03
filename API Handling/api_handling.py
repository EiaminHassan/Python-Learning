import requests

def get_data_from_api():

    # using freeapi to get random user data
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data = data['data']
        id = data['id']
        username = data['login']['username']
        return id, username
    else:
        raise Exception(f"API request failed with status code {response.status_code}")

def main():
    try:
        id, username = get_data_from_api()
        print(f"User ID: {id}, Username: {username}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()