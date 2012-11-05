class ImmediateInstruction(object):
   # type:
   #   0   label
   #       LabelId   the id of the label

   #   1   goto label
   #       LabelId   the id of the label it should jump to

   #   2   assign constant to variable
   #       Variable  the id of th variable
   #       Value     the value to be assigned

   #   3   sub
   #       A
   #       B
   #       Destination

   #   4   div
   #       A
   #       B
   #       Destination

   #   5   mov
   #       Source
   #       Destionation

   #   6   add
   #       A
   #       B
   #       Destination
   #       StaticCarry         if this is true everytime a addition is made +1 is added
   #       TODO CarryVariableActive  if this is set, this variable is used as carry
   #       TODO CarryVariable

   #   7   mul
   #       A
   #       B
   #       Destination

   #   8   shift Right const
   #       (only emitted by optimizer)
   #       
   #       Source
   #       Destination
   #       Bits

   #   9   shift Left const
   #       (only emitted by optimizer)
   #
   #       Source
   #       Destination
   #       Bits

   #  10   inc
   #       Operand
   #       Destination

   #  11   dec
   #       Operand
   #       Destination

   #  12   if                   if this condition is true, we jump to the 'TrueLabelId', else to the 'FalseLabelId'
   #       IfType
   #       0 : greater or equal
   #       TODO< other >
   #       TrueLabelId
   #       FalseLabelId
   #       A                   the variable id of the first Variable
   #       B                   the variable id of the secound Variable

   TypeText = ["label", "goto", "assignConst", "sub", "div", "mov", "add", "mul", "shiftRightConst", "shiftLeftConst", "inc", "dec", "if"]

   def __init__(self, Type, Id):
      self.Id = Id
      self.Type = Type
      self.A = 0
      self.B = 0
      self.Source = 0
      self.LabelId = 0
      self.Variable = 0
      self.Value = 0
      self.Destination = 0
      self.Bits = 0
      self.StaticCarry = False
      self.CarryVariableActive = False
      self.IfType = 0
      self.TrueLabelId = 0
      self.FalseLabelId = 0

   def debug(self):
      Return  = "Type         : " + ImmediateInstruction.TypeText[self.Type] + "\n"

      if   self.Type == 0: # label
         Return += "Label Id     : {0}\n".format(self.LabelId)
      elif self.Type == 1: # goto
         Return += "Label Id     : {0}\n".format(self.LabelId)
      elif self.Type == 2: # assignConst
         Return += "Variable     : {0}\n".format(self.Variable)
         Return += "Value        : {0}\n".format(self.Value)
      elif (self.Type == 3) or (self.Type == 4) or (self.Type == 6) or (self.Type == 7): # Three Operand Operation
         Return += "A            : {0}\n".format(self.A)
         Return += "B            : {0}\n".format(self.B)
         Return += "Destination  : {0}\n".format(self.Destination)

         if (self.Type == 6):
            Return += "Static Carry : {0}\n".format(str(self.StaticCarry))

      elif self.Type == 5:
         Return += "Source       : {0}\n".format(self.Source)
         Return += "Destination  : {0}\n".format(self.Destination)
      elif self.Type == 9:
         Return += "Source       : {0}\n".format(self.Source)
         Return += "Destination  : {0}\n".format(self.Destination)
         Return += "Bits         : {0}\n".format(self.Bits)
      elif self.Type == 10:
         Return += "Operand      : {0}\n".format(self.Operand)
         Return += "Destination  : {0}\n".format(self.Destination)
      elif self.Type == 12:
         Return += "Type         : {0}\n".format(["greater or equal"][self.IfType])
         Return += "TrueLabelId  : {0}\n".format(self.TrueLabelId)
         Return += "FalseLabelId : {0}\n".format(self.FalseLabelId)
         Return += "A            : {0}\n".format(self.A)
         Return += "B            : {0}\n".format(self.B)
         
      else:
         Return += "?\n"
      Return += "===\n"

      return Return
