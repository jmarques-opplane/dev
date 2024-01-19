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
    if "Err" in json_response:
      self.flow_panel_4.add_component(MessagePill(message=json_response, level="info"))
    else:
      self.raw_json_response_panel.content = json_response


  def refresh_click(self, **event_args):
    self.account_ID.text=""

