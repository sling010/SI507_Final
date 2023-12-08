# SI 507: Final Project
# Yelp Restaurant Recommendation Tool

## Description
This tool provides personalized restaurant recommendations using data from the Yelp Fusion API. It caters to user preferences for cuisine, price range, and location, offering a customized dining exploration experience.

## Data Sources
### Yelp Fusion API
- **Data URL**: [Yelp Fusion API](https://www.yelp.com/developers/documentation/v3)
- **Documentation URL**: [Yelp Fusion Documentation](https://www.yelp.com/developers/documentation/v3/get_started)
- **Format**: JSON
- **Access Technique**:
  - The data is accessed using Python's `requests` library to make authenticated API requests.
  - Users input preferences are used to query the Yelp database for matching restaurant listings.
- **Caching**: 
  - Data fetched from the API is cached in `yelp_data.json` to reduce redundant network calls and enhance performance.
- **Data Summary**:
  - **Records Available**: Varies, with a comprehensive range across Yelp's extensive database.
  - **Records Retrieved**: Configured to retrieve up to 1000 records per query, adhering to the API's rate limits.
  - **Key Fields**:
    - `name`: Name of the restaurant.
    - `categories`: Type of cuisine.
    - `price`: Price level of the restaurant.
    - `location`: Geographical location.
    - `rating`: Average user rating.
    - `url`: Yelp page of the restaurant.

## Data Structure
- **Organization**:
  - Data is organized into a tree structure based on cuisine, price, and location. This allows efficient filtering and retrieval based on user preferences.
- **Files**:
  - `Fianl_Project_SI507.py`: Constructs the tree structure from Yelp data.
  - `yelp_data.json`: Stores the serialized tree structure.

## Interaction and Presentation
### User Interaction
- **CLI-Based Interaction**:
  - Users interact with the tool through a command-line interface, where they input their dining preferences.
  - The tool processes these inputs and queries the Yelp API to fetch relevant data.
- **Output Presentation**:
  - A list of restaurants matching the criteria is presented to the user, complete with essential details for each listing.

### Running the Program
1. **Pre-requisites**:
   - Python installation with the `requests` library.
2. **API Key**:
   - Insert your Yelp API key into the designated variable in the script.
3. **Execution**:
   - Run the script and input your preferences at the prompts.
4. **View Results**:
   - Review the recommended restaurants displayed in the CLI.

### Instructions
- Detailed instructions for running the tool are provided, ensuring ease of use even for those new to CLI applications.

## Special Instructions
### Cache File
- `yelp_data.json` can be deleted to refresh data from Yelp.

## Screenshots
- Screenshots here would show the input prompts and the resulting restaurant recommendations and the data structure from the Yelp Fusion API.
![Alt text](image-1.png)
![Alt text](image.png)