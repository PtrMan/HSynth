class Datatype(object):
   # BaseType can be
   # 0 : unsigned
   # 1 : signed
   # 2 : (signed) fixed point
   def __init__(self, BaseType):
      self.BaseType = BaseType
      self.PrePointDigits = 0
      self.PostPointDigits = 0
      self.IsArray = False
      self.IsConst = False
      self.ArrayValues = []
