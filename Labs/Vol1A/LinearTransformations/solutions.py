# solutions.py
"""Volume I: Linear Transformations. Solutions file."""

import time
import timeit
import numpy as np
from random import random
from matplotlib import pyplot as plt, animation

def random_vector(n):
    """Generate a random vector of length n as a list."""
    return [random() for i in xrange(n)]

def random_matrix(n):
    """Generate a random nxn matrix as a list of lists."""
    return [[random() for j in xrange(n)] for i in xrange(n)]

def matrix_vector_product(A, x):
    """Compute the matrix-vector product Ax (as a list)."""
    m, n = len(A), len(x)
    return [sum([A[i][k] * x[k] for k in range(n)]) for i in range(m)]

def matrix_matrix_product(A, B):
    """Compute the matrix-matrix product AB (as a list of lists)."""
    m, n, p = len(A), len(B), len(B[0])
    return [[sum([A[i][k] * B[k][j] for k in range(n)])
                                    for j in range(p) ]
                                    for i in range(m) ]

# Solutions ===================================================================

def prob1(N=8):
    """Use time.time(), timeit.timeit(), or %timeit to time
    matrix_vector_product(n) and matrix-matrix-mult(n) with
    increasingly large inputs. Generate the inputs A, x, and B with
    random_matrix() and random_vector()} (so each input will be nxn or nx1).
    Only time the multiplication functions, not the generating functions.

    Report your findings in a single figure with two subplots: one with matrix-
    vector times, and one with matrix-matrix times. Choose a domain for n so
    that your figure accurately describes the growth, but avoid values of n
    that lead to execution times of more than 1 minute.
    """
    domain = 2**np.arange(1,N+1)
    vector_times, matrix_times = [], []

    for n in domain:
        A = random_matrix(n)
        x = random_vector(n)
        B = random_matrix(n)

        start = time.time()
        matrix_vector_product(A, x)
        vector_times.append(time.time() - start)

        start = time.time()
        matrix_matrix_product(A, B)
        matrix_times.append(time.time() - start)

    plt.subplot(121)
    plt.plot(domain, vector_times, 'b.-', lw=2, ms=15)
    plt.xlabel("n", fontsize=14); plt.ylabel("Seconds", fontsize=14)
    plt.title("Matrix-Vector Multiplication")

    plt.subplot(122)
    plt.plot(domain, matrix_times, 'g.-', lw=2, ms=15)
    plt.xlabel("n", fontsize=14)
    plt.title("Matrix-Matrix Multiplication")

    plt.show()


def prob2(N=8):
    """
    """

    domain = 2**np.arange(1,N+1)
    vector_times, matrix_times = [], []
    npvect_times, npmatr_times = [], []

    for n in domain:
        A = random_matrix(n)
        x = random_vector(n)
        B = random_matrix(n)

        # Time list-list operations.
        start = time.time()
        matrix_vector_product(A, x)
        vector_times.append(time.time() - start)

        start = time.time()
        matrix_matrix_product(A, B)
        matrix_times.append(time.time() - start)

        # Time NumPy operations.
        A, B, x = np.array(A), np.array(B), np.array(x)
        start = time.time()
        A.dot(x)
        npvect_times.append(time.time() - start)

        start = time.time()
        A.dot(B)
        npmatr_times.append(time.time() - start)

    plt.subplot(121)
    plt.plot(domain, vector_times, '.-', lw=2, ms=15,
                                            label="Matrix-Vector with Lists")
    plt.plot(domain, matrix_times, '.-', lw=2, ms=15,
                                            label="Matrix-Matrix with Lists")
    plt.plot(domain, npvect_times, '.-', lw=2, ms=15,
                                            label="Matrix-Vector with NumPy")
    plt.plot(domain, npmatr_times, '.-', lw=2, ms=15,
                                            label="Matrix-Matrix with NumPy")
    plt.xlabel("n", fontsize=14); plt.ylabel("Seconds", fontsize=14)
    plt.legend(loc="upper left")

    plt.subplot(122)
    plt.loglog(domain, vector_times, '.-', lw=2, ms=15, basex=2, basey=2,
                                            label="Matrix-Vector with Lists")
    plt.loglog(domain, matrix_times, '.-', lw=2, ms=15, basex=2, basey=2,
                                            label="Matrix-Matrix with Lists")
    plt.loglog(domain, npvect_times, '.-', lw=2, ms=15, basex=2, basey=2,
                                            label="Matrix-Vector with NumPy")
    plt.loglog(domain, npmatr_times, '.-', lw=2, ms=15, basex=2, basey=2,
                                            label="Matrix-Matrix with NumPy")
    plt.xlabel("n")
    plt.show()

# Horsefeathers ===============================================================

def plotOldNew(old, new):
    """Display a plot of points before and after a transform.

    Inputs:
        old ((2,n) ndarray): Array containing points in R2 stored as columns.
        new ((2,n) ndarray): Array containing points in R2 stored as columns.
    """
    window = [-1,1,-1,1]

    plt.subplot(211)
    plt.title("Before")
    plt.plot(old[0], old[1], 'k,')
    plt.axis(window)
    plt.gca().set_aspect("equal")

    plt.subplot(212)
    plt.title("After")
    plt.plot(new[0], new[1], 'k,')
    plt.axis(window)
    plt.gca().set_aspect("equal")

    plt.show()

