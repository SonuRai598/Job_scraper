import requests
from bs4 import BeautifulSoup

class RemoteOkScraper:
    BASE_URL = "https://remoteok.com"

    def __init__(self, search_term):
        self.search_term = search_term.lower()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }

    def fetch_jobs(self):
        url = f"{self.BASE_URL}/remote-{self.search_term}-jobs"
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to fetch jobs, status code {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        job_listings = soup.select("tr[class*='job']")

        if not job_listings:
            print(f"No jobs found for '{self.search_term}'")
            return []

        jobs = []
        for job in job_listings:
            title_elem = job.find("h2", itemprop="title")
            company_elem = job.find("h3", itemprop="name")
            
            location_elem = job.find("div", class_="location")
            if location_elem:
                location_link = location_elem.find("a")
                location = location_link.text.strip() if location_link else location_elem.text.strip()
            else:
                location = "N/A"

            date_elem = job.find("time")
            if date_elem and date_elem.has_attr("datetime"):
                date_posted = date_elem["datetime"]
            else:
                date_posted = "N/A"

            detail_href = job.get("data-href")

            if not title_elem or not company_elem or not detail_href:
                continue

            title = title_elem.text.strip()
            company = company_elem.text.strip()
            detail_url = f"{self.BASE_URL}{detail_href}"

            jobs.append({
                "job_title": title,
                "company": company,
                "location": location,
                "date_posted": date_posted,
                "detail_url": detail_url
            })

        return jobs

    def fetch_apply_link(self, detail_url):
        response = requests.get(detail_url, headers=self.headers)
        if response.status_code != 200:
            print(f"Failed to fetch job detail page: {response.status_code}")
            return None

        soup = BeautifulSoup(response.text, "html.parser")
        apply_link_elem = soup.select_one("a.action-apply")

        if apply_link_elem and apply_link_elem.get("href"):
            apply_link = apply_link_elem["href"]
            if apply_link.startswith("/"):
                apply_link = f"{self.BASE_URL}{apply_link}"
            return apply_link

        return None
