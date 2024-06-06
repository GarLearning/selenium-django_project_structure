from selenium.webdriver.common.by import By

class TagsLocator:
    a_tag = (By.TAG_NAME, "a")
    li_tag = (By.TAG_NAME, "li")
    span_tag = (By.TAG_NAME, "span")
    tr_tag = (By.TAG_NAME, "tr")
    td_tag = (By.TAG_NAME, "td")
    input_tag = (By.TAG_NAME, "input")
    div_tag = (By.TAG_NAME, "div")


class ByLocator:
    by_id = (By.ID)
    by_css_selector = (By.CSS_SELECTOR)