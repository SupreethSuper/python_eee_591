import numpy as np
from scipy.fftpack import dct

N = 512

class DCT_calc():
    def __init__(self, n, x):
        self.x = x
        self.n = n
        self.n_samples = len(self.x)
        
    def validator(self):  #to make sure that its above 256
        if(self.n <= 256):
            print(f"Error: n must be greater than 256 {self.n}")
            return False
        else:
            return True

    def dct2_loops(self):
        x_frequency = np.zeros(self.n_samples)

        for k in range(self.n_samples):
            total = 0.0
            for n in range(self.n_samples):
                angle = np.pi / self.n_samples * (n + 0.5) * k
                total += self.x[n] * np.cos(angle)
            
            x_frequency[k] = 2.0 * total
    

        return x_frequency

    def dct2_matrix(self):
        
        k = np.arrange(self.n_samples).reshape(-1, 1) # col vec of shape N,1
        n_val = np.arrange(self.n_samples).reshape(1, -1) # row vec of shape 1, N

        C = 2.0 * np.cos(np.pi / self.n_samples * (n_val + 0.5) * k)

        return C @ self.x
    

    def main(self):
        if self.validator():
        
            x_frequency_ref = dct(self.x, type=2, norm=None)
            x_frequency_loop = self.dct2_loops()
            x_frequency_matrix = self.dct2_matrix()

            # largest absolute difference over all N coefficients
            err_loop = np.max(np.abs(x_frequency_loop - x_frequency_ref))
            err_matrix = np.max(np.abs(x_frequency_matrix - x_frequency_ref))

            print(f"N = {self.n_samples}")
            print(f"Max error (loop vs scipy DCT):   {err_loop:.2e}")
            print(f"Max error (matrix vs scipy DCT): {err_matrix:.2e}")



def make_signal(n_samples):
    #it'll be too fictious for a signal to exsist without a noise
    rng = np.random.default_rng(591)
    t = np.arange(n_samples)
    return (np.sin(2.0 * np.pi * 5.0 * t / n_samples)
            + 0.5 * np.cos(2.0 * np.pi * 37.0 * t / n_samples)
            + 0.1 * rng.standard_normal(n_samples))


calc = DCT_calc(N, make_signal(N))
calc.main()


#references :
#https://docs.scipy.org/doc/scipy/tutorial/fft.html
