from app.services.indeed_service import IndeedService


class SearchAgent:
    def __init__(self):
        self.indeed = IndeedService()

    def search(self, keyword: str):
        return self.indeed.search_jobs(keyword)
