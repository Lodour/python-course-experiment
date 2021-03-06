import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)
z = np.cos(x*x)
plt.figure(figsize=(8,4))
plt.plot(x,y,label='$sin(x)$',color='red',linewidth=2)
plt.plot(x,z,'b--',label='$cos(x^2)$')
plt.xlabel('Time(s)')
plt.ylabel('Volt')
plt.title('Sin and Cos figure using pyplot')
plt.ylim(-1.2,1.2)
plt.legend()
plt.savefig('sin_cos.png',dpi=120)
plt.show()
