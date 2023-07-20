import math
import matplotlib.pyplot as plt
from matplotlib import animation

#Setting initial conditions
distance = 1.5e11
G = 6.67e-11
m1 = 5.972e24
m2 = 2.0e30
M = m1+m2

x1 = (-m2/M)*distance
y1 = 0
z1 = 0
p1 = math.sqrt(x1**2+y1**2+z1**2)

x2 = (m1/M)*distance
y2 = 0
z2 = 0

#Calculating relative vector
rx = x2-x1
ry = y2-y1
rz = z2-z1
r = math.sqrt(rx**2+ry**2+rz**2)

v1x = 0
v1y = 0.7*math.sqrt(G*m2*p1/r**2)
v1z = 0

#Setting two body problem
p1x = m1*v1x
p1y = m1*v1y
p1z = m1*v1z

#Set as negative to ensure linear momentum preservation
p2x = -p1x
p2y = -p1y
p2z = -p1z


t = 0.0
dt = 24*60*60

xelist,yelist,zelist = [],[],[]
xslist,yslist,zslist = [],[],[]

while t < 365*dt:
    rx = x2-x1
    ry = y2-y1
    rz = z2-z1
    r = math.sqrt(rx**2+ry**2+rz**2)


    #Computing gravity force
    fx = -(G*m1*m2)*(rx/(r)**3)
    fy = -(G*m1*m2)*(ry/(r)**3)
    fz = -(G*m1*m2)*(rz/(r)**3)

    #Computing new momentum
    p2x += fx*dt
    p2y += fy*dt
    p2z += fz*dt

    #Computing new position
    x2 += (p2x*dt)/m2
    y2 += (p2y*dt)/m2
    z2 += (p2z*dt)/m2

    #Save de position to plot the track
    xslist.append(x2)
    yslist.append(y2)
    zslist.append(z2)

    p1x += -fx*dt
    p1y += -fy*dt
    p1z += -fz*dt

    x1 += (p1x*dt)/m1
    y1 += (p1y*dt)/m1
    z1 += (p1z*dt)/m1

    xelist.append(x1)
    yelist.append(y1)
    zelist.append(z1)

    if x2 - x1 == 0:
        break

    t += dt

#Creating the plot
fig, ax = plt.subplots(figsize=(6,6))
ax.set_aspect('equal')
ax.grid()

#Setting m1 colors
line_e, = ax.plot([(-m2/M)*distance],[0],'-',lw=1,c='blue')
point_e, = ax.plot([], [], marker="o", markersize=4, markeredgecolor="blue", markerfacecolor="blue")
text_e = ax.text((-m2/M)*distance,0,'m1')

#Setting M2 colors
line_s, = ax.plot([(m1/M)*distance],[0],'-',lw=1,c='green')
point_s, = ax.plot([(m1/M)*distance], [0], marker="o", markersize=7, markeredgecolor="green", markerfacecolor="green")
text_s = ax.text((m1/M)*distance,0,'m2')

exdata,eydata = [],[] #m1 track
sxdata,sydata = [],[] #m2 track

def update(i):

    exdata.append(xelist[i])
    eydata.append(yelist[i])

    line_e.set_data(exdata,eydata)
    point_e.set_data(xelist[i],yelist[i])
    text_e.set_position((xelist[i],yelist[i]))

    sxdata.append(xslist[i])
    sydata.append(yslist[i])

    line_s.set_data(sxdata,sydata)
    point_s.set_data(xslist[i],yslist[i])
    text_s.set_position((xslist[i],yslist[i]))

    ax.axis('equal')
    ax.set_xlim(-2*1.5e11,2*1.5e11)
    ax.set_ylim(-2*1.5e11,2*1.5e11)
    #print(i)
    return line_e,point_e,text_e,line_s,point_s,text_s

anim = animation.FuncAnimation(fig,func=update,frames=len(xelist),interval=1,blit=True , repeat = False)
#anim.save('two_body_earth_sun.gif')
plt.show()



'''plt.plot(xelist,yelist,'-g',lw=2)
plt.plot(xslist,yslist,'-b',lw=2)
plt.axis('equal')
plt.show()'''

    

