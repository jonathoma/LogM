def main(g, z = 0.01 + 0.05*I, f = z^2 + 0.5):
    g += circle((0, 0), 2, rgbcolor = (1, 0, 0), linestyle='-.')
    # g += complex_plot(f, (-2, 2), (-2, 2))
    counter = 1
    temp = z
    while(z.norm() <= 4 and counter < 1000):
        pt = point((real(z), imag(z)), rgbcolor=(0, 0, 0.2 * counter), size=50)
        g += plot(pt)
        z = f(z)
        counter += 1
    g += plot(point((real(temp), imag(temp)), rgbcolor=(0, 0, 1 - 0.1 * counter), size=20))
    # print "final number of iterations: ", counter
    # print "final value of z: ", z
    # print "final norm of z: ", norm(z)
    # g.show()

if __name__ == "__main__":
    g = Graphics()
    main(g)
