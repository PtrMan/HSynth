# 0.75

def convertNumberToFixedpoint(Number):
   Index = -1
   
   Bits = []
   
   while True:
      print(Number)
      
      if Index == -13:
         break
         
      if Number >= 2**Index:
         Bits.append(True)
         Number -= 2**Index
      else:
         Bits.append(False)
         
      Index -= 1
   
   print(Bits)
