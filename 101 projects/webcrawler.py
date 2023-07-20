"""
File: webcrawler.py
Name: Eydie Cheng
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tag = soup.tbody.text.split()
        # print(tag[:1000])
        male = 0
        female = 0

        for i in range(1000):  # to avoid the following description being selected

            if i % 5 == 2:
                male_count = ''.join(tag[i].strip().split(','))
                male += int(male_count)
            if i % 5 == 4:
                female_count = ''.join(tag[i].strip().split(','))
                female += int(female_count)
        print(f'Male Number: {male}')
        print(f'Female Number: {female}')



if __name__ == '__main__':
    main()
