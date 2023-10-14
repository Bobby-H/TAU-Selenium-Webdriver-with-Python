class DuckDuckGoResultPage:

    SEARCH_INPUT = (By.ID, "search_form_input")
    RESULT_LINKS = (By.CLASS_NAME, "eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu")

    def __init__(self, browser):
        self.browser = browser

    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        search_input = self.browser.find_elements(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        # TODO
        return ""