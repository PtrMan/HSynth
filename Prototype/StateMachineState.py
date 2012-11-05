# represents a state of a statemachine

class StateMachineState:
   def __init__(self):
      # contains all instructions of that state
      self.ImmediateInstructions = []

      # Array of True/False that decides for each variable if the variable should be keeped
      self.KeepVariables = []

   