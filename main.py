from scraper import RemoteOkScraper
from data_base import JobDatabase

def login():
    username = "Guest"
    print(f"Welcome, {username}!")
    return username

def main():
    user = login()

    search_term = input("Enter the job keyword you want to search for: ").strip()
    scraper = RemoteOkScraper(search_term)
    db = JobDatabase()

    jobs = scraper.fetch_jobs()
    if not jobs:
        print(f"No jobs found for '{search_term}'")
        return
    
    for idx, job in enumerate(jobs, start=1):
        inserted = db.insert_job(job)
        status = "(new)" if inserted else "(exists)"
        print(f"{idx}. {job['job_title']} @ {job['company']} {status}")

    selected = int(input("Enter the job number to see more details: "))
    if selected < 1 or selected > len(jobs):
        print("Invalid selection.")
        db.close()
        return

    job = jobs[selected-1]
    print(f"\nYou selected: {job['job_title']} at {job['company']}")
    print(f"Location: {job['location']}")
    print(f"Date posted: {job['date_posted']}")
    print(f"Details URL: {job['detail_url']}")

    apply_link = scraper.fetch_apply_link(job['detail_url'])
    if apply_link:
        print(f"Apply here: {apply_link}")
    else:
        print("Apply link not found.")

    db.close()

if __name__ == "__main__":
    main()
