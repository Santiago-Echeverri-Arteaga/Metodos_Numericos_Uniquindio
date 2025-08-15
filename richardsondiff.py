from finitediff import f, fprime, calcfd, calccd

x = 0.5
an = fprime(x)

hs = [10**(-i) for i in range(1, 7)]

rowf = "{0:1.0e} {1:20.16f} {2:20.16f}"
print("{0:10} {1:17} {2:20}".format(
    'h abs.', 'error rich fd', 'abs. error rich cd'))

for h in hs:
    fdrich = 2*calcfd(f, x, h/2) - calcfd(f, x, h)
    fd = abs(fdrich-an)
    cdrich = (4*calccd(f, x, h/2) - calccd(f, x, h))/3
    cd = abs(cdrich-an)
    print(rowf.format(h, fd, cd))
