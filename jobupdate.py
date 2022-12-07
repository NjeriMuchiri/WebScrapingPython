from bs4 import BeautifulSoup
import requests
import time

print("Put some skills that you are not familiar with: ")
unfamiliar_skills = input('> ')
print(f"Filtering out {unfamiliar_skills} ")

def findJobs():
 html__text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
# print(html__text)
 soup = BeautifulSoup(html__text.text, 'lxml')
 jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
 for index, job in enumerate(jobs):
    datePost = job.find('span', class_='sim-posted').span.text
    if 'few' in datePost:
        company_name = job.find('h3', class_ = 'joblist-comp-name').get_text().replace(' ', '')
        skills = job.find('span', class_ = 'srp-skills').get_text().replace(' ', '')
        moreInfo = job.header.h2.a['href']
        if unfamiliar_skills not in skills:
            with open(f'posts/{index}.txt', 'w') as f:
                f.write(f"CompanyName: {company_name.strip()} \n")
                f.write(f"RequiredSkills: {skills.strip()} \n")
                f.write(f"MoreInfo: {moreInfo}")
            print(f"File saved: {index}")
if __name__ == "__main__":
    while True:
        findJobs()
        time_wait = 10
        print(f"waiting {time_wait} minutes... ")
        time.sleep(time_wait * 60)