# large = 2.**2048
# for i in range(9):
#    large *= 2
#    print(i, large)
small = 1/2**50
for i in range(30):
    small /= 2
    print(i, 1+small, small)
