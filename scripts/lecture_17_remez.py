### Construct an impulse response from some desired amplitude
### response using the Remez exchange algorithm
import numpy as np
from matplotlib import pyplot as plt
from scipy import signal as sig

# Filter length
N = 11
# Amplitude response is high on [0,0.3*pi] and low on [0.5*pi,pi]
# with transition band on [0.3*pi,0.5*pi]
omega_bands = [0, 0.3 * np.pi, 0.5 * np.pi, 1 * np.pi]
# Gain of the amplitude response in the high and low parts
gains = [1, 0]

fig, axs = plt.subplots(1, 2)

# Impulse response from the Remez exchange algorithm
# using a sampling frequency of 2*pi
imp = np.real(sig.remez(N, omega_bands, gains, fs=2*np.pi))

axs[0].set_xlabel('Time / $n$')
axs[0].set_ylabel('$h[n]$')
axs[0].stem(imp)

# Generate frequency response from the impulse response
freq, freq_resp = sig.freqz(b=imp, whole=False)

axs[1].set_xlabel('$\omega$ / rads')
axs[1].set_ylabel('$H(\omega)$')
axs[1].plot(freq, np.abs(freq_resp), 'b')
# Plot the desired amplitude response on top of the frequency response
axs[1].plot(omega_bands, [1, 1, 0, 0], 'r')

plt.show()
