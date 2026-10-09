fb = lambda a: a + 100 if a > 100 and a < 200 else a + 200 if a > 500 and a < 600 else a
print(fb(150))
print(fb(550))
print(fb(50))
