from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
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
    form.content_panel.add_component(self)
  