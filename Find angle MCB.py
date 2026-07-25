# the output expected in this challenge is the measure of angle MCB (NOT angle MBC - as mentioned on the hackerrank challenge page)
import math
AB = int(input())
BC = int(input())
AC = math.sqrt((AB*AB) + (BC*BC))
MC = AC/2
ang_MCB = math.atan(AB/BC)
print(f"{round(math.degrees(ang_MCB))}\u00b0")
