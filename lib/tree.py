class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    elements_to_check = [self.root]
    while len(elements_to_check):
      element = elements_to_check.pop()
      if element["id"] == id:
        return element
      elements_to_check += element["children"]
