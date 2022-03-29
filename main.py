from bs4 import BeautifulSoup
import requests

data = []

#the main function
def scraper(input):
    #keeping the url generic for scalability
    for i in input:
        url = "https://scraping-interview.onrender.com/"
        if "carrier" and "customerId" in i:
            url = url + i['carrier'].lower() + "/" + i["customerId"]
            url_site = requests.get(url).text
            if i["carrier"] == "MOCK_INDEMNITY":
                # print(url)
                data.append(handle_mock(url_site))
            elif i["carrier"] == "PLACEHOLDER_CARRIER":
                # print(url)
                data.append(handle_placeholder(url_site))
    print(data)

def handle_mock(url):
    soup = BeautifulSoup(url, "lxml")
    keys = soup.findAll("dt")
    # list_keys = soup.findAll("div", class_= "row")
    #optimal way is to utilize row  to read data
    # list_keys = soup.findAll("li")
    # for i in list_keys:
    #     print(handle_additional_tags(i))
    values = soup.findAll("dd")
    mock_dict = dict(zip(handle_additional_tags(keys),handle_additional_tags(values)))
    return mock_dict


def handle_placeholder(url):
    soup = BeautifulSoup(url, "lxml")
    #optimal approach is to utilize div col to read data
    #also not optimized approach as we do not want to read SSNs
    keys = soup.findAll("label")
    values = soup.findAll("span")
    placeholder_dict = dict(zip(handle_additional_tags(keys), handle_additional_tags(values)))
    return placeholder_dict


#function to handle html tag removal
def handle_additional_tags(item):
    function_usage = []
    for i in item:
        i = i.text
        function_usage.append(i)
    
    return function_usage



input = [{
	"carrier": "MOCK_INDEMNITY",
	"customerId": "a0dfjw9a",
},{
  "carrier": "PLACEHOLDER_CARRIER",
	"customerId": "f02dkl4e"
}]

scraper(input)




