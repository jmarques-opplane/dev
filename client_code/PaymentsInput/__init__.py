from ._anvil_designer import PaymentsInputTemplate
from anvil import *
import anvil.server
from ..NudgesInput import NudgesInput

class PaymentsInput(PaymentsInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def see_how_it_works_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    form.content_panel.add_component(NudgesInput())
