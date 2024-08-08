# Import necessary modules
import os

from sys import exit
from argparse import ArgumentParser
from requests import get as get_url, exceptions
from dotenvfile import loadfile
from logging import error


# Define a custom exception for API key errors
class APIKeyError(Exception):
    pass


def load_api_key() -> str:
    # Check if the .env file exists
    env_directory = "./.env"

    if os.path.isfile(env_directory):
        # Load the .env file
        env = loadfile(env_directory)

        # Get the API key from the .env file
        env_api_key = env.get('API_KEY')

        if env_api_key:
            # Return the API key
            return env_api_key

    # Fallback to .bashrc
    bashrc_path = os.path.expanduser("~/.bashrc")
    if os.path.isfile(bashrc_path):
        # Open the .bashrc file
        with open(bashrc_path, "r") as f:
            # Read the lines in the file
            for line in f.readlines():
                # Check if the line starts with "export API_KEY="
                if line.startswith("export API_KEY="):
                    # Get the API key from the line
                    env_api_key = line.split("=")[1].strip().strip('"')

                    # Return the API key
                    return env_api_key

    # Fallback to environment variable
    env_api_key = os.environ.get('API_KEY')

    if env_api_key:
        # Return the API key
        return env_api_key

    # Raise an API key error if not found
    raise APIKeyError(
        "Environment file .env does not exists or API_KEY isn't set. Alternatively, use the --api_key argument to "
        "set the key.")


# Define a class to handle local time and date
class LocalTime:
    # Initialize the class with location and API key
    def __init__(self, location: str, set_api_key: str = None):
        # Set the location
        self.location = location

        # Set the API key or load it from environment variables
        self.api_key = set_api_key or load_api_key()

        # Build the API URL
        self.api_url = self._build_api_url()

    # Build the API URL
    def _build_api_url(self) -> str:
        # Return the API URL with the API key and location
        return f"https://api.ipgeolocation.io/timezone?apiKey={self.api_key}&location={self.location}"

    # Fetch data from the API
    def _fetch_data(self) -> dict:
        try:
            # Send a GET request to the API
            response = get_url(self.api_url)

            # Raise an exception if the response is not OK
            response.raise_for_status()

            # Return the response as JSON
            return response.json()
        except exceptions.RequestException as request_error:
            # Log the error
            error(f"Error fetching data: {request_error}")

            # Raise the exception
            raise

    # Get the data from the API
    def get_data(self, data_type: str) -> str:
        # Fetch the data from the API
        data = self._fetch_data()

        # Check if the data type is timestamp
        if data_type == 'timestamp':
            # Set the data type to date_time_unix
            data_type = 'date_time_unix'

        # Return the data
        return data.get(data_type, data.get('date_time'))


# Check if the script is being run directly
if __name__ == '__main__':
    # Create an argument parser
    parser = ArgumentParser(description='Get local time and date of a location')

    # Add an argument for the location
    parser.add_argument(
        'location',
        type=str,
        help='Location to get the time and date of'
    )

    # Add an argument for the data type
    parser.add_argument(
        '--type',
        type=str,
        help='Type of data to get',
        choices=['date_time', 'time', 'date', 'timestamp'],
        required=False,
        default='full'
    )

    # Add an argument for the API key
    parser.add_argument(
        '--api_key',
        type=str,
        help='API key (overrides .env and .bashrc)',
        required=False
    )

    # Parse the arguments
    args = parser.parse_args()

    # Check if the API key is provided
    if args.api_key:
        # Set the API key
        api_key = args.api_key
    else:
        try:
            api_key = load_api_key()
        except APIKeyError as e:
            # Log the error
            error(f"API key error: {e}")

            # Print the help message
            parser.print_help()

            # Exit the script
            exit(1)

    # Check if the API key is valid
    if not api_key:
        error(
            "API key is not set. Please set the API key using the --api_key argument or the API_KEY environment "
            "variable.")
        exit(1)
    else:
        try:
            # Create a LocalTime object
            localtime = LocalTime(args.location, api_key)

            # Print the data
            print(localtime.get_data(args.type))
        except exceptions.RequestException as e:
            # Log the error
            error(f"Error fetching data: {e}")

            # Exit the script
            exit(1)
        except Exception as e:
            # Log the error
            error(f"An error occurred: {e}")

            # Exit the script
            exit(1)
