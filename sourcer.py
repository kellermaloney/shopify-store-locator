import googlemaps
import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse, urljoin

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# EDIT THIS TO CHANGE THE TYPE OF PLACE YOU ARE SEARCHING FOR. 
# LIST OF PLACE TYPES: 
PLACE_TYPE = "clothing_store" 

# Get a list of places within a certain location and radius
def get_places_nearby(client, location, radius, place_type, keyword=None):
    # Geocode the location string to a lat/long 
    center = client.geocode(location)[0]['geometry']['location']
    print(center)
    # Perform a nearby search
    places_result = client.places_nearby(
        location=center,
        radius=radius,
        type=place_type,
        keyword=keyword
    )
    places = places_result.get('results', [])
    return places

# Get more in-depth information (website URL) about a single place
def get_place_details(client, place_id):
    # Get detailed information about a place
    place_details = client.place(place_id, fields=["name", "formatted_address", "website"])
    return place_details.get('result', {})

# Check if the current website is built with Shopify
def is_shopify_store(url):
    try:
        # Parse the URL to break it into components
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        path_parts = parsed_url.path.strip('/').split('/')
        
        # Generate possible meta.json paths
        possible_paths = [base_url + "/meta.json"]
        for i in range(len(path_parts)):
            partial_path = "/".join(path_parts[:i+1])
            possible_paths.append(urljoin(base_url, f"{partial_path}/meta.json"))
        
        # Check each path for meta.json
        for path in possible_paths:
            response = requests.get(path)
            if response.status_code == 200:
                try: 
                    meta_details = response.json()
                    return 'myshopify_domain' in meta_details
                except ValueError:
                    print(f"Invalid JSON response from {path}")
                    continue

        return False
    except Exception as e:
        print(f"Error checking Shopify site {url}: {e}")
        return False

def main():
    client = googlemaps.Client(key=API_KEY)

    # Clear the file before writing to it
    with open("shopify_stores.txt", "w") as file:
        file.write("")
    
    # Take location and radius as inputs from the user
    location = input("Enter the location (e.g., 'Whitefish, MT'): ")
    radius = int(input("Enter the search radius in meters: "))
    
    place_type = PLACE_TYPE  # Type of place to search for

    # Get nearby places
    places = get_places_nearby(client, location, radius, place_type)
    shopify_count = 0

    # Retrieve detailed information for each place
    for place in places:
        place_id = place['place_id']
        details = get_place_details(client, place_id)
        url = details.get('website')

        # Check if each place is a Shopify store
        if url and is_shopify_store(url):
            shopify_count += 1
            with open("shopify_stores.txt", "a") as file:
                file.write(f"Name: {details.get('name')}\n")
                file.write(f"Address: {details.get('formatted_address')}\n")
                file.write(f"Website: {details.get('website')}\n")
                file.write("-" * 30 + "\n")

    print(f"Searched {len(places)} {place_type} stores and found {shopify_count} Shopify stores. Check results in shopify_stores.txt")

if __name__ == "__main__":
    main()
