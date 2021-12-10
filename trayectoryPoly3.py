# Library for math operations optimized in C programming
import numpy as np
# Library for plotting
import matplotlib.pyplot as plt
import csv

# Trayectory class
class Poly3:
    # Parameters
    def __init__(self, qo, qf, vo, vf, to, tf, step):
        self.qo = qo
        self.qf = qf
        self.vo = vo
        self.vf = vf
        self.to = to
        self.tf = tf
        self.step = step
        # A matrix 
        self.A = np.array([[1, self.to, self.to**2, self.to**3], 
                      [0, 1, 2*self.to, 3*self.to**2],
                      [1, self.tf, self.tf**2, self.tf**3],
                      [0, 1, 2*self.tf, 3*self.tf**2]])
        # b matrix 
        self.b = np.array([[self.qo], [self.vo], [self.qf], [self.vf]])
        # x matrix 
        self.x = np.dot(np.linalg.inv(self.A), self.b)
        # filling position and velocity vectors with zeros to optimize the code 
        self.q_vec = np.zeros((len(np.arange(0, 10, self.step))))
        self.v_vec = np.zeros((len(np.arange(0, 10, self.step))))
        # time vector 
        self.t_vec = np.arange(0, 10, self.step)

    def trayectory(self):
        # Funtion that calculates the position and velocity during the trajectory
        a0 = self.x[0]
        a1 = self.x[1]
        a2 = self.x[2]
        a3 = self.x[3]

        for i, t in enumerate(self.t_vec):
            # indexing the vectors with the corresponding value
            self.q_vec[i] = a0 + a1*t + a2*(t**2) + a3*(t**3) 
            self.v_vec[i] = a1 + 2*a2*t + 3*a3*(t**2)

    def plot(self):
        plt.figure()
        plt.plot(self.t_vec, self.q_vec, label="Position")
        plt.plot(self.t_vec, self.v_vec, label="Velocity")
        plt.scatter([self.to, self.tf],[self.qo, self.qf])
        plt.scatter([self.to, self.tf],[self.vo, self.vf])
        plt.annotate(f'({self.to},{self.qo})', xy=(self.to, self.qo + 4))
        plt.annotate(f'({self.tf},{self.qf})', xy=(self.tf, self.qf + 4))
        plt.annotate(f'({self.to},{self.vo})', xy=(self.to, self.vo - 8))
        plt.annotate(f'({self.tf},{self.vf})', xy=(self.tf, self.vf - 8))
        plt.title("Third degree polynomial")
        plt.legend()
        plt.show()

    def export_to_csv(self):
        with open("trajectory_data_poly3.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(['Time', 'Position', 'Velocity'])
            for i in range(len(self.t_vec)):
                data = [self.t_vec[i], self.q_vec[i], self.v_vec[i]]
                writer.writerow(data)

def main():
    
    while True:
        try:
            t0 = int(input("Enter t0: "))
            if t0 < 0:
                print("t0 must be > 0")
                continue
            q0 = int(input("Enter q0: "))
            v0 = int(input("Enter v0: "))
        except ValueError:
            print("Only numbers please")
            continue

        break

    while True:
        try:
            tf = int(input("Enter tf: "))
            if tf < t0:
                print("t0 must be < tf")
                continue
            qf = int(input("Enter qf: "))
            vf = int(input("Enter vf: "))
            step = float(input("Enter the step: "))
        except ValueError:
            print("Only numbers please")
            continue
        if step < 0:
            print("step must be > 0")
            continue
        else:
            break

    # ej = Poly3(1, 8, -2, 0, 2, 5, 1e-1)
    ej = Poly3(q0, qf, v0, vf, t0, tf, step)
    ej.trayectory()
    ej.plot()
    ej.export_to_csv()


if __name__ == "__main__":
    main()