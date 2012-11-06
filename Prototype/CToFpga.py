"""
// algorithm for calculating the squareroot

unsigned int Counter = 20;
unsigned int Xn = 5;
unsigned int Number = 500;

while(1)
{
	Counter -= 1;

   Xn = (Xn + Number/Xn) / 2;

   if( Counter == 0 )
   {
      break;
   }
}
"""



from ImmediateCode import *

from Optimizer import *

from Datatype import *

class Generator(object):
   def __init__(self):
      # type:

      # while       begin of a while loop
      #             statement    statement of the header
      #             body         the body of the while loop (is a list)

      # number      (statement) only a number
      #             value        the value of the number

      # TODO< remove this >
      # assigment   asign a new value to a number
      #             variable     the name of the target variable
      #             statement    a statement for the assigment of a new value

      # assigment2       assign the right side to the left
      #                  left          leftside
      #                  right         rightside

      # minusAssigment   -=
      #                  left          leftside
      #                  right         rightside

      # variable         access a variable
      #                  name          the name of the variable

      # mul              multiplication
      #                  left          leftside
      #                  right         rightside

      # div              division
      #                  left          leftside
      #                  right         rightside

      # add              addition
      #                  left          leftside
      #                  right         rightside

      # sub              subtraction
      #                  left          leftside
      #                  right         rightside

      # if               if thing
      #                  statement     the statement
      #                  block         the contained block
      #                  else          None or another block with the else part

      # true             (statement)

      # false            (statement)

      # greaterEqual     (statement)
      #                  left          leftside
      #                  right         rightside

      # TODO< smallerEqual, Equal, Unequal, Smaller, Greater >

      # break            break expression

      # postinc          (statement)
      #                  statement

      # preinc           (statement)
      #                  statement

      # postdec          (statement)
      #                  statement

      # preinc           (statement)
      #                  statement

      # return           (statement)
      #                  expression       is the expression that have to be avaluated, can also be not set (None)
      #                  expressionSet    was the Expression set (True or False)

      # newConstArray    creates a new constant unchangable array
      #                  name             is the name of the array
      #                  info             Typeinformation, is a 'Datatype' Object

      # newVar2          allocates space for a new (scoped) variable
      #                  name             is the Variablename
      #                  info             Typeinformation, is a 'Datatype' Object
      
      # constantFloat    is a contant float
      #                  value            is the floatingpoint value

      """
      self.Root = [
         {"type":"newVar", "name":"Counter", "dataType":0,"bits":32},
         {"type":"assigment2", "left":{"type":"variable", "name":"Counter"}, "right":{"type":"number", "value":20}},
         {"type":"newVar", "name":"Xn", "dataType":0, "bits":32},
         {"type":"assigment2", "left":{"type":"variable", "name":"Xn"}, "right":{"type":"number", "value":5}},
         {"type":"newVar", "name":"Number", "dataType":0, "bits":32},
         {"type":"assigment2", "left":{"type":"variable", "name":"Number"}, "right":{"type":"number", "value":500}},

         {"type":"while", "statement":{"type":"number", "value":1}, "body":[
            {"type":"minusAssignment", "left":{"type":"variable", "name":"Counter"}, "right":{"type":"number", "value":1}},
            {"type":"assigment2", "left":{"type":"variable", "name":"Xn"}, "right":{
               "type":"div", "left":{"type":"add", "left":{"type":"variable", "name":"Xn"}, "right":{"type":"div", "left":{"type":"variable", "name":"Number"}, "right":{"type":"variable", "name":"Xn"}}}, "right":{"type":"number", "value":2}
            }}
         ]}
      ]"""

      # algorithm for calculating of the sqrt

      # (examples/calc my sqrt)

      Type1 = Datatype(Datatype.EnumBasetype.UNSIGNED)
      Type1.Bits = 32

      Type2 = Datatype(Datatype.EnumBasetype.UNSIGNED)
      Type2.Bits = 32

      Type3 = Datatype(Datatype.EnumBasetype.UNSIGNED)
      Type3.Bits = 32

      self.Root = [
         {"type":"newVar2", "name":"Input", "info":Type1},
         {"type":"assigment2", "left":{"type":"variable", "name":"Input"}, "right":{"type":"number", "value":29}},
         {"type":"newVar2", "name":"Counter", "info":Type2},
         {"type":"assigment2", "left":{"type":"variable", "name":"Counter"}, "right":{"type":"number", "value":0}},
         {"type":"newVar2", "name":"Old", "info":Type3},
         {"type":"assigment2", "left":{"type":"variable", "name":"Old"}, "right":{"type":"number", "value":0}},
         
         {"type":"while", "statement":{"type":"true"}, "body":[
            {"type":"assigment2", "left":{"type":"variable", "name":"Old"}, "right":{
               "type":"add", "left":{"type":"variable", "name":"Old"}, "right":{
                  "type":"add", "left":{"type":"mul", "left":{"type":"number", "value":2}, "right":{"type":"variable", "name":"Counter"}}, "right":{"type":"number", "value":1}
               }
            }},

            {
               "type":"if",
               "statement":{"type":"greaterEqual", "left":{"type":"variable", "name":"Old"}, "right":{"type":"variable", "name":"Input"}},
               "block":[
                  {"type":"break"}
               ]
            },

            {
               "type":"postinc",
               "statement":{"type":"variable", "name":"Counter"}
            }
         ]}
      ]

      # cordic algorithm

      """
      const fixed6p12 ATanTable[1] = [0.7853981633974483 , 0.4636476090008061,
                                0.24497866312686414, 0.12435499454676144,
                                0.06241880999595735, 0.031239833430268277,
                                0.015623728620476831];
      """

      """
      Type1 = Datatype(Datatype.EnumBasetype.FIXEDPOINT) # fixedpoint Datatype
      Type1.PrePointBits = 6
      Type1.PostPointBits = 12
      Type1.IsArray = True
      Type1.IsConst = True
      Type1.ArrayValues = [0.7853981633974483 , 0.4636476090008061, 0.24497866312686414, 0.12435499454676144, 0.06241880999595735, 0.031239833430268277, 0.015623728620476831]

      Type2 = Datatype(Datatype.EnumBasetype.FIXEDPOINT) # fixedpoint Datatype
      Type2.PrePointBits = 6
      Type2.PostPointBits = 12

      Type3 = Datatype(Datatype.EnumBasetype.FIXEDPOINT) # fixedpoint Datatype
      Type3.PrePointBits = 6
      Type3.PostPointBits = 12

      Type4 = Datatype(Datatype.EnumBasetype.FIXEDPOINT) # fixedpoint Datatype
      Type4.PrePointBits = 6
      Type4.PostPointBits = 12

      self.Root = [
         {"type":"newConstArray", "name":"ATanTable", "info":Type1},
         {"type":"newVar2", "name":"X", "info":Type2},
         {"type":"assigment2", "left":{"type":"variable", "name":"X"}, "right":{"type":"constantFloat", "value":4.0}},
         {"type":"newVar2", "name":"Y", "info":Type3},
         {"type":"assigment2", "left":{"type":"variable", "name":"Y"}, "right":{"type":"constantFloat", "value":1.0}},
         
         {"type":"newVar2", "name":"Phi", "info":Type4},
         {"type":"assigment2", "left":{"type":"variable", "name":"Phi"}, "right":{"type":"constantFloat", "value":0.907571}}
         
         
      ]
      """

      self.ImmediateCodeObj = ImmediateCode()

   def doIt(self):
      ReturnedTuple = self.transformObjectsIntoCode(self.Root, 0, 0, [])

      if ReturnedTuple[0]:
         print("Compilation successfull")
      else:
         print("Compilation Error")
         print(ReturnedTuple[1])

      print("\n\n")

      print(self.ImmediateCodeObj.debugImmediateCode(self.ImmediateCodeObj.ImmCodeData))

      OptimizerObj = Optimizer()
      OptimizerObj.ImmediateInstructions = self.ImmediateCodeObj.ImmCodeData
      OptimizerObj.Variables = self.ImmediateCodeObj.Variables

      OptimizerObj.doOptimization()

      print("\n\n")

      print(self.ImmediateCodeObj.debugImmediateCode(OptimizerObj.ImmediateInstructions))

   # "IntoVariable"    is the Id of the variable the result must be written into

   # returns (Success State, Error Message)
   def evaluateStatement(self, Statement, IntoVariable, IntoDatatype, VariableStack):
      print(Statement["type"])

      if   Statement["type"] == "variable":
         # lookup the variable name
         (Found, VariableId, VariableDatatype) = self.lookupVariable(VariableStack, Statement["name"])

         if not Found:
            return (False, "Variable " + Statement["name"] + " was not declared!")

         # check if the types and bits are equal
         TypeCheckResult = VariableDatatype.compareType(IntoType)

         if TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTBITS:
            return (False, "Variable " + Statement["name"] + " don't have matching number of bits!")
         elif TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTTYPE:
            return (False, "Variable " + Statement["name"] + " is of wrong type!")
         elif TypeCheckResult == Datatype.EnumTypeResult.EQUAL:
            # all right
            pass
         else:
            return (False, "Internal Error #42")

         self.ImmediateCodeObj.writeMov(IntoVariable, VariableId)

         return (True, 0)

      elif Statement["type"] == "number":
         self.ImmediateCodeObj.writeConstAssigment(IntoVariable, Statement["value"])
         
         return (True, 0)

      elif (Statement["type"] == "div") or (Statement["type"] == "add") or (Statement["type"] == "mul") or (Statement["type"] == "div"):
         VarLeft = None
         VarRight = None

         # do a simple optimization
         # if it is a variable, we don't need to create a Temporary Variable, evaluate it and move it into it
         if Statement["left"]["type"] == "variable":
            (Found, VarLeft, VarLeftDatatype) = self.lookupVariable(VariableStack, Statement["left"]["name"])

            if not Found:
               return (False, "Variable " + Statement["name"] + " was not declared!")

         else:
            VarLeft = self.ImmediateCodeObj.allocateVariable(IntoDatatype)
            VarLeftDatatype = IntoDatatype

            (CalleeSuccess, CalleeErrorMessage) = self.evaluateStatement(Statement["left"], VarLeft, VarLeftDatatype, VariableStack)
            if not CalleeSuccess:
               return (False, CalleeErrorMessage)

         # the same for the right side
         if Statement["right"]["type"] == "variable":
            (Found, VarRight, VarRightDatatype) = self.lookupVariable(VariableStack, Statement["right"]["name"])

            if not Found:
               return (False, "Variable " + Statement["name"] + " was not declared!")

         else:
            VarRight = self.ImmediateCodeObj.allocateVariable(IntoDatatype)
            VarRightDatatype = IntoDatatype

            (CalleeSuccess, CalleeErrorMessage) = self.evaluateStatement(Statement["right"], VarRight, VarRightDatatype, VariableStack)
            if not CalleeSuccess:
               return (False, CalleeErrorMessage)

         # check if the types are equal
         TypeCheckResult = VarLeftDatatype.compareType(VarRightDatatype)

         if   TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTBITS:
            return (False, "Left and right variables don't have matching number of bits!")
         elif TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTTYPE:
            return (False, "Left an right variables are of different type!")
         elif TypeCheckResult == Datatype.EnumTypeResult.EQUAL:
            # all right
            pass
         else:
            return (False, "Internal Error #42")


         if Statement["type"] == "add":
            self.ImmediateCodeObj.writeAdd(VarLeft, VarRight, IntoVariable)
         elif Statement["type"] == "sub":
            self.ImmediateCodeObj.writeSub(VarLeft, VarRight, IntoVariable)
         elif Statement["type"] == "mul":
            self.ImmediateCodeObj.writeMul(VarLeft, VarRight, IntoVariable)
         elif Statement["type"] == "div":
            self.ImmediateCodeObj.writeDiv(VarLeft, VarRight, IntoVariable)

         return (True, 0)

      else:
         # TODO

         # return an error
         print("Eval error")
         return (False,0)
         

   # ScopeType is the Type of the Scope
   # 0 : inside "main"
   # 1 : inside a "while"

   # ReturnLabelId is the Id of the Label a return/break instruction would jump to

   # VariableStack  is a stack with lists of the scoped variables
   #                each Element in the List is a dict with
   #                "name"   the name of the variable
   #                "id"     the id of the Variable
   #                "info"   typeinfo as a 'Datatype' object
   def transformObjectsIntoCode(self, Objects, ScopeType, ReturnLabelId, VariableStack):
      VariableStack.append([])

      for Object in Objects:
         print(Object["type"])

         if Object["type"] == "newVar2":
            # check if the variable was allready declared inside this scope
            for Variable in VariableStack[-1]:
               if Variable["name"] == Object["name"]:
                  return (False, "Variable '{0}' was allready defined in this scope!".format(Object["name"]))

            VariableId = self.ImmediateCodeObj.allocateVariable(Object["info"])

            # store the variable in the variable stack
            NewVar = {}
            NewVar["name"] = Object["name"]
            NewVar["id"]   = VariableId
            NewVar["info"] = Object["info"]

            VariableStack[-1].append(NewVar)

         elif Object["type"] == "assigment":
            # Emit an error

            return (False, "Internal Error #2 (Outdated)")
         
         elif Object["type"] == "assigment2":
            # check if on the left is a Variable, if not, emit an error
            # TODO< here is the right place for a struct lookup for for example a C-expression like "blub.a = ..." or "ax->ab = ..." >

            if Object["left"]["type"] != "variable":
               # emit an error
               return (False, "Internal Error #1 (TODO)")

            # do the variable lookup
            (VariableFound, LeftVariableId, LeftVariableInfo) = self.lookupVariable(VariableStack, Object["left"]["name"])

            if not VariableFound:
               # emit syntax error
               return (False, "Variable " + Object["left"]["name"] + " was not declared!")

            # evaluate the right statement
            (CalleeSuccess, CalleeMessage) = self.evaluateStatement(Object["right"], LeftVariableId, LeftVariableInfo, VariableStack)

            # check for errors of the function call
            if not CalleeSuccess:
               # TODO< return better error description >
               return (False, CalleeMessage)

         elif Object["type"] == "minusAssignment":
            # check if on the left is a Variable, if not, emit an error
            # TODO< here is the right place for a struct lookup for for example a C-expression like "blub.a = ..." or "ax->ab = ..." >

            if Object["left"]["type"] != "variable":
               # emit an error
               return (False, "Internal Error #1 (TODO)")

            (VariableFound, LeftVariableId, LeftVariableInfo) = self.lookupVariable(VariableStack, Object["left"]["name"])

            if not VariableFound:
               # emit syntax error
               return (False, "Variable " + Object["left"]["name"] + " was not declared!")

            # create a new temporary variable
            TempVar = self.ImmediateCodeObj.allocateVariable(LeftVariableInfo)

            (CalleeSuccess, CalleeMessage) = self.evaluateStatement(Object["right"], TempVar, LeftVariableInfo, VariableStack)

            # check for errors
            if not CalleeSuccess:
               # TODO< return better error description >
               return (False, CalleeMessage)

            self.ImmediateCodeObj.writeSub(LeftVariableId, TempVar, LeftVariableId)

         elif Object["type"] == "while":
            
            LabelIdStart = self.ImmediateCodeObj.getNewLableIdentifier()
            LabelIdEnd   = self.ImmediateCodeObj.getNewLableIdentifier()
   
            self.ImmediateCodeObj.writeLable(LabelIdStart)

            
            # TODO< emit code for evaluation of the statement >

            (CalleeSuccess, CalleeMessage) = self.transformObjectsIntoCode(Object["body"], 1, LabelIdEnd, VariableStack)
            
            if not CalleeSuccess:
               return (False, CalleeMessage)

            self.ImmediateCodeObj.writeGoto(LabelIdStart)

            self.ImmediateCodeObj.writeLable(LabelIdEnd)
         elif Object["type"] == "if":

            if Object["statement"]["type"] == "greaterEqual":
               if (Object["statement"]["left"]["type"] != "variable") and (Object["statement"]["right"]["type"] != "variable"):
                  return (False, "TODO 'if' #2")

               VariableNameLeft  = Object["statement"]["left"]["name"]
               VariableNameRight = Object["statement"]["right"]["name"]

               (VariableFound, VariableIdLeft, VarLeftDatatype) = self.lookupVariable(VariableStack, VariableNameLeft)

               if not VariableFound:
                  return (False, "Variable " + VariableNameLeft + " was not declared!")

               (VariableFound, VariableIdRight, VarRightDatatype) = self.lookupVariable(VariableStack, VariableNameRight)

               if not VariableFound:
                  return (False, "Variable " + VariableNameRight + " was not declared!")

               # check if the types do match
               TypeCheckResult = VarLeftDatatype.compareType(VarRightDatatype)

               if   TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTBITS:
                  return (False, "Left and right variables don't have matching number of bits!")
               elif TypeCheckResult == Datatype.EnumTypeResult.DIFFERENTTYPE:
                  return (False, "Left an right variables are of different type!")
               elif TypeCheckResult == Datatype.EnumTypeResult.EQUAL:
                  # all right
                  pass
               else:
                  return (False, "Internal Error #42")


               # write Immediate code
               LabelIdTrue  = self.ImmediateCodeObj.getNewLableIdentifier()
               LabelIdIfEnd = self.ImmediateCodeObj.getNewLableIdentifier()

               self.ImmediateCodeObj.writeIf(VariableIdLeft, VariableIdRight, 0, LabelIdTrue, LabelIdIfEnd)
               self.ImmediateCodeObj.writeLable(LabelIdTrue)

               # TODO< add and remove new level of variable stack ! >

               (CalleeSuccess, CalleeMessage) = self.transformObjectsIntoCode(Object["block"], ScopeType, ReturnLabelId, VariableStack)

               if not CalleeSuccess:
                  return (False, CalleeMessage)

               self.ImmediateCodeObj.writeLable(LabelIdIfEnd)

            else:
               # TODO
               return (False, "TODO 'if' #1")

         elif Object["type"] == "break":
            if (ScopeType != 1) and (ScopeType != 2) : # if we are not in in a while or for
               return (False, "Using of break outside of an loop!")

            self.ImmediateCodeObj.writeGoto(ReturnLabelId)

         elif Object["type"] == "return":
            # TODO< check for beeing in a function >
            # TODO< check for needed return argument! >

            self.ImmediateCodeObj.writeGoto(ReturnLabelId)

         elif Object["type"] == "postinc":
            if Object["statement"]["type"] != "variable":
               return (False, "postinc TODO")

            (VariableFound, VariableId, VariableDatatype) = self.lookupVariable(VariableStack, Object["statement"]["name"])

            if not VariableFound:
               return (False, "Variable " + Object["statement"]["name"] + " was not declared!")

            self.ImmediateCodeObj.writeInc(VariableId, VariableId)

         elif Object["type"] == "preinc":
            return (False, "TODO #A")

         elif Object["type"] == "postdec":
            return (False, "TODO #B")

         elif Object["type"] == "predec":
            return (False, "TODO #C")

         else:
            # internal error

            return (False, "Internal Error!")

      VariableStack.pop()

      return (True, None)

   # this does the variable lookup
   def lookupVariable(self, VariableStack, VariableName):
      ActualStackIndex = len(VariableStack)-1
      Found = False
      VariableId = None
      VariableInfo = None

      while True:
         for Variable in VariableStack[ActualStackIndex]:
            if Variable["name"] == VariableName:
               Found = True
               VariableId = Variable["id"]
               VariableInfo = Variable["info"]

               break

         if Found:
            break

         if ActualStackIndex == 0:
            break

         ActualStackIndex -= 1

      return (Found, VariableId, VariableInfo)

Gen = Generator()
Gen.doIt()
