def x_of_i(a, i, delta_x):
    return a + (i * delta_x)
def particular_function(x):
    return x**3
def trap_int(a, b, f_of_x, n, cn):
    #get delta ΔX
    delta_x = (b-a)/n
    sum = (0+0j)
    for i in range(n+1):
        x_i = x_of_i(a, i, delta_x)
        f_x_i = f_of_x(x_i, cn)
        if i == 0 or i == n:
            sum +=  f_x_i
        else:
            sum += 2 * f_x_i
    definite_integral = (delta_x/2)*(sum)
    return definite_integral

