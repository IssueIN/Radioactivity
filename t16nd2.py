import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import integrate
import scipy.optimize as op
from scipy.stats import chi2
from utils import fetch_values_from_folder

# Folder path
folder_path1 = 'task16/T1'
folder_path2 = 'task16/T2'
folder_path3 = 'task16/T3'
folder_path4 = 'data/task16'

# Read all data from the folder
# data = []
# distance = []
# for file in os.listdir(folder_path4):
#     if file.endswith('.csv'):
#         data.append(pd.read_csv(folder_path4 + '/' + file))
#         distance.append(float(file[:-4]))

distance, y, data = fetch_values_from_folder(folder_path4)
data = np.array(data)

d = (np.array(distance)+0.315)/100
# print(d)

n = []
for i in range(len(data)):
    n.append((float(data[i].sum())))
# print(n)

std = []
for i in range(len(data)):
    std.append((float(data[i].std())))
# print(std)

t = []
for i in range(len(data)):
    t.append(len(data[i]))

# calculate the count rate
# n_t = []
# for i in range(len(t)):
#     n_t.append(n[i]/t[i])

U = []
for i in range(len(data)):
    U.append((n[i]/t[i])*d[i]**2)

# Calculate the fraction lost due to the dead time of the detector
def fraction_lost(n, t_d):
    return np.exp(-(n)* t_d)


U = []
for i in range(len(data)):
    U.append((n[i]/t[i])*d[i]**2)

error = []
for i in range(len(data)):
    # error.append(U[i] * np.sqrt((2*0.003/d[i])**2 + (np.array(std[i])/n[i])**2))
    error.append(U[i] * np.sqrt((2*0.0021/d[i])**2 + (1/(n[i]))))

# sort d and then U according to d
d, U, error, n, t = zip(*sorted(zip(d, U, error, n, t)))
d = np.array(d)
U = np.array(U)
error = np.array(error)
n = np.array(n)

# calculate the dead time correction
n_dt = n / (t*fraction_lost(n, 2e-8))
U_dt = n_dt * d **2

# calculate the non point source effect 
def cylinder(p, r, a):
    # p radial coordinate centered at the source
    # r perpendicular distance from the source to the detector
    # a the side length of the detector
    return (1/np.pi) *  np.arctan(a/2 * r/(r**2 + p**2)) * 1/np.sqrt(1 + (2/a * (r**2 + p**2)/r)**2) * p * 2*np.pi

def cs(d, A): # predict count rate of source at distance x (A: activity)
    source_diameter = 0.010
    detector_length = 0.015
    #rho and width correspond to source_diameter and detector_length respectively
    return [A/(np.pi*source_diameter**2/4) * integrate.quad(cylinder, 0, source_diameter/2, args=(i, detector_length))[0] for i in d] * d**2



# Fitting 
def exp(x, A, k):
    return A * np.exp(-x/k)

def linear(x, m, A):
    return m*x + A


att_fit, att_cov = op.curve_fit(exp, d[6:], U[6:], p0=[15, 1]) # attenuation effect
# calculate the chi squared value, the p value and the R squared value
chisq_exp = np.sum((U[6:] - exp(d[6:], *att_fit))**2/error[6:]**2)
p_exp = stats.chi2.cdf(chisq_exp, len(d[6:])-2)
r2_exp = 1 - (np.sum((U[6:] - exp(d[6:], *att_fit))**2)/np.sum((U[6:] - np.mean(U[6:]))**2))
print(f'Exponential Chi squared value = {chisq_exp:.4f}, p value = {p_exp:.4f}, R squared value = {r2_exp:.4f}')

nps_fit, _ = op.curve_fit(lambda x, A: cs(x, A) + exp(x, *att_fit) - exp(0, *att_fit), d[:8], U[:8], p0=[8e5]) # non-point source

# Doing linear regression for selected data points
slope7, intercept7, r_value7, stderr7, intercept_stderr7 = stats.linregress(d[6:], U[6:])
# Calculate the chi squared value, the p value and the R squared value
chisq = np.sum((U[6:] - (slope7*d[6:] + intercept7))**2/error[6:]**2)
p = stats.chi2.cdf(chisq, len(d[6:])-2)
r2 = 1 - (np.sum((U[6:] - (slope7*d[6:] + intercept7))**2)/np.sum((U[6:] - np.mean(U[6:]))**2))
print(f'Linear Chi squared value = {chisq:.4f}, p value = {p:.4f}, R squared value = {r2:.4f}')

# print the results with 4 decimal places
print(f'For distance 7 onwards: slope = {slope7:.4f}, intercept = {intercept7:.4f}, stderr = {stderr7:.4f},r2_value = {r_value7**2:.4f}, intercept_stderr = {intercept_stderr7:.4f}')
# slope = []
# intercept = []
# r_value = []
# intercept_stderr = []
# for i in range(len(d)):
#     slope_, intercept_, r_value_, intercept_stderr_ = stats.linregress(d[i:], U[i:])
#     slope.append(float(slope_))
#     intercept.append(float(intercept_))
#     r_value.append(float(r_value_))
#     intercept_stderr.append(float(intercept_stderr_))

# create a csv file to store the linear regression results with 4 decimal places
# df = pd.DataFrame({'distance': d, 'slope': slope, 'intercept': intercept, 'r2_value': r_value**2, 'intercept_stderr': intercept_stderr})
# df.to_csv('task16/linear_regression.csv', index=False)

# for i in range(len(d)):
#     print(f'For distance {i} onwards: slope = {slope[i]}, intercept = {intercept[i]}, r2_value = {r_value[i]**2}, p_value = {p_value[i]}, intercept_stderr = {intercept_stderr[i]}')


x = np.linspace(0, 1, 100)
d_fit = np.linspace(0, 1, 100)
trans_nps = np.linspace(100, 100, 100)

# plot U against distance
plt.figure(figsize=(8, 5), dpi=100)
plt.plot(d, U_dt, 'o', color = "Grey", label = 'Data points with dead time correction', alpha = 0.8)
#plt.plot(x, cs(x,*nps_fit), label='Geometry Effect', color='orange')
plt.plot(x, exp(x, *att_fit), label=f'Exp Attenuation Effect: y = exp[{att_fit[0]:.2f}x/{att_fit[1]:.2f}], $R^2$ = {r2_exp:.4f}', color='green', alpha = 0.9)
plt.plot(x, slope7*x + intercept7, color = 'red', label = f'Linear Attenuation Effect: y = {slope7:.2f}x + {intercept7:.2f}, $R^2$ = {r_value7**2:.4f}',alpha = 0.9)
plt.errorbar(d, U, xerr = 0.0021,yerr=error, capsize = 3 , fmt='o', color = 'blue', alpha = 0.75)
plt.xlabel('Distance (m)')
plt.ylabel('$U = n d^2$')
plt.xlim(0, 1)
#plt.ylim(7.5, 20)
plt.legend(loc='best')
plt.grid()
plt.title('U against distance')
plt.show()