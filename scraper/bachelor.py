from scraper.core.scraper import Scraper
from scraper.core.common import Common

class Bachelor(Scraper, Common):
    def __init__(self) -> None:
        pass
    
    def get_universities(self):
        soup = self.soup("https://yokatlas.yok.gov.tr/lisans-univ.php")
        universities = []

        for option in soup.select("#univ2 option"):
            if option.text == "Seç...":
                continue

            universities.append([option.text, option["value"]])

        return universities
    
    def get_degrees_by_university(self, university_id):
        soup = self.soup(f"https://yokatlas.yok.gov.tr/lisans-univ.php?u={university_id}")
        degrees = []

        if soup is not None:
            for div in soup.select(".container .panel.panel-primary"):
                degree = div.select_one(".panel-heading a")
                href = degree["href"] if degree else None
                text = degree.text if degree else None

                if href:
                    href = href.split("=")[1]
                
                degrees.append([text, href])

        return degrees
    
    def get_degree_info(self, degree_id):
        soup = self.soup(f"https://yokatlas.yok.gov.tr/content/lisans-dynamic/1000_1.php?y={degree_id}")
        degree_info = {}

        tables = soup.find_all('table', class_='table table-bordered')
        program_title = soup.find('big').text if soup.find('big') else None

        for table in tables:
            tbody = table.find('tbody')
            rows = tbody.find_all('tr')

            for row in rows:
                columns = row.find_all('td')
                key = columns[0].text
                value = columns[1].text

                degree_info[self.transform(key)] = value
                
        degree_info["program_title"] = program_title
        
        return degree_info