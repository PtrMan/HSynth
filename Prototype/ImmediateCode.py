from ImmediateInstruction import *

class ImmediateCode(object):
   def __init__(self):
      self.ImmCodeData = []
      self.ImmediateInstructionCounter = 0

      self.LabelId = 0

      # Variables
      # contains dicts with
      # "typeInfo"    Infos about the Datatype, is a 'Datatype' object
      # "writtenBy"   list with ID's of the Instructions that write to this variable
      # "status"      is it a constant?
      #               0 : not written to jet
      #               1 : one time a const written to it
      #               2 : variable
      # "constValue"  Is the value of the constant
      #               TODO< what aboutsigned types? >
      self.Variables = []



   # TODO< Debug it into a stream? >
   def debugImmediateCode(self, ImmediateCodeList):
      Return = ""

      for Immediate in ImmediateCodeList:
         Return += Immediate.debug()

      return Return

   def getNewLableIdentifier(self):
      self.LabelId += 1

      return self.LabelId

   def writeLable(self, Id):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.LABEL, self.ImmediateInstructionCounter)
      NewInstruction.LabelId = Id

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeGoto(self, Id):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.GOTOLABEL, self.ImmediateInstructionCounter)
      NewInstruction.LabelId = Id

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   # A and B are Variable Id's
   def writeAdd(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.ADD, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination
      NewInstruction.StaticCarry = False

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   # A and B are Variable Id's
   def writeSub(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.SUB, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination;

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   def writeDiv(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.DIV, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeMul(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.MUL, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1      


   def writeMov(self, Destination, Source):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.MOV, self.ImmediateInstructionCounter)
      NewInstruction.Source      = Source
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   def writeConstAssigment(self, Variable, Value):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.ASSIGNCONST, self.ImmediateInstructionCounter)
      NewInstruction.Variable = Variable
      NewInstruction.Value    = Value

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeIf(self, A, B, IfType, TrueLabelId, FalseLabelId):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.IF, self.ImmediateInstructionCounter)
      NewInstruction.IfType       = IfType
      NewInstruction.A            = A
      NewInstruction.B            = B
      NewInstruction.TrueLabelId  = TrueLabelId
      NewInstruction.FalseLabelId = FalseLabelId

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeInc(self, Operand, Destination):
      NewInstruction = ImmediateInstruction(ImmediateInstruction.EnumType.INC, self.ImmediateInstructionCounter)
      NewInstruction.Operand     = Operand
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   # tries to allocate a new space for a variable
   def allocateVariable(self, DatatypeInfo):
      NewVar = {}
      
      NewVar["typeInfo"] = DatatypeInfo
      NewVar["writtenBy"] = []
      NewVar["status"] = 0
      NewVar["constValue"] = 0

      self.Variables.append(NewVar)

      return len(self.Variables)-1
