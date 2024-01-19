from ._anvil_designer import SubscriptionPaymentsTemplate
from anvil import *
import anvil.server
from anvil_extras.MessagePill import MessagePill

class SubscriptionPayments(SubscriptionPaymentsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    json_response = anvil.server.call('call_insights_api',
                                      self.account_ID.text,
                                      "lm",
                                      "monthly")

    self.raw_json_response_panel.content = json_response

  def refresh_click(self, **event_args):
    self.account_ID.text=""

  def submit_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    json_response = anvil.server.call('call_insights_api',
                                      self.account_ID.text,
                                      "lm",
                                      "monthly")

    if "Err" in json_response:
        self.flow_panel_4.add_component(MessagePill(message=f"Unable to connect to the Insights API. We're working to fix this. Apologies for the inconvenience.", level="warning"))
    else:
        self.raw_json_response_panel.content = json_response
    