import numpy as np

def Membrane(Nx, Ny, lamb):
  
    x = np.linspace(0, 1, Nx)
    y = np.linspace(0, 4, Ny)
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    u = np.zeros((Nx, Ny))
    u[:, 0] = 0
    u[:, -1] = 1.4
    u[0, :] = 1.4 * np.sin(4.5 * np.pi * y / 4)
    u[-1, :] = 1.4 * np.sin(4.5 * np.pi * y / 4)
    prev = np.copy(u)
    iterations = 0
    done = False
    
    while (done!=True):
        for i in range(1, Nx-1):
            for x in range(1, Ny-1):
                u_new = 0.5 * ((dx**2 * (u[i, x+1] + u[i, x-1]) + dy**2 * (u[i+1, x] + u[i-1, x])) / (dx**2 + dy**2))
                u[i, x] = (1 - lamb) * u[i, x] + lamb * u_new
        
        rel_error = (u - prev) / (np.abs(u) + 1e-8)
        norm_error = np.linalg.norm(rel_error, 'fro')
        if norm_error < 0.001: #tolerance
            done = True

        prev = np.copy(u)
        iterations += 1
    print(iterations)


