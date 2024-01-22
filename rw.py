import matplotlib.pyplot as plt

from random_walk import randomwalk

while True:
    # make a random walk
    rw=randomwalk(50000)
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(10,6),dpi=128)
    point_numbers= range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap='Blues',edgecolors='none',s=1)
    ax.set_aspect('equal')
    
    #emphasize the first and last plotted point
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)
    
    #Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running=input('Keep making new paths? (y/n)')
    if keep_running == 'n' :
        break