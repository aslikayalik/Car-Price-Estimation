# Car Price Estimation

This project is a web scraper for the website "sahibinden.com". It uses Python along with the libraries requests and BeautifulSoup.


## Usage
The project contains two main functions:

get_options(choice="/otomobil"): This function fetches the options available for a given category from the website. The category is specified by the choice parameter.

get_results(model="/otomobil", year="", km="", sample_size=50): This function fetches the results for a given model, year, and kilometer range. The results are limited by the sample_size parameter.


## Example
options = get_options("/otomobil")
print(options)

results = get_results(model="/otomobil", year="2010", km="50000", sample_size=100)
print(results)


## Installation

To install the required libraries, run the following command:

```bash
pip install requests beautifulsoup4
