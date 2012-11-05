
class Backend(object):
   def __init__(self):
      self.ImmediateInstructions = None
      self.Variables = None

      # contain only StateMachineState Objects
      self.StateMachineStates = []

      # list with {"labelId":..., "state":...} objects that describe which label is represented by which state
      self.LabelToState = []

   # returns a bool, false on failture
   def transform(self):
      CalleeSuccess = self._transformInstructionsIntoStates()
      if not CalleeSuccess:
         return False

      # TODO< fold states that don't depend upon each other (leaveraging parallism) >

      # check which state change variables and write it out
      self._checkVariableChanges()

      # emit vhdl code
      CalleeSuccess = self._generateVhdlCode()
      if not CalleeSuccess:
         return False

      return True

   # returns a bool, false on failture
   def _transformInstructionsIntoStates(self):
      for Instruction in self.ImmediateInstructions:
         if Instruction.Type == 0: # label
            NewLabelToState = {}
            NewLabelToState["labelId"] = Instruction.labelId
            NewLabelToState["state"]   = len(self.StateMachineStates)

            self.LabelToState.append(NewLabelToState)
         else:
            NewState = StateMachineState()
            NewState.ImmediateInstructions.append(Instruction)

      return True

   def _checkVariableChanges(self):
      # create a array that represent no change of an variable
      NoChangedVariables = []

      i = 0

      while i < self.Variables:
         NoChangedVariables.append(True)

         i += 1

      i = 0

      while i < self.StateMachineStates:
         # fill in no change of the Variables
         self.StateMachineStates[i].KeepVariables = NoChangedVariables

         for Instruction in self.StateMachineStates[i].ImmediateInstructions:
            if   Instruction.Type == 2:  # assign constant to variable
               self.StateMachineStates[i].KeepVariables[ Instruction.variable ] = False
            
            # if it is a sub, div, mov, add, mul, shift, inc, dec operation
            elif (Instruction.Type ==  3) or \
                 (Instruction.Type ==  4) or \
                 (Instruction.Type ==  5) or \
                 (Instruction.Type ==  6) or \
                 (Instruction.Type ==  7) or \
                 (Instruction.Type ==  8) or \
                 (Instruction.Type ==  9) or \
                 (Instruction.Type == 10) or \
                 (Instruction.Type == 11):

               # ...
               self.StateMachineStates[i].KeepVariables[ Instruction.Destination ] = False

            # no else

         i += 1

   # return a Boolean Value, false if an error has happend
   def _generateVhdlCode(self):
      Output = ""
      
      Output += "architecture arch0 of x is\n"
      # TODO    type stateType is()

      i = 0

      for Variable in self.Variables:
         if Variable["type"] != 0: # if it is unsigned
            # TODO
            return False

         if Variable["status"] == 2:
            Output += "   signal signal{0}    : unsigned({1} downto 0) := to_unsigned(0, {2});\n".format(i, Variable["bits"]-1, Variable["bits"])
            Output += "   signal nextSignal{0}: unsigned({1} downto 0) := to_unsigned(0, {2});\n".format(i, Variable["bits"]-1, Variable["bits"])
         elif Variable["status"] == 1:
            Output += "   signal signal{0}    : unsigned({1} downto 0) := to_unsigned({2}, {3});\n".format(i, Variable["bits"]-1, Variable["constValue"], Variable["bits"])

         Output += "\n"

         i += 1

      Output += "begin\n"

      Output += "   -- next state logic\n"
      Output += "   nextStateLogic: process(state, TODO)\n"
      Output += "   begin\n"
      Output += "      case state is\n"

      i = 0


      for State in self.StateMachineStates:
         
         Output += "         when s{0} =>\n".format(i)

         # TODO

         i += 1

      Output += "      end case state;\n"
      Output += "   end process nextStateLogic;\n"

      # TODO< next variable logic >

      Output += "end arch0;\n"

      return True