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

  def see_how_it_works_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(NudgesInput())

  def payments_button_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(PaymentsInput())
    pass

  def data_lineage_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(ExplainabilityConsole_2())
 
