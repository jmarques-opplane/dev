from ._anvil_designer import NudgesInputTemplate
from anvil import *
import anvil.server
from ..NudgesOutput import NudgesOutput
from anvil_extras.MessagePill import MessagePill


class NudgesInput(NudgesInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.account_ID.text = properties['account_ID'] if 'account_ID' in properties else "000d5572aab9fb634534d78a9535189b"

  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    nudges_output = NudgesOutput()

    json_response = anvil.server.call('call_insights_api',
                                      self.account_ID.text,
                                      "lm",
                                      "monthly")

    nudges_output.raw_json_response_panel.content = json_response
    
    form.content_panel.add_component(nudges_output)

  def refresh_click(self, **event_args):
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(NudgesInput(account_ID=""))

  def submit_click(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    nudges_output = NudgesOutput()

    json_response = anvil.server.call('call_insights_api',
                                      self.account_ID.text,
                                      "lm",
                                      "monthly")

    if "Err" in json_response:
        nudges_output.flow_panel_4.add_component(MessagePill(message=f"Unable to connect to the Insights API. We're working to fix this. Apologies for the inconvenience.", level="warning"))
    else:
        nudges_output.raw_json_response_panel.content = json_response
    
    form.content_panel.add_component(nudges_output)

  
