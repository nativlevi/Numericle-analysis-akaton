import math

def eq1(L):
    return 4.86 + 0.018 * L

def eq2(L):

    return L / 3000.0

def eq3(L, A0=0.0047, A1=0.0023, A2=0.000043):
    if L <= 0:
        return 0
    return L * (A0 + A1 * math.log(L) + A2 * (math.log(L)**2))

def eq4(L):
    return 4.2 + 0.0015 * (L ** (4.0/3.0))

def eq5(L):
    return 0.069 + 0.00156 * L + 0.00000047 * (L**2)

if __name__ == '__main__':
    L_values = [1297, 1500, 2928]

    for L in L_values:
        print(f"\n=== Results for L = {L} ===")
        print(f"eq1:            {eq1(L):.4f}")
        print(f"eq2:      {eq2(L):.4f}")
        print(f"eq3:              {eq3(L):.4f}")
        print(f"eq4:            {eq4(L):.4f}")
        print(f"eq5:  {eq5(L):.4f}")
