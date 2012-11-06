class Datatype(object):
   # enum for the BaseType
   class EnumBasetype(object):
      UNSIGNED   = 0
      SIGNED     = 1
      FIXEDPOINT = 2

   class EnumTypeResult(object):
      EQUAL = 0
      DIFFERENTBITS = 1
      DIFFERENTTYPE = 2

   def __init__(self, BaseType):
      self.BaseType        = BaseType
      self.PrePointBits    = 0
      self.PostPointBits   = 0
      self.IsArray         = False
      self.IsConst         = False
      self.ArrayValues     = []
      self.Bits            = 0

   # return some value from EnumTypeResult

   def compareType(self, Other):
      if self.BaseType != Other.BaseType:
         return Datatype.EnumTypeResult.DIFFERENTTYPE

      if (self.BaseType == Datatype.EnumBasetype.UNSIGNED) or (self.BaseType == Datatype.EnumBasetype.SIGNED):
         if self.Bits != Other.Bits:
            return Datatype.EnumTypeResult.DIFFERENTBITS
         
      elif (self.BaseType == Datatype.EnumBasetype.FIXEDPOINT):
         if (self.PrePointBits != Other.PrePointBits) or (self.PostPointBits != Other.PostPointBits):
            return Datatype.EnumTypeResult.DIFFERENTBITS

      return Datatype.EnumTypeResult.EQUAL