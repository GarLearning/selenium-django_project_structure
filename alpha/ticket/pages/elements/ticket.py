from config import Config
from ...page_object.page_objects import PageElement
from ..locators import (
    FillOsFormLocator,
    CreateTicketLocator
)

from ..locators import (
    TagsLocator,
    ByLocator
)

class Common:
    def _extract_input_id_position(self, object_id):
        ...

    def _extract_input_id_position_temp(self, object_id):
        ...

    def _custom_locator(self, locator, **kwargs):
        ...

    def _extract_results_id_position(self, object_id, mark):
        ...

class FillOsForm(PageElement):
    ...

class CreateTicket(PageElement, Common):
    ...
