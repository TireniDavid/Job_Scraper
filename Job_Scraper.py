from bs4 import BeautifulSoup
import requests
import time


print("Put Some skills that you ar not familiar with (separated with space)")
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')
unfamiliar_skills = unfamiliar_skill.split(' ')
class Job_match:

    def find_jobs(self):
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
        for index, job in enumerate(jobs):
            detect_unwanted = False
            published_date = job.find('span', class_="sim-posted").text
            if published_date.__contains__("few"):
                company_name = job.find('h3', class_="joblist-comp-name").text.replace('  ', ' ')
                skills = job.find('span', class_="srp-skills").text.replace('  ', ' ')
                more_info = job.header.h2.a['href']

                for unfamiliar in unfamiliar_skills:
                    if unfamiliar in skills:
                        detect_unwanted = True
                        break
                if detect_unwanted == False:
                    with open(f'posts/{index+1}.txt', 'w') as f:
                        f.write(f'Company Name: {company_name.strip()}\n')
                        f.write(f'Required Skills: {skills.strip()}\n')
                        f.write(f'More Info: {more_info}\n')
                    print(f'File saved: {index + 1}')

if __name__ == '__main__':
    job_match = Job_match()
    while True:
        job_match.find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
