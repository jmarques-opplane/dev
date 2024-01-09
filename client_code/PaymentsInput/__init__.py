from ._anvil_designer import PaymentsInputTemplate
from anvil import *
import anvil.server
from ..NudgesInput import NudgesInput
from ..PaymentsOutput import PaymentsOutput

class PaymentsInput(PaymentsInputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def account_ID_pressed_enter(self, **event_args):
    form = get_open_form()
    form.content_panel.clear()
    self.nudges_console.clear()

    payments_output = PaymentsOutput()

    json_response = anvil.server.call('call_payments_api',
                                      self.account_ID.text,
                                      "ly"
                                     )

    payments_output.raw_json_response_panel_copy.content = json_response
    
    form.content_panel.add_component(payments_output)
