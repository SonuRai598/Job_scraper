# 💼 Remote Job Scraper

A Python-based command-line tool that lets you search, view, and save remote job listings from [RemoteOK.com](https://remoteok.com). Jobs are scraped using BeautifulSoup and stored in an SQLite database to prevent duplicates and allow future access.

## 📌 Features

✅ Search for remote jobs by keyword  
✅ View job title, company, location and post date  
✅ Open application links directly  
✅ Save jobs in SQLite database (duplicates avoided)  
✅ Organized into clean modules (Scraper, Database, User)  

## 🛠 Tech Stack

- **Language**: Python 3
- **Libraries**: 'requests', 'beautifulsoup4', 'sqlite3'
- **Database**: SQLite

## 📁 Project Structure

job-scraper/
├── main.py # Main application logic
├── scraper.py # Object-Oriented scraper class
├── data_base.py # SQLite operations (create table, insert)
├── user.py # User welcome/login (Guest mode)
├── jobs.db # SQLite database file (auto-generated)
└── README.md 

## ▶️ Getting Started
1. Clone the repository
git clone https://github.com/your-username/job-scraper.git
cd job-scraper

2. Install dependencies
pip install requests beautifulsoup4

3. sqlite3 is built into Python, no need to install it separately.

4. Run the project
python main.py

🔍 How It Works
The script welcomes the user as a Guest.
You enter a keyword (like python, developer, etc.).
It scrapes the first page of results from RemoteOK.
Shows job title, company, location, detail url, apply url and date.
You select a job to view its application link.
Job data is saved in a local jobs.db file (no duplicates).

💾 Database Info
SQLite database: jobs.db
Table: jobs
Columns: job_title, company, location, date_posted, detail_url

📣 Credits
Job data scraped from RemoteOK.com
Built with ❤️ using Python by a beginner developer exploring web scraping and Git workflows
