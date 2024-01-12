from ._anvil_designer import TxnEnrichmentTemplate
from anvil import *
import anvil.server
from .Response import Response
from .RawJsonResponse import RawJsonResponse
from ..MCCs import MCCs
import json
import anvil.js
from anvil_extras.MessagePill import MessagePill


class TxnEnrichment(TxnEnrichmentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
   
  def enrich_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.response_panel.clear()

    #json_response = RawJsonResponse()
    json_data = anvil.server.call('call_txn_api', self.descriptor.text, self.amount_input.text)

    response = Response()

    if json_data.get('enrichedTransactions'):

       transaction = json_data['enrichedTransactions'][0]
       response.merchant.text = transaction['merchant']['name'] if transaction.get('merchant') else "n/a"
       response.category.text = transaction['categorization']['category'] if transaction.get('categorization') else "n/a"
       response.subcategory.text = transaction['categorization']['subCategory'] if transaction.get('categorization') else "n/a"
       response.channel.text = transaction.get('channel')
       response.tags.text = transaction['categorization']['tags'] if transaction.get('categorization') and transaction['categorization'].get('tags') else "n/a"
       response.subscription.text = transaction.get('subscription')
       response.amount.text = "$"+str(transaction['transaction']['amount']) if transaction.get('transaction') else "n/a"

       response.website.text = transaction['merchant']['website'] if transaction['merchant'].get('website') else "n/a"
       response.state.text = transaction['merchant']['location']['state'] if transaction['merchant']['location'].get('state') else "n/a"
       response.third_party.text = "n/a"

       response.merchant_header.text = response.merchant.text
       self.response_panel.add_component(response, width=638.4)
    else:
      self.response_panel.add_component(MessagePill(message=json_data), width=638.4)

    
    form.content_panel.add_component(self)


  #def mcc_footer_click(self, **event_args):
   # form = get_open_form()
    #form.content_panel.clear()
    #form.content_panel.add_component(MCCs())

  
  
  def mcc_footer_click(self, **event_args):
      # Replace 'your_html_file.html' with the name of your HTML asset
      url = anvil.server.get_app_origin() + "/_/theme/mcc_list.html"
      anvil.js.window.open(url, "_blank")

  def refresh_click(self, **event_args):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(TxnEnrichment())
