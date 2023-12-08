
import requests
import json
import time
import os

def cache_data(data, filename):
    """
    Cache data by saving it to a file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_cached_data(filename):
    """
    Load cached data from a file if it exists.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return None

def get_yelp_data(api_key, term, location, price=None, offset=0, limit=50):
    headers = {'Authorization': 'Bearer %s' % api_key}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'term': term,
        'location': location,
        'limit': limit,
        'offset': offset
    }
    if price:
        params['price'] = price

    print(f"Making API call with parameters: {params}")

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error occurred: {response.status_code}")
        return None

def create_tree(data):

    tree = {}
    for restaurant in data:
        cuisine = restaurant.get('categories', [{}])[0].get('title', 'Unknown')
        price = len(restaurant.get('price', 'Unknown'))
        if price > 4:
            price = 'unknown'
        else:
            price = str(price)
        location = restaurant.get('location', {}).get('city', 'Unknown')

        if cuisine.lower() not in tree:
            tree[cuisine.lower()] = {}
        if price not in tree[cuisine.lower()]:
            tree[cuisine.lower()][price] = {}
        if location.lower() not in tree[cuisine.lower()][price]:
            tree[cuisine.lower()][price][location.lower()] = []

        tree[cuisine.lower()][price][location.lower()].append(restaurant)

    return tree

def get_user_preferences():
    """
    Prompt the user to enter their preferences for cuisine, price range, and location.
    """
    cuisine = input("Enter preferred cuisine type: ").lower()
    price_range = input("Enter preferred price range (e.g., $10-$20, $20-$30, $30-$40, more than $40): ")
    location = input("Enter preferred location: ").lower()
    return cuisine, price_range, location

def map_price_range_to_yelp_format(price_range):
    """
    Map numeric price range to Yelp's integer format.
    """
    if price_range == "$10-$20":
        return "1"
    elif price_range == "$20-$30":
        return "2"
    elif price_range == "$30-$40":
        return "3"
    elif price_range == "more than $40":
        return "4"
    else:
        return ""
    
def filter_restaurants(tree, cuisine, price_range, location):
    """
    Filter restaurants based on the user's preferences.
    """
    filtered_restaurants = tree.get(cuisine, {}).get(price_range, {}).get(location, [])
    return filtered_restaurants

def main():
    api_key = 'TXb_M2nC3ElV6JpKBKvSTXRUTbXqCQ8QvuHq6mmGGkjjmh6-wfyppxLJTHWCyngrzLZ3r1t3mw0YCR1MBhtqX808U9y3O4H2mbLIWI67fBqP_JcFebus8RWWNANcZXYx' 
    term = 'restaurants'
    location = 'Los Angeles'
    total_records = 1000  
    limit = 50 
    cache_filename = 'yelp_data.json'

    user_cuisine, user_price_range, user_location = get_user_preferences()
    mapped_price = map_price_range_to_yelp_format(user_price_range)

    cached_data = load_cached_data(cache_filename)
    if cached_data:
        print("Loading data from cache.")
        all_data = cached_data
    else:
        all_data = []
        offset = 0
        while offset < total_records:
            data = get_yelp_data(api_key, user_cuisine, user_location, mapped_price, offset, limit)
            if data and 'businesses' in data:
                all_data.extend(data['businesses'])
                offset += limit
                time.sleep(1)  
            else:
                break
        cache_data(all_data, cache_filename)

    restaurant_tree = create_tree(all_data)

    filtered_data = filter_restaurants(restaurant_tree, user_cuisine, mapped_price, user_location)

    if filtered_data:
        print(f"Restaurants matching your preferences in {user_location}:")
        for restaurant in filtered_data:
            print(f"- {restaurant['name']} ({restaurant['rating']} stars, {restaurant['price']})")
    else:
        print("No restaurants found matching your preferences.")

    print(f"Total records retrieved: {len(all_data)}")

if __name__ == "__main__":
    main()
