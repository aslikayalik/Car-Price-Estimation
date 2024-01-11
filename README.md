# Car Price Estimation

This project is a web scraper for the website "sahibinden.com". It uses Python along with the libraries requests and BeautifulSoup.


## Usage
The project contains two main functions:

get_options(choice="/otomobil"): This function fetches the options available for a given category from the website. The category is specified by the choice parameter.

get_results(model="/otomobil", year="", km="", sample_size=50): This function fetches the results for a given model, year, and kilometer range. The results are limited by the sample_size parameter.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/33df99b9-aa7f-4a6c-98f4-909fc4e1215b)


## Example
options = get_options("/otomobil")
print(options)

results = get_results(model="/otomobil", year="2010", km="50000", sample_size=100)
print(results)


## Installation

To install the required libraries, run the following command:

```bash


## Project Demonstration
- On this page, the user can choose the car’s features

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/b670b956-c62d-4d2c-a39e-1de5de108809)

- When the user clicks on the brand select button, all brands appear for her/him.
 Suggested brands are shown below after you click to the brand bar.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/597f54ef-c325-4380-b2af-3d865ac6b18d)


![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/4b21860b-ad5b-4860-8d86-7b75aa6bf9a4)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/2df41a85-4daa-48e2-ae44-b0673aff3a94)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/7cc92e70-ab05-4b4b-9b49-42c51cbef55c)

- The user can see the cars after choosing the one user wants according to the parameters which entered.
![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/c374b33d-671d-4282-a5aa-be54548df65a)

- Data can easily export to ‘output.json’.
![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/d474642f-ca83-47f8-8cb4-38717b3715d9)










pip install requests beautifulsoup4
