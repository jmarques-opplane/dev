from ._anvil_designer import TxnEnrichmentTemplate
import anvil.server

class TxnEnrichment(TxnEnrichmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def submit_click(self, **event_args):
    if self.api_request.text is '' or self.api_request.text is None:
      alert("Missing request")
      return

    resp = anvil.server.call('call_txn_api', self.api_request.text)

    self.api_response.text = resp
