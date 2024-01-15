from ._anvil_designer import Homepage_before_loginTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from ..Insights import Insights
from ..Lineage import Lineage
from ..TxnEnrichment import TxnEnrichment
from ..Overview import Overview
from ..Nudges import Nudges
from ..Login import Login
from ..Homepage import Homepage

class Homepage_before_login(Homepage_before_loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.content_panel.add_component(Login())
    # Any code you write here will run before the form opens.


  def login_click(self, **event_args):
    form = get_open_form()
    form = Homepage()


