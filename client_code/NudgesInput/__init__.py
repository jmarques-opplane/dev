from ._anvil_designer import NudgesInputTemplate
from anvil import *
import anvil.server
from .N


class NudgesInput(NudgesInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()

    form = get_open_form()
    form.content_panel.clear()
    
    nudges_input = NudgesInput()
    form.content_panel.add_component(nudges_input)
    
    pass
