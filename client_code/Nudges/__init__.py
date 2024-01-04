from ._anvil_designer import NudgesTemplate
from anvil import *
import anvil.server
from .SubscriptionDetails import SubscriptionDetails

class Nudges(NudgesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def see_how_it_works_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()
    
    self.nudges_console.add_component(SubscriptionDetails())
    form.content_panel.add_component(self)

 

