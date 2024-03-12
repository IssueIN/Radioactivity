import matplotlib.pyplot as plt
import numpy as np
from utils import fetch_values_nd2, nd2, nd2_err, dead_time_correction
from solid_angle import solid_angle, solid_angle_numerical, monte_carlo_integration
from air_attenuation import fit_exp_decay

def activity_d2(n, d, dt, a = 5e-3):
    n = np.array(n)
    d = np.array(d)
    dt = np.array(dt)
    return 4 * n * d**2/ (dt * a**2)

def activity_imp(n, d, dt):
    n = np.array(n)
    d = np.array(d)
    dt = np.array(dt)
    solid_angles, solid_angle_err = solid_angle(d)
    solid_angles = np.array(solid_angles)
    return np.array([n[i] / (dt[i] * solid_angles[i]) for i in range((len(n)))])

def activity_test(n, d, dt):
    n = np.array(n)
    d = np.array(d)
    dt = np.array(dt)
    solid_angles = monte_carlo_integration(d)
    solid_angles = np.array(solid_angles)
    return n * 4 * np.pi / (dt * solid_angles)

N0 = 5e6
x, n, n_tot, dt = fetch_values_nd2('data/ndsquare_data/')
x = (np.array(x)) / 100 
n_tot_c = dead_time_correction(n_tot, dt)

# z_values = np.linspace(2e-3, 1.0, int(1e4))
# solid_angles_N0, solid_angles_N0_err = solid_angle(z_values)
# plt.plot(z_values, solid_angles_N0)

activity_improve = activity_test(n_tot_c, x, dt)
activity_improve_2 = activity_test(n_tot, x, dt)
activity_d2_ = activity_d2(n_tot, x, dt)

# nd2_ = nd2(n_tot, x, dt)
# nd2_err_ = nd2_err(x, n_tot, dt)
# plt.errorbar(x, nd2_, yerr=nd2_err_, fmt='o', label ='raw data points')
# plt.scatter(x, 1/ np.array(solid_angle(x)[0]))
# plt.plot(z_values, N_corrected)
plt.scatter(x, activity_d2_, label='nd2')
plt.scatter(x, activity_improve, label='improve')
plt.scatter(x, activity_improve_2, label='improve before deadtime')
# plt.scatter(x, np.array(n_c)/(np.array(solid_angles)), label = '2')
# plt.scatter(x, np.array(n) / (np.array(solid_angles)))
# plt.scatter(x, solid_angles)
# plt.scatter(x, n_c)
plt.legend()
plt.xlabel('distance(m)')
plt.ylabel('nd2')
plt.title('ndsquare') 
plt.show()