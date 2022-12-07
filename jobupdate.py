from bs4 import BeautifulSoup
import requests

print("Put some skills that you are not familiar with: ")
unfamiliar_skills = input('> ')
print(f"Filtering out {unfamiliar_skills} ")

html__text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html__text)
soup = BeautifulSoup(html__text.text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
       datePost = job.find('span', class_='sim-posted').span.text
       if 'few' in datePost:
            company_name = job.find('h3', class_ = 'joblist-comp-name').get_text().replace(' ', '')
            skills = job.find('span', class_ = 'srp-skills').get_text().replace(' ', '')
            moreInfo = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                 print(f"CompanyName: {company_name.strip()}")
                 print(f"RequiredSkills: {skills.strip()}")
                 print(f"MoreInfo: {moreInfo}")
            
                 print(' ')