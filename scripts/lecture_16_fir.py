### Construct an impulse response from some desired amplitude
### response
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig

# Filter length
N = 15
# Midpoint of the filter
M = (N - 1) / 2
# Cutoff frequency
omega_c = 0.4 * np.pi

fig, axs = plt.subplots(1, 2)

# Generate the frequencies that we sample, omega_k = 2 * pi * k / N
omega_k = np.arange(start=0, stop=N, dtype=np.float) * 2 * np.pi / N
# Desired amplitude response is high before cutoff frequency
# Also account of 2pi periodicity
A_des = ((omega_k <= omega_c) | (omega_k >= 2*np.pi - omega_c)) * 1
# Linear phase filter
phase = M * omega_k

# Impulse response is the IFFT of the sampled frequency response
imp = np.real(np.fft.ifft(A_des * np.exp(-1j * phase)))

axs[0].set_xlabel('Time / $n$')
axs[0].set_ylabel('$h[n]$')
axs[0].stem(imp)

# Generate frequency response from the impulse response
freq, freq_resp = sig.freqz(b=imp, whole=True)

axs[1].set_xlabel('$\omega$ / rads')
axs[1].set_ylabel('$H(\omega)$')
axs[1].plot(freq, np.abs(freq_resp), 'b')
# Plot the sampled amplitude response on top of the frequency response
axs[1].plot(omega_k, A_des, 'ro')

plt.show()
