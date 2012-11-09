class DAGElement(object):
   class EnumOperationType:
      ADD = 1
      SUB = 2
      MUL = 3
      DIV = 4
      VAR = 5
      MOV = 6 # moves from NodeA to VarId (VarId is the destination variable)

   def __init__(self, OperationType):
      self.NodeA = None
      self.NodeB = None
      self.OperationType = OperationType
      self.VarId = 0
      self.IsOutput = False
