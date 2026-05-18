from app.tools.browser import Browser


class IndeedService:
    def search_jobs(self, keyword: str):
        browser = Browser()

        url = (
            f"https://www.indeed.com/jobs?q={keyword}"
        )

        browser.page.goto(url)

        jobs = browser.page.locator(".job_seen_beacon")

        results = []

        for i in range(jobs.count()):
            try:
                title = jobs.nth(i).locator("h2").inner_text()

                results.append({
                    "title": title
                })
            except:
                continue

        browser.close()

        return results
