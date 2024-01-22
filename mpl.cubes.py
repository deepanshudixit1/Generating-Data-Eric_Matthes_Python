import matplotlib.pyplot as plt

x_values = range(1,3001)
y_values = [x**3 for x  in range(1,3001)]

# plt.style.use('seaborn-v0_8')
fig,ax=plt.subplots()

ax.scatter(x_values,y_values,c=y_values,cmap='Blues',s=5)

ax.set_title('Cubes of numbers',fontsize=24)
ax.set_xlabel('Numbers',fontsize=10)
ax.set_ylabel('Cubes',fontsize=10)

ax.tick_params(labelsize=10)

ax.axis([0,3100,0,30_000_000_000])

plt.show()