class DAGElement(object):
   class EnumOperationType:
      ADD = 0
      SUB = 1
      MUL = 2
      DIV = 3
      VAR = 4
      MOV = 5 # moves from NodeA to VarId (VarId is the destination variable)
      FLIPFLOP = 6 # a flipflop stage, is added to ease the creation of the logic

   StringsOperationType = ["ADD", "SUB", "MUL", "DIV", "VAR", "MOV"]

   def __init__(self, OperationType):
      self.NodeA = None
      self.NodeB = None
      self.OperationType = OperationType
      self.VarId = 0
      self.IsOutput = False # not needed????

   def debug(self):
      Return = ""

      Return += "Type: {0}\n".format(DAGElement.StringsOperationType[self.OperationType])

      if (self.OperationType == DAGElement.EnumOperationType.ADD) or \
         (self.OperationType == DAGElement.EnumOperationType.SUB) or \
         (self.OperationType == DAGElement.EnumOperationType.MUL) or \
         (self.OperationType == DAGElement.EnumOperationType.DIV):

         # ...
         Return += "NodeA: {0}\n".format(self.NodeA)
         Return += "NodeB: {0}\n".format(self.NodeB)

         if self.IsOutput:
            Return += "Output Var Id: {0}\n".format(self.VarId)
      
      elif self.OperationType == DAGElement.EnumOperationType.VAR:
         Return += "VarId: {0}\n".format(self.VarId)

      elif self.OperationType == DAGElement.EnumOperationType.MOV:
         Return += "NodeA: {0}\n".format(self.NodeA)
         Return += "VarId: {0}\n".format(self.NodeB)

      Return += "---\n"

      return Return
