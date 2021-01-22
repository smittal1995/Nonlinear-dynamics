import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#~ fig, ax = plt.subplots()
fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-.07, .07))

filename = '{}{}'.format("file_0.550_u_0.00_q_0.87_T_9.10_Stag-Hunt-T1_0",".txt")
data1=np.loadtxt(filename)
#~ s1=data1[:,0]
#~ t1=data1[:,1]

filename = '{}{}'.format("file_0.750_u_0.00_q_0.87_T_9.10_Stag-Hunt-T1_0",".txt")
data2=np.loadtxt(filename)
#~ s1=data1[:,0]
#~ t1=data1[:,1]
filename = '{}{}'.format("file_0.250_u_0.00_q_0.87_T_9.10_Stag-Hunt-t1_0",".txt")
data3=np.loadtxt(filename)

filename = '{}{}'.format("file_0.350_u_0.00_q_0.87_T_9.10_Stag-Hunt-t1_0",".txt")
data4=np.loadtxt(filename)
#~ colors = plt.cm.jet(np.linspace(0, 1, 2))
colors1 = ['b', 'b', ]
colors = ['r', 'r']
colors2 = ['g', 'g']
colors3 = ['c', 'c']
# set up lines and points
lines = sum([ax.plot([], [], [], '-', c=c)
             for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors], [])
lines1 = sum([ax.plot([], [], [], '-', c=c)
             for c in colors1], [])
pts1 = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors1], [])
lines2 = sum([ax.plot([], [], [], '-', c=c)
             for c in colors2], [])
pts2 = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors2], []) 
           
lines3 = sum([ax.plot([], [], [], '-', c=c)
             for c in colors3], [])
pts3 = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors3], [])           
def init():
    for line, pt, line1, pt1, line2, pt2, line3, pt3 in zip(lines, pts, lines1, pts1, lines2, pts2, lines3, pts3):
        line.set_data([], [])
        pt.set_data([], [])
        
        line1.set_data([], [])
        pt1.set_data([], [])       
        
        line2.set_data([], [])
        pt2.set_data([], [])  
        
        line3.set_data([], [])
        pt3.set_data([], [])        
    return lines + pts + lines1 + pts1 + lines2 + pts2 + lines3 + pts3


def animate(i):
    # we'll step two time-steps per frame.  This leads to nice results.
    for line, pt, line1, pt1, line2, pt2, line3, pt3 in zip(lines, pts, lines1, pts1, lines2, pts2, lines3, pts3):
		x, y = data1[:i].T
		p, q = data2[:i].T
		p1, q1 = data3[:i].T
		p2, q2 = data4[:i].T	
			
		line.set_data(x, y)
		pt.set_data(x[-1:], y[-1:])
		
		line1.set_data(p, q)
		pt1.set_data(p[-1:], q[-1:])
		
		line2.set_data(p1, q1)
		pt2.set_data(p1[-1:], q1[-1:])	
		
		line3.set_data(p2, q2)
		pt3.set_data(p2[-1:], q2[-1:])				
    return lines + pts + lines1 + pts1 + lines2 + pts2 + lines3 + pts3

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=2000, interval=10, blit=True)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=100, metadata=dict(artist='Me'), bitrate=100)
anim.save('sh-lim-cyc-1.mp4', writer=writer)
plt.show()
