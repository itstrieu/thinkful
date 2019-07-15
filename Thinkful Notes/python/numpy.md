# Numpy Notes

**np.polyfit**

Least squares polynomial fit.

Fit a polynomial 
```
p(x) = p[0] * x**deg + ... + p[deg] of degree deg to points (x, y)
``` 

Returns a vector of coefficients p that minimises the squared error in the order deg, deg-1, … 0.

The Polynomial.fit class method is recommended for new code as it is more stable numerically.

``` python
fit = np.polyfit(xvals, ln_yodds, 1) 
```

**numpy.poly1d**

A one-dimensional polynomial class.

A convenience class, used to encapsulate “natural” operations on polynomials so that said operations may take on their customary form in code (see Examples).

Construct the polynomial x^2 + 2x + 3:

``` python
p = np.poly1d([1, 2, 3])
print(np.poly1d(p))
```

Evaluate the polynomial at x = 0.5:

```
p(0.5)
4.25
```
