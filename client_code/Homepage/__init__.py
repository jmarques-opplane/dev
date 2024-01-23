from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from ..Lineage import Lineage
from ..TxnEnrichment import TxnEnrichment
from ..Overview import Overview
from ..Nudges import Nudges
from ..Login import Login


class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # self.content_panel.add_component(Login())
    self.sidebar_new_1.dom_nodes['nav-sub-menu-overview'].addEventListener("click",self.overview_click)
    self.sidebar_new_1.dom_nodes['nav-sub-menu-nudges'].addEventListener("click",self.nudges_click)
    self.sidebar_new_1.dom_nodes['nav-sub-menu-txn'].addEventListener("click",self.txn_enrich_click)

    self.content_panel.add_component(Overview())
    self.side_bar.width = "280"
    # Any code you write here will run before the form opens.
    
  def txn_enrich_click(self, event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(TxnEnrichment())
    
  def insights_click(self, event_args):
    """This method is called when the link is clicked"""
    # The top-level form has a component called
    # content_panel. Clear it and put a new Form2() panel there:
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Insights())

  def nudges_click(self, event_args):
    """This method is called when the link is clicked"""
    form = get_open_form()
    form.content_panel.clear()
    nudges = Nudges()
    form.content_panel.add_component(nudges)


  def lineage_click(self, event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Lineage())

  def overview_click(self, event_args):
    """This method is called when the link is clicked"""
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(Overview())
