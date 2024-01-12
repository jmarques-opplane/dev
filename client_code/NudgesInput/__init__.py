from ._anvil_designer import NudgesInputTemplate
from anvil import *
import anvil.server
from ..NudgesOutput import NudgesOutput
from anvil_extras.MessagePill import MessagePill


class NudgesInput(NudgesInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

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
    get_open_form().content_panel.add_component(NudgesInput())

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
        nudges_output.raw_json_response_panel.add_component(MessagePill(message=json_response, level="info"))
    else:
        nudges_output.raw_json_response_panel.content = json_response
    
    form.content_panel.add_component(nudges_output)

 
