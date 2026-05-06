import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta, x0=0, y0=0):
        self.v0 = v0
        self.theta = math.radians(theta)  # store in radians
        self.x0 = x0
        self.y0 = y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.t = 0
        self.positions = [(self.x, self.y)]

    def __move(self, dt):
        self.vy -= 9.81 * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.t += dt
        self.positions.append((self.x, self.y))

    def range(self,dt=0.01):
        self.reset()
        
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self):
        self.reset()
        dt = 0.01
        while self.y >= 0:
            self.__move(dt)
        plt.plot([p[0] for p in self.positions], [p[1] for p in self.positions])
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Putanja projektila')
        plt.grid(True)
        plt.show()
