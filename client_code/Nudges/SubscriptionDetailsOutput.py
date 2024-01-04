from ._anvil_designer import SubscriptionDetailsOutputTemplate
from anvil import *
import anvil.server
from . import Nudges

class SubscriptionDetailsOutput(SubscriptionDetailsOutputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()

    sub_details = SubscriptionDetails()
    sub_details.response_panel.clear()
    sub_details.response_panel.add_component(RichText(content="ANVIL"))

    nudges_page = Nudges()
    nudges_page.nudges_console.clear()
    nudges_page.nudges_console.add_component(sub_details)
    form.content_panel.add_component(nudges_page)

    pass
