from sympy import symbols
from sympy.logic.boolalg import Implies

p, q = symbols('p q')

expr = Implies(p, q)
print(expr)

print(expr.subs({p: True, q: True}))
print(expr.subs({p: True, q: False}))