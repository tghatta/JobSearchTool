from app.services.scoring_service import score_job


class FilterAgent:
    def filter_jobs(self, jobs):
        filtered = []

        for job in jobs:
            result = score_job(job["title"])

            if "APPLY" in result:
                filtered.append(job)

        return filtered
