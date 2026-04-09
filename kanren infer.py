from kanren import run, var, Relation, facts

parent = Relation()
facts(parent, ("john","mary"), ("mary","susan"), ("john","mike"))

x = var()
print(run(3, x, parent("john", x)))