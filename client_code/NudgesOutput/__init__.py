from ._anvil_designer import NudgesOutputTemplate
from anvil import *
import anvil.server

class NudgesOutput(NudgesOutputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.account_ID.text = properties['account_ID'] if 'account_ID' in properties else "000d5572aab9fb634534d78a9535189b"

  def submit_click(self, **event_args):
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
    get_open_form().content_panel.add_component(NudgesOutput(account_ID=""))
