from ._anvil_designer import SubscriptionDetailsTemplate
from anvil import *
import anvil.server

class SubscriptionDetails(SubscriptionDetailsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
