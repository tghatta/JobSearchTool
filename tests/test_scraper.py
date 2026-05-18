from app.agents.search_agent import SearchAgent


def test_search():
    agent = SearchAgent()

    jobs = agent.search("python")

    assert jobs is not None
