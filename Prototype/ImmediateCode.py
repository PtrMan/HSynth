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
      NewInstruction = ImmediateInstruction(0, self.ImmediateInstructionCounter)
      NewInstruction.LabelId = Id

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeGoto(self, Id):
      NewInstruction = ImmediateInstruction(1, self.ImmediateInstructionCounter)
      NewInstruction.LabelId = Id

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   # A and B are Variable Id's
   def writeAdd(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(6, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination
      NewInstruction.StaticCarry = False

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   # A and B are Variable Id's
   def writeSub(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(3, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination;

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   def writeDiv(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(4, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeMul(self, A, B, Destination):
      NewInstruction = ImmediateInstruction(7, self.ImmediateInstructionCounter)
      NewInstruction.A = A
      NewInstruction.B = B
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1      


   def writeMov(self, Destination, Source):
      NewInstruction = ImmediateInstruction(5, self.ImmediateInstructionCounter)
      NewInstruction.Source      = Source
      NewInstruction.Destination = Destination

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1


   def writeConstAssigment(self, Variable, Value):
      NewInstruction = ImmediateInstruction(2, self.ImmediateInstructionCounter)
      NewInstruction.Variable = Variable
      NewInstruction.Value    = Value

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeIf(self, A, B, IfType, TrueLabelId, FalseLabelId):
      NewInstruction = ImmediateInstruction(12, self.ImmediateInstructionCounter)
      NewInstruction.IfType       = IfType
      NewInstruction.A            = A
      NewInstruction.B            = B
      NewInstruction.TrueLabelId  = TrueLabelId
      NewInstruction.FalseLabelId = FalseLabelId

      self.ImmCodeData.append(NewInstruction)
      self.ImmediateInstructionCounter += 1

   def writeInc(self, Operand, Destination):
      NewInstruction = ImmediateInstruction(10, self.ImmediateInstructionCounter)
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