# Problem 3
def stretch(A, a, b):
    """Scale the points in 'A' by 'a' in the x direction and 'b' in the
    y direction.

    Inputs:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        a (float): scaling factor in the x direction.
        b (float): scaling factor in the y direction.
    """
    return np.dot([[a, 0],[0, b]], A)

def shear(A, a, b):
    """Slant the points in 'A' by 'a' in the x direction and 'b' in the
    y direction.

    Inputs:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        a (float): scaling factor in the x direction.
        b (float): scaling factor in the y direction.
    """
    return np.dot([[1, a],[b, 1]], A)

def rotation(A, theta):
    """Rotate the points in 'A' about the origin by 'theta' radians.

    Inputs:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        theta (float): The rotation angle in radians.
    """
    return np.dot([[np.cos(theta),-np.sin(theta)],
                   [np.sin(theta),np.cos(theta)]], A)

def reflection(A, a, b):
    """reflect the points in 'A' about the origin by 'theta' radians.

    Inputs:
        A ((2,n) ndarray): Array containing points in R2 stored as columns.
        theta (float): The rotation angle in radians.
    """
    return np.dot([[a**2 - b**2, 2*a*b],
                   [2*a*b, b**2 - a**2]], A)/(a**2 + b**2)

# Problem 4
def translate(A, a, b):
    """Translate the points in A by the vector b.

    Inputs:
        A (array) - Array of size (2,n) containing points in R2 stored as columns.
        b (2-tuple (b1,b2)) - Translate points by b1 in the x direction and by b2
            in the y direction.
    """
    return A + np.vstack(b)


# Problem 5
def solar_system(T, omega_e, omega_m, N=400):
    """Plot the trajectories of the earth and moon over the time interval [0,T]
    using 'N' time steps.

    Parameters:
        T (int): The final time.
        omega_e (float): The earth's angular velocity.
        omega_m (float): The moon's angular velocity.
        N (int): The number of time steps to use. Defaults to 400.
    """

    time = np.linspace(0, T, N)
    earth, moon = [np.array([10,0])], [np.array([11,0])]

    def rotation(theta):
        return np.array([[np.cos(theta),-np.sin(theta)],
                         [np.sin(theta),np.cos(theta)]])

    for t in time[1:]:
        earth.append(rotation(t*omega_e).dot(earth[0]))
        moon.append(rotation(t*omega_m).dot([1, 0]) + earth[-1])

    earth = np.transpose(earth)
    moon = np.transpose(moon)

    plt.plot(earth[0], earth[1], label="Earth")
    plt.plot(moon[0], moon[1], label="Moon")
    plt.gca().set_aspect("equal")
    plt.legend(loc="upper left")
    plt.show()

    return earth, moon

def solar_system_animation(earth, moon):
    """Animate the earth orbiting the sun and the moon orbiting the earth.

    Inputs:
        earth ((2,N) ndarray): The earth's postion with x-coordinates on the
            first row and y coordinates on the second row.
        moon ((2,N) ndarray): The moon's postion with x-coordinates on the
            first row and y coordinates on the second row.
    """

    animation_fig = plt.figure(1)                   # Make a new figure.
    plt.axis([-15,15,-15,15])                       # Set the window limits.
    plt.gca().set_aspect("equal")                   # Make the window square.

    earth_dot,  = plt.plot([],[], 'bo', ms=10)      # Blue dot for the earth.
    earth_path, = plt.plot([],[], 'b-')             # Blue line for the earth.
    moon_dot,   = plt.plot([],[], 'go', ms=5)       # Green dot for the moon.
    moon_path,  = plt.plot([],[], 'g-')             # Green line for the moon.
    plt.plot([0],[0],'y*',ms=30)                    # Yellow star for the sun.

    def animate(index):
        """Update the four earth and moon plots."""
        earth_dot.set_data(earth[0,index], earth[1,index])
        earth_path.set_data(earth[0,:index], earth[1,:index])
        moon_dot.set_data(moon[0,index], moon[1,index])
        moon_path.set_data(moon[0,:index], moon[1,:index])
        return earth_dot, earth_path, moon_dot, moon_path

    a = animation.FuncAnimation(animation_fig, animate,
                                frames=earth.shape[1], interval=25)
    plt.show()

if __name__ == '__main__':
    # prob1(8)
    # prob2(8)
    a, b = solar_system(2*np.pi, 1, 13)
    solar_system_animation(a, b)
    pass

# Old Problem 5
def rotatingParticle(time, omega, direction, speed):
    """Display a plot of the path of a particle P1 that is rotating
    around another particle P2.

    Inputs:
     - time (2-tuple (a,b)): Time span from a to b seconds.
     - omega (float): Angular velocity of P1 rotating around P2.
     - direction (2-tuple (x,y)): Vector indicating direction.
     - speed (float): Distance per second.
    """
    direction = np.array(direction)
    T = np.linspace(time[0],time[1],100)
    start_P1 = [1,0]
    posP1_x = []
    posP1_y = []

    for t in T:
        posP2 = speed*t*direction/la.norm(direction)
        posP1 = translate2D(rotate2D(start_P1, t*omega), posP2)[0]
        posP1_x.append(posP1[0])
        posP1_y.append(posP1[1])

    plt.plot(posP1_x, posP1_y)
    plt.gca().set_aspect('equal')
    plt.show()
