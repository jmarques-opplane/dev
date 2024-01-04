from ._anvil_designer import TxnEnrichmentTemplate
from anvil import *
import anvil.server
from .Response import Response
from .RawJsonResponse import RawJsonResponse

class TxnEnrichment(TxnEnrichmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def enrich_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.response_panel.clear()

    json_response = RawJsonResponse()
    json_response.raw_json_response.content = anvil.server.call('call_txn_api', self.descriptor.text)

    self.response_panel.add_component(json_response, width=638.4)
    form.content_panel.add_component(self)


  def outlined_button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
