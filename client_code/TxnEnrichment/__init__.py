from ._anvil_designer import TxnEnrichmentTemplate
from anvil import *
import anvil.server
import Response

class TxnEnrichment(TxnEnrichmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def enrich_click(self, **event_args):
    form = get_open_form()
    form.content_panel.response_panel.clear()
    response_component = Response()
    form.content_panel.response_panel.add_component(response_component)

  def outlined_button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
