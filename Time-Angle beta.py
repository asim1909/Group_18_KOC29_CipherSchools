#Time-Angle beta
def calcAngle(h,m):
    if (h < 0 or m < 0 or h > 23 or m > 60):         # validating the input

        print('Wrong input')
    if (h == 24):
        h = 0
    if (m == 60):
        m = 0
        h += 1;
    if(h>12):
        h = h-12;
   
    hour_angle = 0.5 * (h * 60 + m)  # Calculating the angles moved by hour and minute hands with reference to 12:00
    minute_angle = 6 * m
    angle =(hour_angle - minute_angle)     # Find the difference between two angles
    c=abs(360-abs(angle))
    angle = min(c, abs(angle))       # Return the smaller angle of two possible angles
    return angle
h,m=map(int, input("Please enter the time ").split())
print('Angle ', calcAngle(h,m),"°")
