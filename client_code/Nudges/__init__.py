from ._anvil_designer import NudgesTemplate
from anvil import *
import anvil.server

class Nudges(NudgesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

 

