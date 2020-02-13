import numpy as np
import matplotlib.pyplot as plt
import basic as stat 

def mandelbrot( h,w, maxit=20 ):
	y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
	c = x+y*1j
	z = c
	divtime = maxit + np.zeros(z.shape, dtype=int)

	for i in range(maxit):
		z = z**2 + c
		diverge = z*np.conj(z) > 2**2            # who is diverging
		div_now = diverge & (divtime==maxit)  # who is diverging now
		divtime[div_now] = i                  # note when
		z[diverge] = 2                        # avoid diverging too much

	return divtime



def main():
	a = np.arange(15).reshape(3, 5)
	stat.axes(a)
	plt.imshow(mandelbrot(1000,1000))
	plt.show()


if __name__ == "__main__":
    main()