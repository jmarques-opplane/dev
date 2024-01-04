from ._anvil_designer import NudgesOutputTemplate
from anvil import *
import anvil.server


class NudgesOutput(NudgesOutputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  

