from DAGElement import *

# 'Flow chart' for the Operations

class FlowChart(object):
   def __init__(self):
      pass

   # Dag is a 'DAG' object
   def calcFlowChart(self, Dag):
      """
      classic code

      Timing = []
      DagLength = None

      DagLength = len(Dag.Content)

      i = 0
      while i < DagLength:
         Timing.append(0)

         i += 1
      """
      Timing = [0] * len(Dag.Content)

      # change the timing data until it doesn't change anymore

      while True:
         Changed = False

         i = 0
         while i < len(Timing):
            # TODO< add mov path ? >

            if Dag.Content[i].OperationType == DAGElement.EnumOperationType.VAR:
               i += 1
               continue

            NodeA = Dag.Content[i].NodeA
            NodeB = Dag.Content[i].NodeB

            OldTiming = Timing[i]

            Timing[i] = max(Timing[NodeA] + 1, Timing[NodeB] + 1)

            Changed = Changed or (OldTiming != Timing[i])

            i += 1

         if not Changed:
            break

      return Timing
