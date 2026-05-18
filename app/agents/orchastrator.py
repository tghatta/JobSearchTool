from app.agents.search_agent import SearchAgent
from app.agents.filter_agent import FilterAgent
from app.agents.tracker_agent import TrackerAgent


class Orchestrator:
    def __init__(self):
        self.search_agent = SearchAgent()
        self.filter_agent = FilterAgent()
        self.tracker = TrackerAgent()

    def run(self):
        jobs = self.search_agent.search(
            "entry level python ai data"
        )

        filtered = self.filter_agent.filter_jobs(jobs)

        for job in filtered:
            print(job)
            self.tracker.save_job(job)
