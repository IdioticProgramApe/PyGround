#include "sample.h"
#include "Python.h"

/* int gcd(int x, int y) */
static PyObject *py_gcd(PyObject *self, PyObject *args)
{
	int x, y, result;

	if (!PyArg_ParseTuple(args, "ii", &x, &y))
	{
		return NULL;
	}
	result = gcd(x, y);
	return Py_BuildValue("i", result);
}

/* int in_mandel(double x0, double y0, int n) */
static PyObject *py_in_mandel(PyObject *self, PyObject *args)
{
	double x0, y0;
	int n;
	int result;

	if (!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n))
	{
		return NULL;
	}
	result = in_mandel(x0, y0, n);
	return Py_BuildValue("i", result);
}

/* int divide(int a, int b, int *remainder) */
static PyObject *py_divide(PyObject *self, PyObject *args)
{
	int a, b, remainder, result;
	if (!PyArg_ParseTuple(args, "ii", &a, &b))
	{
		return NULL;
	}
	result = divide(a, b, &remainder);
	return Py_BuildValue("ii", result, remainder);
}