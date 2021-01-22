import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax = plt.axes(xlim=(0.1,0.9), ylim=(-.08, .08))

ax.plot(0.5,0,'k-x')
ax.plot(0.314379724686,0,'w-o')
ax.plot(0.661620275314,0,'w-o')
ax.get_xaxis().set_ticks([])
ax.get_yaxis().set_ticks([]) 
filename = '{}{}'.format("file_0.315_u_0.196_q_0.988_T_6.50_Stag-Hunt-t1_0 (copy)",".txt")
data1=np.loadtxt(filename)


filename = '{}{}'.format("file_0.660_u_0.196_q_0.988_T_6.50_Stag-Hunt-t1_0 (copy)",".txt")
data2=np.loadtxt(filename)


colors1 = ['b', 'b', ]
colors = ['r', 'r']

# set up lines and points
lines = sum([ax.plot([], [], [], '-', c=c)
             for c in colors], [])
pts = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors], [])
lines1 = sum([ax.plot([], [], [], '-', c=c)
             for c in colors1], [])
pts1 = sum([ax.plot([], [], [], 'o', c=c)
           for c in colors1], [])
        
def init():
    for line, pt, line1, pt1 in zip(lines, pts, lines1, pts1):
        line.set_data([], [])
        pt.set_data([], [])
        
        line1.set_data([], [])
        pt1.set_data([], [])       
               
    return lines + pts + lines1 + pts1


def animate(i):
    # we'll step two time-steps per frame.  This leads to nice results.
    for line, pt, line1, pt1 in zip(lines, pts, lines1, pts1):
		x, y = data1[:i].T
		p, q = data2[:i].T
			
			
		line.set_data(x, y)
		pt.set_data(x[-1:], y[-1:])
		
		line1.set_data(p, q)
		pt1.set_data(p[-1:], q[-1:])
		
				
    return lines + pts + lines1 + pts1 

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=2500, interval=20, blit=True)

#~ Writer = animation.writers['ffmpeg']
#~ writer = Writer(fps=300, metadata=dict(artist='Me'), bitrate=1000)
#~ anim.save('sh-lim-cyc-1.mp4', writer=writer)
plt.show()
