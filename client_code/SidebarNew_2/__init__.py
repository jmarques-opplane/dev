from ._anvil_designer import SidebarNew_2Template
from anvil import *
import anvil.server

class SidebarNew_2(SidebarNew_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
