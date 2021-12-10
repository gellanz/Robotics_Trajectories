# Library for math operations optimized in C programming
import numpy as np
# Library for plotting
import matplotlib.pyplot as plt
import csv

# Trayectory class
class Trapezoidal:
    # Parameters
    def __init__(self, qo, qf, V, to, tf, step):
        self.qo = qo
        self.qf = qf
        self.V = V
        self.to = to
        self.tf = tf
        self.step = step
        # A matrix 
        self.tb = (self.qo - self.qf + (self.V*self.tf)) / self.V
        # time vector 
        self.t_vec1 = np.arange(0, self.tb, self.step)
        self.t_vec2 = np.arange(self.tb, self.tf - self.tb, self.step)
        self.t_vec3 = np.arange(self.tf - self.tb, self.tf, self.step)
        self.t_vec = np.concatenate((self.t_vec1, self.t_vec2, self.t_vec3))
        # filling position and velocity vectors with zeros to optimize the code 
        self.q_vec = np.zeros(len(self.t_vec1) + len(self.t_vec2) + len(self.t_vec3))
        self.v_vec = np.zeros(len(self.t_vec1) + len(self.t_vec2) + len(self.t_vec3))

    def trayectory(self):
        # Funtion that calculates the position and velocity during the trajectory
        i = 0
        for t in range(len(self.t_vec1)):
            # indexing the vectors with the corresponding value
            self.q_vec[i] = self.qo + (self.V * self.t_vec1[t]**2)/(2*self.tb)
            self.v_vec[i] = self.V * self.t_vec1[t] / self.tb
            i += 1
        
        for t in range(len(self.t_vec2)):
            # indexing the vectors with the corresponding value
            self.q_vec[i] = (self.qo + self.qf - self.V*self.tf) / 2 + (self.V * self.t_vec2[t])
            self.v_vec[i] = self.V
            i += 1

        for t in range(len(self.t_vec3)):
            self.q_vec[i] = self.qf - (self.V * self.tf**2 / (2*self.tb)) + (self.V*self.tf / self.tb)* self.t_vec3[t] - (self.V/(2*self.tb))*self.t_vec3[t]**2
            self.v_vec[i] = (self.V*self.tf / self.tb) - (self.V/(self.tb))*self.t_vec3[t]
            i += 1

    def plot(self):
        plt.figure()
        plt.plot(self.t_vec, self.q_vec, label="Position")
        plt.plot(self.t_vec, self.v_vec, label="Velocity")
        plt.title("Trapezoidal")
        plt.legend()
        plt.show()

    def export_to_csv(self):
        with open("trajectory_data_trap.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(['Time', 'Position', 'Velocity'])
            for i in range(len(self.t_vec)):
                data = [self.t_vec[i], self.q_vec[i], self.v_vec[i]]
                writer.writerow(data)

def main():
    
    while True:
        try:
            t0 = int(input("Enter t0: "))
            q0 = int(input("Enter q0: "))
            V = int(input("Enter V: "))
        except ValueError:
            print("Only numbers please")
            continue

        if t0 < 0:
            print("t0 must be > 0")
            continue
        else:
            break

    while True:
        try:
            tf = int(input("Enter tf: "))
            qf = int(input("Enter qf: "))
            step = float(input("Enter the step: "))
        except ValueError:
            print("Only numbers please")
            continue

        if tf < t0:
            print("t0 must be < tf")
            continue

        if step < 0:
            print("step must be > 0")
            continue
        else:
            break

    # ej = Trapezoidal(0, 40, 60, 0, 1, 1e-3)
    ej = Trapezoidal(q0, qf, V, t0, tf, step)
    ej.trayectory()
    ej.plot()
    ej.export_to_csv()


if __name__ == "__main__":
    main()