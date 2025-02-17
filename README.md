# Car Price Estimation 

## Usage
The project contains two main functions:

get_options(choice="/otomobil"): This function fetches the options available for a given category from the website. The category is specified by the choice parameter.

get_results(model="/otomobil", year="", km="", sample_size=50): This function fetches the results for a given model, year, and kilometer range. The results are limited by the sample_size parameter.


## Example
options = get_options("/otomobil")
print(options)

results = get_results(model="/otomobil", year="2010", km="50000", sample_size=100)
print(results)




## Project Demonstration

#### On this page, the user can choose the car’s features.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/ccf3e265-3d04-4008-832f-7ec5b25d0e19)

#### When the user clicks on the brand select button, all brands appear for her/him. 
#### Suggested brands are shown below after you click to the brand bar.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/60a9db7f-d894-4d26-b9ea-848860e04029)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/726780ed-235e-4657-8758-f4927ae59c08)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/0fc24d9b-0fe5-42d1-a1ce-2cc9ae1deffb)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/8f62a00d-f1f3-48cb-b98f-5c4d71195634)

#### The user can see the cars after choosing the one user wants according to the parameters which entered.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/ae5e9811-4efe-4ff6-b1d8-75ae6e9e2534)

#### Data can easily export to ‘output.json’.

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/74848be5-6f63-41a2-ba35-a0502af3abd7)

![image](https://github.com/aslikayalik/Car-Price-Estimation/assets/96055823/965f3982-7b8a-4253-a167-cae46689860d)




## Installation

To install the required libraries, run the following command:

```bash
pip install requests beautifulsoup4 
