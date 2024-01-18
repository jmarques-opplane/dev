from ._anvil_designer import NudgesNavigationTemplate
from anvil import *
import anvil.server

class NudgesNavigation(NudgesNavigationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.flow_panel_1.w

    # Any code you write here will run before the form opens.

  def subscriptions_payments_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
