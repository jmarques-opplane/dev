from ._anvil_designer import ExplainabilityConsoleTemplate
from anvil import *
import anvil.server
from ..ExplainabilityConsole2 import ExplainabilityConsole2

class ExplainabilityConsole(ExplainabilityConsoleTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def data_lineage_click(self, **event_args):
    self.parent.linear_panel.content_panel.clear()
    self.parent.linear_panel.content_panel.add_component(ExplainabilityConsole2())