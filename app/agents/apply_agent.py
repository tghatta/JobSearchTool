from browser_use import Agent


class ApplyAgent:
    def apply(self, url: str):
        agent = Agent(
            task=f"""
            Open this job application:
            {url}

            Fill all forms.
            Stop before final submit.
            """
        )

        agent.run()
