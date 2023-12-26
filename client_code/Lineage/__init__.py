from ._anvil_designer import LineageTemplate
from anvil import *
import anvil.server
# Rest of your code remains unchanged
# import tkinter as tk
# from tkinter import ttk

class Lineage(LineageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Synthetic data
    self.data = {
        'source_fcn': ['A', 'A', 'B', 'C', 'C', 'D'],
        'target_fcn': ['B', 'C', 'D', 'E', 'F', 'G']
    }

    # Create a DataFrame
    self.df = pd.DataFrame(self.data)
    # Initialize tkinter

#   # Define a function to perform depth-first search
#   def source_dfs(self, source, parent_item):
#       children = self.df[self.df['target_fcn'] == source]['source_fcn'].tolist()
#       visited.add(source)
#       for child in children:
#           if child not in visited:
#               child_item = tree.insert(parent_item, 'end', text=child)
#               source_dfs(child, child_item)

#   def target_dfs(self, target, parent_item):
#       parents = self.df[self.df['source_fcn'] == target]['target_fcn'].tolist()
#       visited.add(target)
#       for parent in parents:
#           if parent not in visited:
#               child_item = tree.insert(parent_item, 'end', text=parent)
#               target_dfs(parent, child_item)

#   # Define a function to start the source search
#   def start_source_search(self):
#       tree.delete(*tree.get_children())
#       source = source_entry.get()
#       root_item = tree.insert("", 'end', text=source)
#       global visited
#       visited = set()
#       source_dfs(source, root_item)

#   def start_target_search(self):
#       tree.delete(*tree.get_children())
#       target = source_entry.get()
#       root_item = tree.insert("", 'end', text=target)
#       global visited
#       visited = set()
#       target_dfs(target, root_item)
#       tree.see(root_item)

# root = tk.Tk()
# root.title("Lineage Extraction")
# root.configure(bg='#FFFFFF')

# # Add an entry field for user input
# source_label = ttk.Label(root, text="Enter Table:", background='#FFFFFF')
# source_label.pack()

# source_entry = ttk.Entry(root)
# source_entry.pack()

# button_frame = ttk.Frame(root)
# button_frame.pack(side="top")

# source_button = ttk.Button(button_frame, text="Start Source Search", command=start_source_search)
# source_button.pack(side="left")

# target_button = ttk.Button(button_frame, text="Start Target Search", command=start_target_search)
# target_button.pack(side="right")

# # Create a treeview widget
# tree = ttk.Treeview(root)
# tree.heading("#0", text="Lineage")

# #Scrollbar setup
# tree_scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
# tree.configure(yscroll=tree_scrollbar.set)
# tree_scrollbar.pack(side="right", fill="y")

# tree.pack(side="left", fill="both", expand=True)

# # Start the tkinter main loop
# root.mainloop()
