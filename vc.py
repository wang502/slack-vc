from bs4 import BeautifulSoup
import httplib2
import unicodedata

portfolio_dict = {
    "a16z": "http://a16z.com/portfolio/venture-growth/",
    "Khosla": "http://www.khoslaventures.com/portfolio",
    "Accel": "http://www.accel.com/companies/",
    "Sequoia": "https://www.sequoiacap.com/companies/",
    "First round": "http://firstround.com/companies",
    "KPCB": "http://www.kpcb.com/companies"
}

industries = ["advertising", "agriculture-food", "big-data", "chemical-fuels", "consumer", "education", "efficiency", "enterprise", "financial-services", "health", "materials", "power", "robotics", "space", "storage", "transportation"]

# get the portfolio list of a16z
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

# Get the portfolio list of Khosla Venture
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
                    print companies[t]

#if __name__ == "__main__":
	#geta16zPortfilios('a16z')
    #getKhoslaPortfolio()
