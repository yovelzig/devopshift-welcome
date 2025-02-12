import httpx
from time import sleep
import os

API_KEY = os.environ["API_KEY"]
# headers = {"authorization" }
# response = httpx.get("https://jsonplaceholder.typicode.com/users/1.")

# code = response.status_code
# user_data = response.json()
# # data = response.json()

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    # print(user_data)
    try:
        response = httpx.get(url)
        try:
            code = response.status_code
            response.raise_for_status()
        except httpx.HTTPStatusError :
            if code ==404:
                print("User not found")
            elif code >= 500:
                print("Server error. Please try again later")
            else:
                print("somethig went wrong")           
            # if 200 <= code < 300:           
            #     print(f"name:, {user_data["name"]} ")
            #     print(f"email: {user_data["email"]}")
            #     print(f"address: {user_data["address"]}")
        user_data = response.json() 
        if user_data:
            print(f"name: {user_data['name']}")
            print(f"email: {user_data['email']}")
            print(f"address: {user_data['address']}")
    except httpx.HTTPError:
        print(f"An error occurred: ")


def fetch_matrics1():
    url = f"https://api.example.com/system/metrics?metrics=cpu,memory"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    

def fetch_matrics():
    print("Fetching system metrics...")
    retries = 3
    delay = 2
    url = f"https://api.example.com/system/metrics"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}
    params = {"metrics": "cpu,memory"}  # Query parameters
    for entry in range(retries):
        try:            
            response = httpx.get(url, headers=headers, params=params)            
            if response.status_code == 401:
                print("Invalid API Key")
            elif response.status_code == 500:
                print("Server is currently down")
            break
        except httpx.HTTPError:
            print(f"Attempt {entry+1} failed: Server is currently down.")       
            sleep(delay)
            print(f"Retrying in {delay} seconds...")
    
    
        try:
            response = httpx.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            code = response.status_code
            print("System Metrics:", response.json())
        except httpx.exceptions.HTTPError as errh:
            if code == 401:
                print("Invalid API Key")        
            elif code == 500:
                print("Server is currently down")
                
                               
    


fetch_user_data(1)
fetch_matrics()


# , params={"name": "Leanne Graham"}, headers={"Accept": "application/json"}











# for attempt in range(1, retries + 1):
#     try:
#         print(f"Fetching system metrics... (Attempt {attempt})")
#         response = requests.get(url, headers=headers, timeout=5)
#         response.raise_for_status()  # Raise an error for non-200 responses
#         print("System Metrics:", response.json())
#         break
#     except requests.exceptions.HTTPError as errh:
#         if response.status_code == 401:
#             print("Invalid API Key.")
#             break
#         elif response.status_code == 500:
#             print("Server is currently down.")
#         else:
#             print(f"HTTP error occurred: {errh}")
#     except requests.exceptions.ConnectionError:
#         print("Error: Unable to connect to the API.")
#     except requests.exceptions.Timeout:
#         print("Error: The request timed out.")
#     except requests.exceptions.RequestException as e:
#         print(f"General error occurred: {e}")
    
#     if attempt < retries:
#         print(f"Retrying in 2 seconds...")
#         time.sleep(2)
#     else:
#         print("All retry attempts failed.")