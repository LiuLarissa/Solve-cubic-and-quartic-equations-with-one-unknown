import math
import cmath

#一元四次方程
def Quartic(args):
    a,b,c,d,e = args
    P = (c**2+12*a*e-3*b*d)/9
    Q = (27*a*d**2+2*c**3+27*b**2*e-72*a*c*e-9*b*c*d)/54
    D = cmath.sqrt(Q**2-P**3)
    u = ThreeSquare(Q+D) if abs(Q+D)>=abs(Q-D) else ThreeSquare(Q-D)
    v = 0 if u==0 else P/u
    w = complex(-0.5,3**0.5/2)
    m = []
    M = []
    flag = 0
    roots = []
    for i in range(3):
        x = cmath.sqrt(b**2-8*a*c/3+4*a*(w**i*u+w**(3-i)*v))
        m.append(x)
        M.append(abs(x))
        if m == 0:
            flag=flag+1
    if flag == 3:
        mm = 0
        S = b**2-8*a*c/3
        T = 0
    else:
        t = M.index(max(M))
        mm = m[t]
        S = 2*b**2-16*a*c/3-4*a*(w**t*u+w**(3-t)*v)
        T = (8*a*b*c-16*a**2*d-2*b**3)/mm

    '''for i in range(4):
        n = i+1
        k = math.ceil(n/2)
        x = (-b+(-1)**k*mm+(-1)**(n+1)*cmath.sqrt(S+(-1)**k*T))/(4*a)
        roots.append(x)'''
    x1=(-b-mm+cmath.sqrt(S-T))/(4*a)
    x2=(-b-mm-cmath.sqrt(S-T))/(4*a)
    x3=(-b+mm+cmath.sqrt(S+T))/(4*a)
    x4=(-b+mm-cmath.sqrt(S+T))/(4*a)
    roots.append(x1)
    roots.append(x2)
    roots.append(x3)
    roots.append(x4)
        
    return roots
       
#一元三次方程
def Cubic(args):
    a,b,c,d = args
    p = c/a-b**2/(3*a**2)
    q = d/a+2*b**3/(27*a**3)-b*c/(3*a**2)
    w = complex(-0.5,(3**0.5)/2)
    ww = complex(-0.5,-(3**0.5)/2)
    A = cmath.sqrt((q/2)**2+(p/3)**3)
    B = ThreeSquare(-q/2+A)
    C = ThreeSquare(-q/2-A)
    y1 = B+C
    y2 = w*B+ww*C
    y3 = ww*B+w*C
    D = b/(3*a)
    roots=[RoundAns(y1-D,6),RoundAns(y2-D,6),RoundAns(y3-D,6)]
    return roots

#一元二次方程
def Quadratic(args):
    a,b,c=args
    D = cmath.sqrt(b**2-4*a*c)
    x1 = (-b+D)/(2*a)
    x2 = (-b-D)/(2*a)
    roots = [x1,x2]
    return roots


#计算立方根，包括实数和复数
def ThreeSquare(x):
    if x.imag == 0:
        #实数
        m = x.real
        ans = -math.pow(-m,1/3) if m<0 else math.pow(m,1/3)
    else:
        #复数
        ans = x**(1/3)
    return ans

#将根round到num位
def RoundAns(x,num):
    if x.imag == 0:
        m = x.real
        ans = round(m,num)
    else:
        m = round(x.real,num)
        n = round(x.imag,num)
        ans = complex(m,n)
    return ans

args=(3,-1,3,1,-5)
#args=(1,-4,6,-4,1)
res = Quartic(args)
#args1 =(2,1,4,5)
#res = Cubic(args1)
#args=(5,1,1)
#res= Quadratic(args)
print(res)
