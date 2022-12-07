from bs4 import BeautifulSoup
import requests

html__text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html__text)
soup = BeautifulSoup(html__text.text, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
company_name = job.find('h3', class_ = 'joblist-comp-name').get_text()
print(company_name)