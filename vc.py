from bs4 import BeautifulSoup
import httplib2
import unicodedata
import utils

portfolio_dict = {
    "a16z": "http://a16z.com/portfolio/venture-growth/",
    "Khosla": "http://www.khoslaventures.com/portfolio",
    "Accel": "http://www.accel.com/companies/",
    "Sequoia": "https://www.sequoiacap.com/companies/",
    "First round": "http://firstround.com/companies",
    "KPCB": "http://www.kpcb.com/companies",
    "Greylock": "http://www.greylock.com/greylock-companies"
}

industries = ["advertising", "agriculture-food", "big-data", "chemical-fuels", "consumer", "education", "efficiency", "enterprise", "financial-services", "health", "materials", "power", "robotics", "space", "storage", "transportation"]

# Crawl the portfolio list of a16z
def geta16zPortfilio():
    url = portfolio_dict['a16z']
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    companies = {}
    company = ""
    for li in soup.find(id="main").findAll('li'):
        t = li.get_text()
        if t[0] == "C":
            company = t[9:]
        if t[1] == "W":
            companies[company] = t[9:]
    #print companies["Zulily"]
    return companies

# Crawl the portfolio list of Khosla Venture
def getKhoslaPortfolio():
    url = portfolio_dict['Khosla']
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    companies = {}
    cstring = ""
    for industry in industries:
        url = portfolio_dict['Khosla'] + "/" + industry
        status, response = http.request(url)
        soup = BeautifulSoup(response)
        for i in range(1, 10):
            cstring = "company-" + str(i)
            company = soup.find(id=cstring)
            if (company == None):
                break
            else:
                for li in company.findAll('a'):
                    t = li.get_text()
                    u = li.get('href')
                    companies[t] = portfolio_dict['Khosla'] + u
    return companies

# Crawl the portfolio list of Sequoia Cap
def getSequoiaPortfolio():
    url = portfolio_dict['Sequoia']
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    companies = {}
    name = ""
    for li in soup.find(id="allColumn").findAll('li'):
        name = li.get_text()
        companies[name] = "https://www.sequoiacap.com"+ li.find('div').get('data-url')
    return companies

# Crawl the portfolio list of KPCB ventures
def getKPCBPortfolio():
    url = portfolio_dict['KPCB']
    http = httplib2.Http()
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    companies = {}
    name = ""
    for li in soup.find("div", {"class":"medium-9"}).findAll("li"):
        if li != None:
            a = li.find('a')
            if a != None:
                url = a.get('href')
                if url[0] == '/':
                    url = "http://www.kpcb.com" + url
                name = utils.extract_name(a.get('href'))
                companies[name] = url
    return companies

if __name__ == "__main__":
	#print geta16zPortfilio()
    #print getKhoslaPortfolio()
    #print getSequoiaPortfolio()
    print getKPCBPortfolio()
