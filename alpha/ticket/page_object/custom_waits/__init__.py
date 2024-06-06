class amount_elements:
  def __init__(self, locator, elements):
    self.locator = locator
    self.elements = elements

  def __call__(self, driver):
    element = driver.find_elements(*self.locator)
    if len(driver.find_elements(*self.locator)) >= self.elements:
        return element
    return False