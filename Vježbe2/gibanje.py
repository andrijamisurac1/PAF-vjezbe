from particle import Particle
import numpy as np
import matplotlib.pyplot as plt

cestica= Particle(25,45)
listdt= np.linspace(0.0001,0.1,100)
numericki= []
for dt in listdt:
    numericki.append(cestica.range(dt))


analiticki= (cestica.v0**2 * np.sin(2*cestica.theta)) / 9.81   
domet = cestica.range()
print(domet)

greska= []
for d in numericki:
    greska.append(abs(analiticki-d)/analiticki)

plt.plot(listdt, greska)
plt.show()