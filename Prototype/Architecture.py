import functools

from Dag import *
from FlowChart import *
from ImmediateInstruction import *

class Architecture(object):
   def __init__(self):
      self.ImmediateCodeOptimized = []
      self.VariablesOptimized     = []
      self.FlowChartObj = FlowChart()

   # returns a (Success boolean, string error message)
   def generateParallelDesign(self):
      if self._notParallelisizableInstructions():
         return (False, "Immediate Instructions contain a not parallelisizable Instruction")

      # this is a array with the state if the variable was used in this DAG of this Block
      VariableUsedInDag = [False] * len(self.VariablesOptimized)
      # the Index in the Dag content where the variables was defined
      VariableIndexInDag = [0] * len(self.VariablesOptimized)

      BlockDag = DAG()

      # we translate with this the Code of the Block into one Dag where we can do some optimisations
      # and we can with the help of the optimized Dag schedule the Dataflow
      
      for Instruction in self.ImmediateCodeOptimized:
         if   Instruction.Type == ImmediateInstruction.EnumType.ASSIGNCONST:
            return (False, "TODO!")

         elif (Instruction.Type == ImmediateInstruction.EnumType.ADD) or \
              (Instruction.Type == ImmediateInstruction.EnumType.SUB) or \
              (Instruction.Type == ImmediateInstruction.EnumType.MUL) or \
              (Instruction.Type == ImmediateInstruction.EnumType.DIV):
            
            # ...
            DagIndexA = 0
            DagIndexB = 0

            if not VariableUsedInDag[ Instruction.A ]:
               DagIndexA = BlockDag.addVariable(Instruction.A, False)
               VariableUsedInDag[ Instruction.A ] = True
               VariableIndexInDag[ Instruction.A ] = DagIndexA
            else:
               DagIndexA = VariableIndexInDag[ Instruction.A ]

            if not VariableUsedInDag[ Instruction.B ]:
               DagIndexB = BlockDag.addVariable(Instruction.B, False)
               VariableUsedInDag[ Instruction.B ] = True
               VariableIndexInDag[ Instruction.B ] = DagIndexB
            else:
               DagIndexB = VariableIndexInDag[ Instruction.B ]

            DagOperationType = 0

            if   Instruction.Type == ImmediateInstruction.EnumType.ADD:
               DagOperationType = DAGElement.EnumOperationType.ADD
            elif Instruction.Type == ImmediateInstruction.EnumType.SUB:
               DagOperationType = DAGElement.EnumOperationType.SUB
            elif Instruction.Type == ImmediateInstruction.EnumType.MUL:
               DagOperationType = DAGElement.EnumOperationType.MUL
            elif Instruction.Type == ImmediateInstruction.EnumType.DIV:
               DagOperationType = DAGElement.EnumOperationType.DIV
            else:
               return (False, "internal Error!")

            DagIndexInstruction = BlockDag.addOperation(DagOperationType, DagIndexA, DagIndexB)

            VariableUsedInDag[ Instruction.Destination ] = True
            VariableIndexInDag[ Instruction.Destination ] = DagIndexInstruction

         elif Instruction.Type == ImmediateInstruction.EnumType.MOV:
            if not VariableUsedInDag[ Instruction.Source ]:
               return (False, "Internal Error #0x1337")

            SourceIndexInDag = VariableIndexInDag[ Instruction.Source ]

            DagIndexInstruction = BlockDag.addOperation(DAGElement.EnumOperationType.MOV, SourceIndexInDag)

            VariableUsedInDag[ Instruction.Destination ] = True
            VariableIndexInDag[ Instruction.Destination ] = DagIndexInstruction

         elif Instruction.Type == ImmediateInstruction.EnumType.SHIFTR:

            return (False, "TODO!")
         elif Instruction.Type == ImmediateInstruction.EnumType.SHIFTL:

            return (False, "TODO!")

         elif Instruction.Type == ImmediateInstruction.EnumType.INC:
            return (False, "Internal Error!")
         elif Instruction.Type == ImmediateInstruction.EnumType.DEC:
            return (False, "Internal Error!")
         else:
            return (False, "Internal Error!")


      # TODO< restructure the DAG so that it is more optimized >


      print("Dag 1:")

      DebugString = BlockDag.debug()

      print(DebugString)

      # calculate the Flow chart of the Dag
      FlowChartList = self.FlowChartObj.calcFlowChart(BlockDag)
      
      print("Flow chart")
      print(FlowChartList)

      # now we group the stages of the pipeline

      # classic code
      #StagesCount = 0
      #
      #for FlowChartElement in FlowChartList:
      #   StagesCount = max(FlowChartElement, StagesCount)

      StagesCount = functools.reduce(lambda a,b: max(a, b), FlowChartList)

      # in stages are the index's of the operations in the Dag

      Stages = []

      i = 0
      while i < StagesCount:
         Stages.append([])
         i += 1

      i = 0
      while i < len(BlockDag.Content):
         # if it is a variable we skip it
         if BlockDag.Content[i].OperationType == DAGElement.EnumOperationType.VAR:
            i += 1
            continue

         # TODO< what about MOV? >

         Stages[ FlowChartList[i]-1 ].append(i)

         i += 1

      print(Stages)

      # we now manipulate the DAG and add FlipFlops before each Operation

      OldDagLength = len(BlockDag.Content)

      i = 0
      while i < OldDagLength:
         DagElement = BlockDag.Content[i]

         if (DagElement.OperationType == DAGElement.EnumOperationType.ADD) or \
            (DagElement.OperationType == DAGElement.EnumOperationType.SUB) or \
            (DagElement.OperationType == DAGElement.EnumOperationType.DIV) or \
            (DagElement.OperationType == DAGElement.EnumOperationType.MUL):

            # ...

            # we create for each stage where the data must to be flow througth
            # a FF

            #  for NodeA
            CurrentSourceA = DagElement.NodeA

            j = 0

            while j < ( FlowChartList[i] - FlowChartList[ DagElement.NodeA ] ):
               CurrentSourceA = BlockDag.addOperation(DagElement.EnumOperationType.FLIPFLOP, CurrentSourceA)

               j += 1

            #   update the NodeA
            BlockDag.Content[i].NodeA = CurrentSourceA


            #  for NodeB
            CurrentSourceB = DagElement.NodeB

            j = 0

            while j < ( FlowChartList[i] - FlowChartList[ DagElement.NodeB ] ):
               CurrentSourceB = BlockDag.addOperation(DagElement.EnumOperationType.FLIPFLOP, CurrentSourceB)

               j += 1

            #   update the NodeA
            BlockDag.Content[i].NodeB = CurrentSourceB

         elif DagElement.OperationType == DAGElement.EnumOperationType.VAR:
            # we do nothing
            pass

         elif DAGElement.OperationType == DAGElement.EnumOperationType.MOV:
            # TODO

            return (False, "TODO XXX")

         else:
            return (False, "Internal error")

         i += 1


      FfIds = []

      i = 0
      while i < len(BlockDag.Content):
         FfIds.append(None)

         i += 1

      # TODO< create the VHDL sourcecode ??? >

      VhdlSource  = ""

      # create VHDL for the FlipFlops

      VhdlSource += "   p: process(c)\n"
      VhdlSource += "   begin\n"
      VhdlSource += "      if( c'event and c = '1' ) then\n"

      FfCounter = 0
      i = 0
      while i < len(BlockDag.Content):
         if BlockDag.Content[i].OperationType == DagElement.EnumOperationType.FLIPFLOP:
            VhdlSource += "         OutFF{0} <= InFF{0};\n".format(FfCounter)

            FfIds[i] = FfCounter

            FfCounter += 1

         i += 1

      VhdlSource += "      end if;\n"
      VhdlSource += "   end process;\n"

      VhdlSource += "\n"

      # create VHDL for the operations
      i = 0
      while i < len(BlockDag.Content):
         if (BlockDag.Content[i].OperationType == DagElement.EnumOperationType.ADD) or \
            (BlockDag.Content[i].OperationType == DagElement.EnumOperationType.SUB) or \
            (BlockDag.Content[i].OperationType == DagElement.EnumOperationType.MUL) or \
            (BlockDag.Content[i].OperationType == DagElement.EnumOperationType.DIV):

            # ...
            FFA = FfIds[ BlockDag.Content[i].NodeA ]
            FFB = FfIds[ BlockDag.Content[i].NodeB ]

            if   BlockDag.Content[i].OperationType == DagElement.EnumOperationType.ADD:
               VhdlSource += "   OutSig{0} <= OutFF{1} + OutFF{2}\n".format(i, FFA, FFB)
            elif BlockDag.Content[i].OperationType == DagElement.EnumOperationType.SUB:
               VhdlSource += "   OutSig{0} <= OutFF{1} + OutFF{2}\n".format(i, FFA, FFB)
            elif BlockDag.Content[i].OperationType == DagElement.EnumOperationType.MUL:
               return (False, "Error: Synthesis Error: MUL not allowed!")
            elif BlockDag.Content[i].OperationType == DagElement.EnumOperationType.DIV:
               return (False, "Error: Synthesis Error: DIV not allowed!")
            else:
               return (False, "Internal Error")

         i += 1

      VhdlSource += "\n"

      # create VHDL for the connections

      # TODO

      VhdlSource += "   "


      print(VhdlSource)

      # TODOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

      return (True, None)

   # returns bool that indicates if some instructions of the design are not parallelisizable
   # True  if at least one not parallelisizable Instruction was found
   # Flase if not
   def _notParallelisizableInstructions(self):
      for Instruction in self.ImmediateCodeOptimized:
         if (Instruction.Type == ImmediateInstruction.EnumType.GOTOLABEL) or \
            (Instruction.Type == ImmediateInstruction.EnumType.IF):

            # ...
            return True

      return False
