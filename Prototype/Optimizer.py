""" Optimizer
    
    - does optimizations and some transformations
    - doesn't split the Immediate Representation into States! (is done by StateGenerator.py)

    TODO
    - detect /2 /4 /8 /16 /32
    - detect *2
    - detect *3 and so on
"""

from Datatype import *

class Optimizer(object):
   def __init__(self):
      self.ImmediateInstructions = None
      self.Variables = None

   # NOTE< self.ImmediateInstructions must be setted >
   # NOTE< self.Variables must be setted >
   def doOptimization(self):
      #self._analyseVariables()

      # now we check if a variable is a constant (means if it isn't changed)
      #  (if so, we can eleminate the assignment operation(s) and declare it as a constant)
      
      self._analyseConstants()

      for Variable in self.Variables:
         print(["not written jet", "one time written", "variable"][Variable["status"]])
         print(Variable["constValue"])
         print("---")

      if self._checkForVariableDivision():
         print("Error: Division by Variable detected!")
         return False

      self._removeConstantAssignments()

      # we transfrom all multiplications with 2 or some constant to equivalent faster code
      self._optimizeMultiplications()

      # transform all additions with 1 to inc operations
      # this is needed for the next step
      self._transfromAddition()

      # this fuses additions and inc's
      self._fuseAdditionAndIncrement()

      # this tries to optimize (conditional) jump to jump situations
      CalleeSuccess = self._optimizeJumpToJump()
      if not CalleeSuccess:
         return False

      return True


   # this method looks which instruction writes to a variable
   # NOTE< self.ImmediateInstructions must be setted >

   # NOTE< currently not called >
   def _analyseVariables(self):
      for ImmediateInstruction in self.ImmediateInstructions:
         if   ImmediateInstruction.Type == 2: # assign constant to variable
            self.Variables[ImmediateInstruction.Variable]["writtenBy"].append(ImmediateInstruction.Id)
         elif ImmediateInstruction.Type >= 3 and ImmediateInstruction.Type <= 9:
            self.Variables[ImmediateInstruction.Destination]["writtenBy"].append(ImmediateInstruction.Id)
         else:
            # nothing

            pass

   # this removes all "assign constant to variable" instructions that assign to constants

   def _removeConstantAssignments(self):
      i = 0

      while i < len(self.ImmediateInstructions):
         if self.ImmediateInstructions[i].Type == 2: # assign constant to variable
            if self.Variables[self.ImmediateInstructions[i].Variable]["status"] == 1:
               del self.ImmediateInstructions[i]
               i -= 1

         i += 1

   # this cheks if the user divided by a variable
   # is used to alert the user if he divides by an variable
   # returns True or False

   def _checkForVariableDivision(self):
      for Instruction in self.ImmediateInstructions:
         if Instruction.Type == 4 and self.Variables[Instruction.B]["status"] == 2:
            return True

      return False

   # this method checks which variable is in reality a constant
   # NOTE< self.ImmediateInstructions must be setted >
   def _analyseConstants(self):
      for ImmediateInstruction in self.ImmediateInstructions:
         if   ImmediateInstruction.Type == 2: # assign constant to variable
            if   self.Variables[ImmediateInstruction.Variable]["status"] == 0: # if nothing got written jet to the variable
               self.Variables[ImmediateInstruction.Variable]["status"] = 1 # only one time something got written to it
               self.Variables[ImmediateInstruction.Variable]["constValue"] = ImmediateInstruction.Value
            
            elif self.Variables[ImmediateInstruction.Variable]["status"] == 1: # if only one time a constant value got written to it
               if ImmediateInstruction.Value != self.Variables[ImmediateInstruction.Variable]["constValue"]:
                  # if the value was changed

                  self.Variables[ImmediateInstruction.Variable]["status"] = 2 # it is a normal variable
            elif self.Variables[ImmediateInstruction.Variable]["status"] == 2: # if it is a variable
               pass # we do nothing
         elif  ImmediateInstruction.Type >= 3 and ImmediateInstruction.Type <= 9:
            self.Variables[ImmediateInstruction.Destination]["status"] = 2

   # NOTE< _analyzeConstants must have been called before this! >

   # this transforms any multiplication with a constant into a shift or a shift and add combination
   def _optimizeMultiplications(self):
      i = 0

      while i < len(self.ImmediateInstructions):
         if self.ImmediateInstructions[i].Type == 7: # if it is a multiplication
            if   self.Variables[ self.ImmediateInstructions[i].A ]["status"] == 1: # one time a const written to it

               # if it gets multiplied by 2 the other operand is unsigned
               if (self.Variables[ self.ImmediateInstructions[i].A ]["constValue"] == 2) and \
                  (self.Variables[ self.ImmediateInstructions[i].B ]["typeInfo"].BaseType == Datatype.EnumBasetype.UNSIGNED): 
                  
                  # ...
                  # we replace the instruction with a shift instruction

                  Source      = self.ImmediateInstructions[i].B
                  Destination = self.ImmediateInstructions[i].Destination

                  self.ImmediateInstructions[i].Type        = 9 # shift left const
                  self.ImmediateInstructions[i].Source      = Source
                  self.ImmediateInstructions[i].Destination = Destination
                  self.ImmediateInstructions[i].Bits        = 1

            elif self.Variables[ self.ImmediateInstructions[i].B ]["status"] == 1: # one time a const written to it

               # if it gets multiplied by 2 the other operand is unsigned 
               if (self.Variables[ self.ImmediateInstructions[i].B ]["constValue"] == 2) and \
                  (self.Variables[ self.ImmediateInstructions[i].A ]["typeInfo"].BaseType == Datatype.EnumBasetype.UNSIGNED):
                  # we replace the instruction with a shift instruction

                  Source      = self.ImmediateInstructions[i].A
                  Destination = self.ImmediateInstructions[i].Destination

                  self.ImmediateInstructions[i].Type        = 9 # shift left const
                  self.ImmediateInstructions[i].Source      = Source
                  self.ImmediateInstructions[i].Destination = Destination
                  self.ImmediateInstructions[i].Bits        = 1

            else:
               pass # nothing done

         i += 1

   # this transforms all additions +1 into inc operations
   def _transfromAddition(self):
      i = 0

      while i < len(self.ImmediateInstructions):
         # check if it is an addition
         if (self.ImmediateInstructions[i].Type == 6) and (not self.ImmediateInstructions[i].StaticCarry) and (not self.ImmediateInstructions[i].CarryVariableActive):
            # check if the operand A is a constant and has the value 1
            if   (self.Variables[ self.ImmediateInstructions[i].A ]["status"] == 1) and \
                 (self.Variables[ self.ImmediateInstructions[i].A ]["constValue"] == 1):
               Operand     = self.ImmediateInstructions[i].B
               Destination = self.ImmediateInstructions[i].Destination

               self.ImmediateInstructions[i].Type = 10 # inc
               self.ImmediateInstructions[i].Operand = Operand
               self.ImmediateInstructions[i].Destination = Destination

            # check if the operand B is a constant and has the value 1
            elif (self.Variables[ self.ImmediateInstructions[i].B ]["status"] == 1) and \
                 (self.Variables[ self.ImmediateInstructions[i].B ]["constValue"] == 1):
               Operand     = self.ImmediateInstructions[i].A
               Destination = self.ImmediateInstructions[i].Destination

               self.ImmediateInstructions[i].Type = 10 # inc
               self.ImmediateInstructions[i].Operand = Operand
               self.ImmediateInstructions[i].Destination = Destination
            # no else
         i += 1

   # this fuses additions and increments

   # TODO< check types of the Variables >
   def _fuseAdditionAndIncrement(self):
      i = 0

      while i < len(self.ImmediateInstructions):
         if i == 0:
            i += 1
            continue

         # check if it is an add operation and if the carry is inactive
         if (self.ImmediateInstructions[i].Type == 6) and \
            (not self.ImmediateInstructions[i].CarryVariableActive) and \
            (not self.ImmediateInstructions[i].StaticCarry) and \
            (self.ImmediateInstructions[i-1].Type == 10):

            # ...

            # search for any instructions that reference "self.ImmediateInstructions[i-1].Destination"
            # if we found it, we can't do the optimisation, because the varibale is again referenced
            Referenced = self._isVariableReferenced(i+1, self.ImmediateInstructions[i-1].Destination)

            # if the variable gets referenced after that, we can't do the optimisation
            if Referenced:
               i += 1
               continue

            if   (self.ImmediateInstructions[i-1].Destination == self.ImmediateInstructions[i].B):
               self.ImmediateInstructions[i].B = self.ImmediateInstructions[i-1].Operand
               self.ImmediateInstructions[i].StaticCarry = True
               
               # remove inc operation
               del self.ImmediateInstructions[i-1]

               # fix i
               i -= 1

            elif (self.ImmediateInstructions[i-1].Destination == self.ImmediateInstructions[i].A):
               self.ImmediateInstructions[i].A = self.ImmediateInstructions[i-1].Operand
               self.ImmediateInstructions[i].StaticCarry = True
               
               # remove inc operation
               del self.ImmediateInstructions[i-1]

               # fix i
               i -= 1               

         i += 1

   # this tries to optimize (conditional) jump to jump situations
   # returns True if no error occured or False if it did
   def _optimizeJumpToJump(self):
      i = 0

      while i < len(self.ImmediateInstructions):
         if (self.ImmediateInstructions[i].Type == 12): # if it is an if
            TrueLabelId  = self.ImmediateInstructions[i].TrueLabelId
            FalseLabelId = self.ImmediateInstructions[i].FalseLabelId

            # for the TrueLabelId
            (Found, InstructionIndex) = self._findLabel(TrueLabelId)

            if not Found:
               return False

            InstructionIndexAfterLabel = InstructionIndex + 1


            # if the instruction is a goto and
            # if the instruction is not referenced anywhere else
            if (InstructionIndexAfterLabel < len(self.ImmediateInstructions)) and \
               (self.ImmediateInstructions[InstructionIndexAfterLabel].Type == 1) and \
               (not self._otherJumpsToLabel(i, TrueLabelId)):
               
               # ...

               # if so, we exchange the labels (the goto LabelId goes into the TrueLabelId)
               # and we remove the label and the goto

               self.ImmediateInstructions[i].TrueLabelId = self.ImmediateInstructions[InstructionIndexAfterLabel].LabelId
               del self.ImmediateInstructions[InstructionIndex]
               del self.ImmediateInstructions[InstructionIndex]


            # for the FalseLabelId
            (Found, InstructionIndex) = self._findLabel(FalseLabelId)

            if not Found:
               return False

            InstructionIndexAfterLabel = InstructionIndex + 1


            # if the instruction is a goto and
            # if the instruction is not referenced anywhere else
            if (InstructionIndexAfterLabel < len(self.ImmediateInstructions)) and \
               (self.ImmediateInstructions[InstructionIndexAfterLabel].Type == 1) and \
               (not self._otherJumpsToLabel(i, FalseLabelId)):
               
               # ...

               # if so, we exchange the labels (the goto LabelId goes into the TrueLabelId)
               # and we remove the label and the goto

               self.ImmediateInstructions[i].FalseLabelId = self.ImmediateInstructions[InstructionIndexAfterLabel].LabelId
               del self.ImmediateInstructions[InstructionIndex]
               del self.ImmediateInstructions[InstructionIndex]

         i += 1

      return True

   # ---
   # helper methods
   # ---

   # searches for a referencing of a variable after the position
   def _isVariableReferenced(self, Position, VariableId):
      i = Position

      while i < len(self.ImmediateInstructions):
         if   (self.ImmediateInstructions[i].Type == 3) or \
              (self.ImmediateInstructions[i].Type == 4) or \
              (self.ImmediateInstructions[i].Type == 6) or \
              (self.ImmediateInstructions[i].Type == 7):
            # ...
            if (self.ImmediateInstructions[i].A == VariableId) or \
               (self.ImmediateInstructions[i].B == VariableId):
               #...
               return True
            # no else

         # check for move, shift, inc, dec
         elif (self.ImmediateInstructions[i].Type ==  5) or \
              (self.ImmediateInstructions[i].Type ==  8) or \
              (self.ImmediateInstructions[i].Type ==  9) or \
              (self.ImmediateInstructions[i].Type == 10) or \
              (self.ImmediateInstructions[i].Type == 11):
            #...
            if self.ImmediateInstructions[i].Source == VariableId:
               return True
            # no else

         # no else

         i += 1

      return False

   # is any instruction jumping to the LabelId except "except"?
   def _otherJumpsToLabel(self, Except, LabelId):

      i = Except + 1

      while i < len(self.ImmediateInstructions):
         Instruction = self.ImmediateInstructions[i]

         # if it is a goto and the Destination is the Label
         if   (Instruction.Type == 1) and \
              (Instruction.LabelId == LabelId):
            return True

         # if it is a if instruction and TrueLabelId or FalseLabelId are equal to the LabelId
         elif   (Instruction.Type == 12) and \
              ( (Instruction.TrueLabelId == LabelId) or (Instruction.FalseLabelId == LabelId) ):
            return True

         i += 1

      i = Except - 1

      while True:
         if i == -1:
            return False

         Instruction = self.ImmediateInstructions[i]

         # if it is a goto and the Destination is the Label
         if   (Instruction.Type == 1) and \
              (Instruction.LabelId == LabelId):
            return True

         # if it is a if instruction and TrueLabelId or FalseLabelId are equal to the LabelId
         elif   (Instruction.Type == 12) and \
              ( (Instruction.TrueLabelId == LabelId) or (Instruction.FalseLabelId == LabelId) ):
            return True

         i =- 1

      return False

   # searches for the (index) of the label instruction for the LabelId
   # return (Found, Index)
   def _findLabel(self, LabelId):
      i = 0

      while i < len(self.ImmediateInstructions):
         # if it is a label and the labelId is equal
         if (self.ImmediateInstructions[i].Type == 0) and (self.ImmediateInstructions[i].LabelId == LabelId):
            return (True, i)

         i += 1

      return (False, 0)
