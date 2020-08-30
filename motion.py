import math
import matplotlib.pyplot as plt
import numpy as np

# some global functions ---------------- --------------- ------------ #

def posi(num) :
    if num < 0 :
        return -1*num
    else :
        return num
# ------------- ------------- --------------- ------------ ---------- #

class thing :

    def __init__(self,mass=0.001) :
        self.mass = mass 
        self.weight = mass*9.8

    def throw_from_ground(self,velocity,angle_in_deg=0,angle_in_rad=0) :
        if angle_in_rad == 0 and angle_in_deg != 0 :
            angle = math.radians(angle_in_deg)
        else :
            angle = angle_in_rad
        x_pos = lambda t : velocity*math.cos(angle) * t
        y_pos = lambda t : (velocity*math.sin(angle)*t)-((9.8*(t**2))/2)
        T = 2*velocity*math.sin(angle) / 9.8
        xList = [ x_pos(i) for i in np.arange(0,T,0.01) ]
        yList = [ y_pos(i) for i in np.arange(0,T,0.01) ]
        max_height = (velocity**2)*math.sin(2*angle)/9.8
        max_dist = (velocity**2)*(math.sin(angle)**2)/(2*9.8)
        plt.plot(xList,yList)
        
        print(f"Total time in air : {T}")
        print(f"Max horizontal distance : { max_height }")
        print(f"Max height reached : { max_dist }")
        
        if max_height > max_dist :
            plt.ylim([0,max_height])
        else :
            plt.xlim([0,max_dist])

        plt.show()

    def throw_horizontally(self,velocity,height) :
        
        x_pos = lambda t : velocity * t
        y_pos = lambda t : height - ((9.8*(t**2))/(2*(velocity**2))) 
        T = (2*height/9.8)**(1/2)

        xList = [ x_pos(i) for i in np.arange(0,T,0.0001) ]
        yList = [ y_pos(i) for i in np.arange(0,T,0.0001) ]
        max_dist = velocity*T
        print(f"Total time in air : {T}")
        print(f"Max horizontal distance : { max_dist }")
        print(yList)
        
        plt.plot(xList,yList)
        if height > max_dist :
            plt.ylim([0,height])
        else :
            plt.xlim([0,max_dist])
        plt.show()
        






if __name__ == "__main__" :

    thing(6).throw_from_ground(50,angle_in_deg=87)