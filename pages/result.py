class DuckDuckGoResultPage:

    SEARCH_INPUT = (By.ID, "search_form_input")
    RESULT_LINKS = (By.CLASS, "eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        # TODO
        return []

    def search_input_value(self):
        # TODO
        return ""

    def title(self):
        # TODO
        return ""