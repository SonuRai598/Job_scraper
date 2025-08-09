import sqlite3

class JobDatabase:
    def __init__(self, db_name="jobs.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company TEXT NOT NULL,
            location TEXT,
            date_posted TEXT,
            detail_url TEXT NOT NULL UNIQUE
        );
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_job(self, job):
        try:
            query = """
            INSERT INTO jobs (job_title, company, location, date_posted, detail_url)
            VALUES (?, ?, ?, ?, ?)
            """
            self.conn.execute(query, (
                job["job_title"],
                job["company"],
                job["location"],
                job["date_posted"],
                job["detail_url"]
            ))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def close(self):
        self.conn.close()
