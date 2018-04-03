def general_poly(L):
    """ this function works in values outside of it like:general_poly([1,3,4,5])(10)
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def inner(x):
        sumlist=[]
        for i in range(len(L)):
            sumlist.append((L[i])*(x**(len(L)-1-i)))
        return sum(sumlist)
    return inner