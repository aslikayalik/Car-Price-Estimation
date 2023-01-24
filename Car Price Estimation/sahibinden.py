from requests import get 
from bs4 import BeautifulSoup as Bs
from time import sleep


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", 
    "Referer": "https://www.sahibinden.com"
    }

url = "https://www.sahibinden.com"


def get_options(choice="/otomobil"): 

    r = get(url + choice, headers=headers)
    soup = Bs(r.content, "html.parser")

    categories = soup.find("div", attrs={"id": "searchCategoryContainer"}).find_all("a")

    options = [(o["title"], o["href"]) for o in categories]
    return options


def get_results(model="/otomobil", year="", km="", sample_size=50):

    results = []

    for offset in range(int(sample_size / 50)): 

        filters = "?pagingSize=50"
        if offset: 
            filters += f"&pagingOffset={offset * 50}"
            sleep(3)
        if km: 
            km = int(km)
            filters += f"&a4_min={int(km * 0.8)}&a4_max={int(km * 1.2)}"
        if year: 
            year = int(year)
            filters += f"&a5_min={year}&a5_max={year}"

        r = get(url + model + filters, headers=headers) 
        soup = Bs(r.content, "html.parser")

        head_row_tds = soup.find_all("thead")[0].find("tr").find_all("td")

        title_index = 2
        year_index = 3
        km_index = 4
        price_index = 6

        for i in range(len(head_row_tds)):
            
            td = head_row_tds[i]
            if td.text.strip() == "İlan Başlığı": 
                title_index = i
            elif td.text.strip() == "Yıl": 
                year_index = i
            elif td.text.strip() == "KM": 
                km_index = i
            elif td.text.strip() == "Fiyat": 
                price_index = i

        trs = soup.find_all("tr", attrs={"class": "searchResultsItem"})

        for tr in trs: 
            try:
                tds = tr.find_all("td")
                result = {
                    "title": tds[title_index].text.strip(),
                    "year": int(tds[year_index].text.strip()),
                    "km": int(tds[km_index].text.strip().replace(".", "")),
                    "price": int(tds[price_index].text.strip().split(" ")[0].replace(".", ""))
                }
                results.append(result)
            except Exception as err: 
                print(err, tds)
                continue

    return results

def get_estimated_price(results): 
    
    total = sum(r["price"] for r in results)
    return int(total / len(results))
            

if __name__ == "__main__": 

    options = get_options("/audi-a3-a3-sportback-1.6-tdi-attraction")

    results = get_results("/audi-a3-a3-sportback-1.6-tdi-attraction", 2011, 200000)
    print( get_estimated_price(results))
