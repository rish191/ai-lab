from sympy import symbols
from sympy.logic.boolalg import And, Or, Not, Implies

p, q = symbols('p q')

expr1 = And(p, q)
expr2 = Or(p, q)
expr3 = Not(p)
expr4 = Implies(p, q)

print(expr1)
print(expr2)
print(expr3)
print(expr4)

print(expr4.subs({p: True, q: False}))