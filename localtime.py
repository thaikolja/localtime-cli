# Copyright (C) 2024 by Kolja Nolte
# https://kolja-nolte.com
# <kolja.nolte@gmail.com>
#
# This project is licensed under the MIT License. See the LICENSE file in the project root for more information.
# Furthermore, this software is provided "as-is," without any express or implied warranty. In no event
# shall the authors be held liable for any damages arising from the use of this software.
#
# Permission is GRANTED to anyone to use this software for any purpose, including commercial applications,
# and to alter it and redistribute it freely, subject to the restrictions in the license.
#

# Import the requests library to make HTTP requests
import requests

# Import the os library to interact with the operating system
import os

# Import the sys library to interact with the Python interpreter
import sys

# Import the dotenvfile library to load environment variables from a file
import dotenvfile

# Import the argparse library to parse command-line arguments
import argparse

# Import the logging library to handle errors and provide informative messages
import logging

# Set up logging to display messages with a timestamp, log level, and message
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Define a class to represent the local time of a given location using the IPGeolocation API
class LocalTime:
    """
    A class to represent the local time of a given location using the IPGeolocation API.

    Attributes:
    -----------
    location : str
        The location for which to get the local time.
    api_key : str
        The API key for accessing the IPGeolocation API.
    api_url : str
        The constructed URL for the API request.
    data : dict
        The data fetched from the API.
    """

    # Define the constructor method to initialize the object's attributes
    def __init__(self, location: str):
        """
        Constructs all the necessary attributes for the LocalTime object.

        Parameters:
        -----------
        location : str
            The location for which to get the local time.
        """
        # Set the location attribute to the provided location
        self.location = location

        # Load the API key from environment variables
        self.api_key = self._load_api_key()

        # Build the API URL with the location and API key
        self.api_url = self._build_api_url()

        # Fetch data from the API
        self.data = self._fetch_data()

    # Define a method to load the API key from environment variables
    @staticmethod
    def _load_api_key() -> str:
        """
        Load the API key from environment variables.

        Returns:
        --------
        str
            The API key.

        Raises:
        -------
        SystemExit
            If the environmental file or API key is not found.
        """
        # Specify the directory of the environment file
        env_directory = "./.env"

        # Check if the environment file exists
        if not os.path.isfile(env_directory):
            # Log an error message if the file does not exist
            logging.error(f"Environmental file \"{env_directory}\" could not be found.")
            # Exit the program with a non-zero status code
            sys.exit(1)

        # Load environment variables from the file
        env = dotenvfile.loadfile(env_directory)

        # Get the API key from the environment variables
        api_key = env.get('API_KEY')

        # Check if the API key is set
        if not api_key:
            # Log an error message if the API key is not set
            logging.error("API key not found in environment variables.")
            # Exit the program with a non-zero status code
            sys.exit(1)

        # Return the API key
        return api_key

    # Define a method to build the API URL with the location and API key
    def _build_api_url(self) -> str:
        """
        Build the API URL with the location and API key.

        Returns:
        --------
        str
            The constructed API URL.
        """
        # Construct the API URL with the location and API key
        return f"https://api.ipgeolocation.io/timezone?apiKey={self.api_key}&location={self.location}"

    # Define a method to fetch data from the API
    def _fetch_data(self) -> dict:
        """
        Fetch data from the API.

        Returns:
        --------
        dict
            The data fetched from the API.

        Raises:
        -------
        SystemExit
            If there is an error fetching data from the API.
        """
        try:
            # Make a GET request to the API URL
            response = requests.get(self.api_url)

            # Raise an exception if the response was not successful
            response.raise_for_status()

            # Return the JSON data from the response
            return response.json()
        except requests.exceptions.RequestException as error:
            # Log an error message if there is an error fetching data
            logging.error(f"Error fetching data: {error}")

            # Exit the program with a non-zero status code
            sys.exit(1)

    # Define a method to get data of the specified type
    def get_data(self, data_type: str) -> str:
        if data_type == 'timestamp':
            data_type = 'date_time_unix'

        """
        Get data of the specified type.

        Parameters:
        -----------
        data_type : str
            The type of data to get (e.g., 'full', 'time', 'date', 'timestamp').

        Returns:
        --------
        str
            The requested data or the full date_time if the type is not found.
        """
        # Return the requested data or the full date_time if the type is not found
        return self.data.get(data_type, self.data.get('date_time'))


# Check if the script is being run directly (not being imported)
# ...

if __name__ == '__main__':
    # Create an ArgumentParser to parse command-line arguments
    parser = argparse.ArgumentParser(description='Get local time and date of a location')

    # Add an argument for the location
    parser.add_argument('location', type=str, help='Location to get the time and date of')

    # Add an argument for the type of data to get
    parser.add_argument('--type', type=str, help='Type of data to get', choices=['full', 'time', 'date', 'timestamp'])

    # Parse the command-line arguments
    args = parser.parse_args()

    try:
        # Create a LocalTime object with the provided location
        localtime = LocalTime(args.location)

        # Get the requested data
        print(localtime.get_data(args.type))
    except Exception as e:
        # Log an error message if there is an exception
        logging.error(f"An error occurred: {e}")

        # Exit the program with a non-zero status code
        sys.exit(1)
