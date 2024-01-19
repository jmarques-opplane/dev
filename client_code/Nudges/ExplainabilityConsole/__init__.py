from ._anvil_designer import ExplainabilityConsoleTemplate
from anvil import *
import anvil.server

class ExplainabilityConsole(ExplainabilityConsoleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def data_lineage_click(self, **event_args):
    form = get_open_form()
