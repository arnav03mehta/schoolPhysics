import math

# some global functions ---------------- --------------- ------------ #

def posi(num) :
    if num < 0 :
        return -1*num
    else :
        return num
# ------------- ------------- --------------- ------------ ---------- #

class pointCharge :

    k = 9*(10**9)
    e_o = 1/(4*math.pi*k)

    def __init__(self,charge) :
        self.charge = charge


    def field(self,distance) :
        charge = self.charge
        k = self.k
        return k*(charge/(distance**2))

    def force(self,point2,distance) :
        iField = self.field(distance)
        return iField*point2.charge

# ------------- ---------------- --------------- ------------ #

class twoChargeSystem :

    def __init__(self,charge1,charge2,distance=0) :
        k = 9*(10**9)
        e_o = 1/(4*math.pi*k)
        self.charge1 = charge1
        self.charge2 = charge2
        self.k = k
        self.e_o = e_o
        self.distance = distance

    def field(self,type_,dist_from_c1=0,dist_from_c2=0,dist_from_center=0) :
        charge1 = self.charge1
        charge2 = self.charge2
        half_dist = self.distance/2
    
        if type_ == "eq" :
            if dist_from_c1 > 0 :
                dist_from_center = ((half_dist**2)-(dist_from_c1**2))**(1/2)
                dist_from_c2 = dist_from_c1
            elif dist_from_center > 0 :
                dist_from_c1 = ((half_dist**2)+(dist_from_center**2))**(1/2)
                dist_from_c2 = dist_from_c1
        cos = half_dist/dist_from_c1
        net_field = ( posi(charge1.field(dist_from_c1)) * cos )+( posi(charge2.field(dist_from_c2)) * cos )
        return net_field

    def force(self,other_charge,type_f,dist_from_c1=0,dist_from_c2=0,dist_from_center=0) :
        
        E = self.field(type_f,dist_from_c1,dist_from_c2,dist_from_center)
        return other_charge*E

    def potentialEnergy(self) :
        charge1 = self.charge1
        charge2 = self.charge2
        k = self.k
        distance = self.distance
        return k*(charge1.charge*charge2.charge)/distance

class dipole :
    def __init__(self,charge,distance) :
        moment = charge*distance
        k = 9*(10**9)
        self.charge = charge
        self.distance = distance
        self.moment = moment
        self.k = k
        
    def potential(self,dist_from_center,rad_from_center=0,deg_from_center=0) :
        k = self.k
        p = self.moment
        if rad_from_center == 0 and deg_from_center != 0 :
            angle = math.radians(deg_from_center)
        else :
            angle = rad_from_center

        return k*p*math.cos(angle) / (dist_from_center**2)

# ------------- ---------------- --------------- ------------ #

class ringCharge :

    def __init__(self,charge,radius) :
        k = 9*(10**9)
        e_o = 1/(4*math.pi*k)
        self.k = k
        self.charge = charge
        self.radius = radius
    
    def field(self,dist_from_center) :
        charge = self.charge
        radius = self.radius
        k = self.k
        r = (radius**2) + (dist_from_center**2)
        E = (k*dist_from_center*charge)/(r**(3/2))
        return E
        
    def force(self,pt_charge,dist_from_center) :
        E = self.field(dist_from_center)
        return E*pt_charge

# ------------- ---------------- --------------- ------------ #


if __name__ == "__main__":

    c = pointCharge(10)
    c2 = pointCharge(-10)
    syst = twoChargeSystem(c,c2,0.1)

    print(syst.field("eq",dist_from_center=0.12))

    print(len(str(int(syst.field("eq",dist_from_center=0.12)))))
    
    print(dipole(10,0.1).potential(0.5,deg_from_center=45))
