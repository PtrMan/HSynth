from DAGElement import *

class DAG(object):
   def __init__(self):
      # this is the Dag as a list
      # contains only 'DAGElement' objects
      # NOTE< can'T use pointers in the native code for this >
      self.Content = []

   def addOperation(self, OperationType, NodeA, NodeB = None):
      # search for the Operation with the Same Properties

      i = 0

      while i < len(self.Content):
         if (self.Content[i].OperationType == OperationType) and \
            (self.Content[i].NodeA == NodeA) and \
            (self.Content[i].NodeB == NodeB):

            # ...
            return i

         i += 1

      NewElement = DAGElement(OperationType)
      NewElement.NodeA = NodeA
      NewElement.NodeB = NodeB

      self.Content.append(NewElement)

      return i

   # Check : when set this method checks if the Variable was allready Defined/Used 
   def addVariable(self, VarId, Check = True):
      # search for the Operation with the Same Properties

      i = 0

      if Check:
         while i < len(self.Content):
            if (self.Content[i].OperationType == DAGElement.EnumOperationType.VAR) and \
               (self.Content[i].VarId == VarId):

               # ...
               return i

            i += 1
      else:
         i = len(self.Content)

      NewElement = DAGElement(DAGElement.EnumOperationType.VAR)
      NewElement.VarId = VarId

      self.Content.append(NewElement)

      return i

   def debug(self):
      Return = ""

      for Element in self.Content:
         Return += Element.debug()

      return Return

"""
d = DAG()

d.addVariable(0)
d.addVariable(1)
d.addOperation(DAGElement.EnumOperationType.ADD, 0, 1)
LastOp = d.addOperation(DAGElement.EnumOperationType.MUL, 2, 0)

d.Content[LastOp].IsOutput = True
d.Content[LastOp].VarId = 2

print(d.Content)
"""
