# Library for math operations optimized in C programming
import numpy as np
# Library for plotting
import matplotlib.pyplot as plt
import csv

# Trayectory class
class Bezier9:
    # Parameters
    def __init__(self, qo, qf, t1, t2, step):
        self.qo = qo
        self.qf = qf
        self.t1 = t1
        self.t2 = t2
        self.step = step
        # Gamma coeficients
        self.gamma1 = 126
        self.gamma2 = 420
        self.gamma3 = 540
        self.gamma4 = 315
        self.gamma5 = 70
        # time vector 
        self.t_vec1 = np.arange(0, self.t1, self.step)
        self.t_vec2 = np.arange(self.t1, self.t2, self.step)
        self.t_vec3 = np.arange(self.t2, self.t2 + 2, self.step)
        self.t_vec = np.concatenate((self.t_vec1, self.t_vec2, self.t_vec3))
        # filling position, velocity and accelaration vectors with zeros to optimize the code 
        self.q_vec = np.zeros(len(self.t_vec1) + len(self.t_vec2) + len(self.t_vec3))
        self.v_vec = np.zeros(len(self.t_vec1) + len(self.t_vec2) + len(self.t_vec3))
        self.a_vec = np.zeros(len(self.t_vec1) + len(self.t_vec2) + len(self.t_vec3))

    def trayectory(self):
        # Funtion that calculates the position and velocity during the trajectory
        i = 0
        for t in range(len(self.t_vec1)):
            # indexing the vectors with the corresponding value
            self.q_vec[i] = self.qo 
            self.v_vec[i] = 0
            self.a_vec[i] = 0
            i += 1
        
        for t in range(len(self.t_vec2)):
            # indexing the vectors with the corresponding value
            delta = (self.t_vec2[t] - self.t1) / (self.t2 - self.t1)
            mu = delta**5 * (self.gamma1 - self.gamma2*delta + self.gamma3*delta**2 - self.gamma4*delta**3 + self.gamma5*delta**4)
            mu_derivative = 5*delta**4 * (self.gamma1 - 1.2*self.gamma2*delta + 1.4*self.gamma3*delta**2 - 1.6*self.gamma4*delta**3 + 1.8*self.gamma5*delta**4)
            mu_2nd_derivative = 20*self.gamma1*delta**3 - 30*self.gamma2*delta**4 + 42*self.gamma3*delta**5 - 56*self.gamma4*delta**6 + 72*self.gamma5*delta**7
            self.q_vec[i] = self.qo + (self.qf - self.qo) * mu
            self.v_vec[i] = (self.qf - self.qo) * mu_derivative
            self.a_vec[i] = (self.qf - self.qo) * mu_2nd_derivative
            i += 1

        for t in range(len(self.t_vec3)):
            self.q_vec[i] = self.qf
            self.v_vec[i] = 0
            self.a_vec[i] = 0
            i += 1

    def plot(self):
        plt.figure()
        plt.plot(self.t_vec, self.q_vec, label="Position")
        plt.plot(self.t_vec, self.v_vec, label="Velocity")
        plt.plot(self.t_vec, self.a_vec, label="Acceleration")
        plt.title("Bezier Polynomial degree 9")
        plt.legend()
        plt.show()

    def export_to_csv(self):
        with open("trajectory_data_bezier9.csv", "w", newline='') as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(['Time', 'Position', 'Velocity', 'Acceleration'])
            for i in range(len(self.t_vec)):
                data = [self.t_vec[i], self.q_vec[i], self.v_vec[i], self.a_vec[i]]
                writer.writerow(data)

def main():
    
    while True:
        try:
            t1 = int(input("Enter t1: "))
            if t1 < 0:
                print("t0 must be > 0")
                continue
            q0 = int(input("Enter q0: "))
        except ValueError:
            print("Only numbers please")
            continue

        break

    while True:
        try:
            t2 = int(input("Enter t2: "))
            if t2 < t1:
                print("t0 must be < tf")
                continue
            qf = int(input("Enter qf: "))
            step = float(input("Enter the step: "))
        except ValueError:
            print("Only numbers please")
            continue

        if step < 0:
            print("step must be > 0")
            continue
        else:
            break

    ej = Bezier9(q0, qf, t1, t2, step)
    # ej = Bezier9(3, -2, 3, 7, 1e-1)
    ej.trayectory()
    ej.plot()
    ej.export_to_csv()

if __name__ == "__main__":
    main()