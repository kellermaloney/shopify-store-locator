# Shopify Store Locator

This script helps you locate brick-and-mortar stores with an online store component built on Shopify. It uses the Google Maps API to find nearby stores based on a given location and radius, and checks if the store's website is powered by Shopify. This tool was built as a growth hacking tool for getting customer interviews with Shopify store owners.

## Features

- Search for nearby clothing stores within a specified radius
- Check if the store's website is built with Shopify

## Prerequisites

- Python 3.6+
- Google Maps API Key

## Installation

1. Clone the repository

2. Create a virtual environment (optional but recommended):

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the root directory of the project.
   - Add your Google Maps API key to the `.env` file:
     ```makefile
     GOOGLE_MAPS_API_KEY=your_google_maps_api_key
     ```

## Usage

1. Create a Google Cloud Project
2. Enable the Google Maps APIs:
   - Geocoding API
   - Places API
3. Create an API Key

4. Run the script:

   ```sh
   python shopify_store_locator.py
   ```

5. Follow the prompts to enter the location and radius for your search:
   - Example: Whitefish, MT
   - Radius in meters: 5000

The script will search for clothing stores in the specified location and radius, check if they have a Shopify-powered website, and save the details to `shopify_stores.txt`.

## Output

The output file `shopify_stores.txt` will contain details of the Shopify stores found, including their name, address, and website.

## Notes

- Ensure your Google Maps API key has the necessary permissions for Geocoding and Places API.
- The script attempts to detect Shopify stores by checking for a `meta.json` file on the website. This method may not be foolproof and could result in false negatives or positives.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please open an issue or contact yourname.

**Disclaimer:** This project is for educational and personal use. Use it responsibly and respect the privacy and rights of the store owners.

**Authors:** Keller Maloney
