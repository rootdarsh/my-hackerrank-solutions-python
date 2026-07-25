import cmath
z = complex(input())
re = z.real
im = z.imag
r = abs(complex(re,im))
phase = cmath.phase(complex(re,im))
print(r)
print(phase)
