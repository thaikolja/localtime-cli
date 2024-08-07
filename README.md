# Python Localtime CLI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/) [![IPGeolocation API](https://img.shields.io/badge/IPGeolocation-API-orange.svg)](https://ipgeolocation.io/documentation/timezone-api.html)

A Command-Line Interface (CLI) tool that retrieves the **local time and date of a given location** using the [IPGeolocation API](https://ipgeolocation.io/).

## Features

* Retrieves the local time and date of a specified location
* Supports different display types: `full`, `time`, `date`, and `timestamp`
* Uses the [IPGeolocation](https://ipgeolocation.io/documentation/timezone-api.html) API for accurate location-based time and date information
* Configurable API key for secure access to the IPGeolocation API
* Command-line interface for easy usage and integration with other tools

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
install -r requirements.txt
```

#### 4. Create a copy of the example environment file and rename it to `.env`

```bash
cp .env.example .env
```

#### 5. Set your IPGeolocation API key in the `.env` file

```env
API_KEY=your-api-key
```

## Usage

To use the `localtime` tool, run the following command:

```bash
python main.py <location> [--type <data_type>]
```

* `<location>`: The location for which to retrieve the local time and date (e.g., "New York", "London", etc.)
* `<data_type>`: The type of data to retrieve (optional, default: "full")
	+ `full`: Retrieves the full date and time
	+ `time`: Retrieves only the time
	+ `date`: Retrieves only the date
	+ `timestamp`: Retrieves the Unix timestamp

### Examples:

> **Note:** Quotation marks are required for places that contain spaces or special characters.

```bash
python main.py "New York"
```

**Displays:** `2024-08-07 18:25:20`

```bash
python main.py "Bangkok, Thailand" --type timestamp
```

**Displays:** `1723069621.367`

```bash
python main.py "Poland" --type date
```

**Displays:** `2024-08-08`

## Configuration Options

The `localtime` tool uses environment variables to configure the API key. You can set the `API_KEY` variable in the `.env` file or as an environment variable.

## Contribution Guidelines

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Commit your changes with a descriptive commit message
4. Open a pull request to the main repository

## Testing Instructions

To test the `localtime` tool, run the following command:

```bash
python main.py --help
```

This will display the help message and verify that the tool is working correctly.

## Author

* [**Kolja Nolte**]() <[kolja.nolte@gmail.com](mailto:kolja.nolte@gmail.com)>

## License

The `localtime` tool is licensed under the MIT License. See the LICENSE file in the project root for more information.

## Acknowledgements

The `localtime` tool uses the [IPGeolocation API](https://ipgeolocation.io/documentation/timezone-api.html) for location-based time and date information. Even though this repository contains a `.env` file with a provided API key, please [obtain your own API key from IPGeolocation](https://app.ipgeolocation.io/signup) to use this tool. [A free plan is offered](https://ipgeolocation.io/pricing.html) that offers 30,000 requests per month and 1,000 requests per day.

I added the following badges:

* License: MIT
* Python Version: 3.8+
* IPGeolocation API

These badges provide a quick visual representation of the project's license, Python version, and API usage.
