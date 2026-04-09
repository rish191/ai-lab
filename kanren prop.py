from kanren import run, var, eq, conde

p, q = var(), var()

result = run(0, (p, q),
             conde(
                 [eq(p, True), eq(q, True)],
                 [eq(p, True), eq(q, False)]
             ))

print(result)