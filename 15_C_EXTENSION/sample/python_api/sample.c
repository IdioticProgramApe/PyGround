#include <math.h>

#include "sample.h"

/* function are declared that can be called from outside */
//__declspec(dllexport) int gcd(int x, int y);
//__declspec(dllexport) int in_mandel(double x0, double y0, int n);
//__declspec(dllexport) int divide(int a, int b, int *reminder);
//__declspec(dllexport) double avg(double *a, int n);
//__declspec(dllexport) double distance(Point *p1, Point *p2);

/* Compute the greatest common divisor */
int gcd(int x, int y)
{
	int g = y;
	while (x > 0)
	{
		g = x;
		x = y % x;
		y = g;
	}
	return g;
}

/* Test if (x0, y0) is in the Mandelbrot set or not */
int in_mandel(double x0, double y0, int n)
{
	double x = 0.0, y = 0.0, xtemp;
	while (n > 0)
	{
		xtemp = x * x - y * y + x0;
		y = 2 * x * y + y0;
		x = xtemp;
		n -= 1;
		if (x * x + y * y > 4)
		{
			return 0;
		}
	} 
	return 1;
}

/* Divide 2 numbers */
int divide(int a, int b, int *reminder)
{
	int quot = a / b;
	*reminder = a % b;
	return quot;
}

/* Average values in an array */
double avg(double *a, int n)
{
	int i;
	double total = 0.0;
	for (i = 0; i < n; ++i)
	{
		total += a[i];
	}
	return total / n;
}

/* Function involving a C data structure */
double distance(Point *p1, Point *p2)
{
	// hypot: calculate square root, defined in <math.h> 
	return hypot(p1->x - p2->x, p1->y - p2->y);
}

