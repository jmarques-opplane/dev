from ._anvil_designer import SubscriptionDetailsInputTemplate
from anvil import *
import anvil.server
from .SubscriptionDetailsOutput import SubscriptionDetailsOutput

class SubscriptionDetailsInput(SubscriptionDetailsInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()

    nudges_page = Nudges()
    nudges_page.nudges_console.clear()
    nudges_page.nudges_console.add_component(SubscriptionDetailsOutput())
    form.content_panel.add_component(nudges_page)
    
    pass
