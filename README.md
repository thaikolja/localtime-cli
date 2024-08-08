# localtime CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/) [![IPGeolocation API](https://img.shields.io/badge/IPGeolocation-API-orange.svg)](https://ipgeolocation.io/documentation/timezone-api.html)

**localtime CLI** is a Command-Line Interface (CLI) tool written in **Python** that retrieves the **local time and date of a given location**, including cities and countries, using the [IPGeolocation API](https://ipgeolocation.io/). This tool accurately handles time zones, ensuring that you get the correct time and date for your desired location. With its quick execution and simple interface, the `localtime` command is a handy utility for developers, travelers, and anyone who needs to keep track of time across different locations.

## Features

* Retrieves the local time and date of a specified location (city or country)
* Supports different display types: `full`, `time`, `date`, and `timestamp`
* Uses the [IPGeolocation](https://ipgeolocation.io/documentation/timezone-api.html) API for accurate location-based time and date information
* Configurable API key for secure access to the IPGeolocation API
* Command-line interface for easy usage and integration with other tools
* Future support for additional date and time formats

## Installation

To install the `localtime` tool, follow these steps:

#### 1. Clone the repository:

```bash
git clone https://gitlab.com/thaikolja/localtime.git
```

#### 2. Navigate to the project directory:

```bash
cd localtime
```

#### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Configuration Options

The `localtime` tool uses an API key to access the IPGeolocation API. You can configure the API key in one of the following ways:

* Save the API key as `API_KEY` in a `.env` file
* Set the API key as an environment variable in your `.zshrc` or `.bashrc` file
* Pass the API key as an argument using the `--api_key` flag

A default API key can be found in the `.env.example` file. This key is a working API key for the free tier plan and can be used for testing purposes. However, we encourage you to register your own free API key at [IPGeolocation](https://app.ipgeolocation.io/signup) for production use.

## Usage

To use the `localtime` tool, run the following command:

```bash
python localtime.py <location> [--type <data_type>] [--api_key <api_key>]
```

* `<location>`: The city or country for which to retrieve the local time and date (e.g., "New York", "London", etc.)
* `<data_type>`: The type of data to retrieve (optional, default: "full")
	+ `full`: Retrieves the full date and time
	+ `time`: Retrieves only the time
	+ `date`: Retrieves only the date
	+ `timestamp`: Retrieves the Unix timestamp
* `<api_key>`: The API key to use for the IPGeolocation API (optional)

### Examples:

> **Note:** Quotation marks are required for places that contain spaces or special characters.

```bash
python localtime.py "New York"
```

**Displays:** `2024-08-07 18:25:20`

```bash
python localtime.py "Bangkok, Thailand" --type timestamp
```

**Displays:** `1723069621.367`

```bash
python localtime.py "Poland" --type date
```

**Displays:** `2024-08-08`

## Creating a Binary with PyInstaller

To create a binary executable of the `localtime` tool, you can use PyInstaller. This is useful for distributing the tool to users who may not have Python installed on their systems. By creating a binary executable, you can ensure that the tool is easily accessible and can be run without requiring any additional setup.

### Steps to create a binary with PyInstaller

#### 1. Install PyInstaller

```bash
pip install pyinstaller
```

#### 2. Navigate to the project directory

```bash
cd localtime
```

#### 3. Run PyInstaller

```bash
pyinstaller --onefile localtime.py
```

This will create a `dist` directory containing the binary executable `localtime`.

## Changelog

### v0.0.2

* Added support for creating a binary executable using PyInstaller
* Improved documentation and usage examples
* No changes to the underlying functionality of the tool

### v0.0.1

* Initial release of the `localtime` tool
* Supports retrieving local time and date of a specified location using the IPGeolocation API
* Configurable API key for secure access to the IPGeolocation API

## Future Development

In the future, the `localtime` tool will support additional date and time formats. Additional error handling and logging may also be added.

## Contribution Guidelines

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with a descriptive commit message
4. Open a pull request to the main repository

## Author

* [**Kolja Nolte**](https://kolja-nolte.com) <[kolja.nolte@gmail.com](mailto:kolja.nolte@gmail.com)>

## License

The `localtime` tool is licensed under the MIT License. See the LICENSE file in the project root for more information.

## Acknowledgements

The `localtime` tool uses the [IPGeolocation API](https://ipgeolocation.io/documentation/timezone-api.html) for location-based time and date information. Even though this repository contains a `.env` file with a provided API key, please [obtain your own API key from IPGeolocation](https://app.ipgeolocation.io/signup) to use this tool. [A free plan is offered](https://ipgeolocation.io/pricing.html) that offers 30,000 requests per month and 1,000 requests per day.
