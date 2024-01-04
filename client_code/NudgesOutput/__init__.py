from ._anvil_designer import NudgesOutputTemplate
from anvil import *
import anvil.server
from .SubscriptionDetailsInput import SubscriptionDetailsInput

class NudgesOutput(NudgesOutputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def see_how_it_works_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    self.nudges_console.add_component(SubscriptionDetailsInput())
    form.content_panel.add_component(self)
