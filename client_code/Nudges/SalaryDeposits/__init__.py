from ._anvil_designer import SalaryDepositsTemplate
from anvil import *
import anvil.server
from anvil_extras.MessagePill import MessagePill


class SalaryDeposits(SalaryDepositsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def account_ID_pressed_enter(self, **event_args):

    json_response = anvil.server.call('call_payments_api',
                                      self.account_ID.text,
                                      "ly"
                                      )

    self.raw_json_response_panel_copy.content = json_response

  def submit_click(self, **event_args):
    json_response = anvil.server.call('call_payments_api',
                                      self.account_ID.text,
                                      "ly"
                                      )
    self.flow_panel_4.clear()
    self.raw_json_response_panel.content = json_response
    response_panel = self.raw_json_response_panel

    if "Err" in json_response:
      self.flow_panel_4.add_component(MessagePill(message=f"Unable to connect to the Payments API. We're working to fix this. Apologies for the inconvenience.", level="warning"))
    elif (json_response == "Invalid Account ID."):
        self.flow_panel_4.add_component(MessagePill(
            message=f"We're currently unable to process requests with the provided account ID. Please verify the ID and try again.",
            level="info"))
    else:
      self.flow_panel_4.add_component(response_panel)


  def refresh_click(self, **event_args):
    self.flow_panel_4.clear()
    self.account_ID.text=""

