from ._anvil_designer import ExplainabilityConsole_1Template
from anvil import *
import anvil.server
from ..NudgesInput import NudgesInput
from ..PaymentsInput import PaymentsInput
from ..ExplainabilityConsole_2 import ExplainabilityConsole_2

class ExplainabilityConsole_1(ExplainabilityConsole_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def data_lineage_click(self, **event_args):
    self.parent.nudges_console.clear()
    
 
