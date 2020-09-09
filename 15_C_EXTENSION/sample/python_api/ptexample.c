#include "pysample.h"


/* An extension function that uses the exported API */
static PyObject* print_point(PyObject* self, PyObject* args)
{
	Point* p;
	PyObject* obj;

	if (!PyArg_ParseTuple(args, "O", &obj))
	{
		return NULL;
	}

	/* Note: this is defined in a different module */
	p = PyPoint_AsPoint(obj);
	if (!p)
	{
		return NULL;
	}
	printf("(%f, %f)\n", p->x, p->y);
	return Py_BuildValue(""); // None
}

static PyMethodDef PtExampleMethods[] = {
	{"print_point", print_point, METH_VARARGS, "output a point"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef PtExampleModule = {
	PyModuleDef_HEAD_INIT,
	"ptexample",
	"A module that imports a API",
	-1,
	PtExampleMethods
};

/* Module initialization function */
PyMODINIT_FUNC PyInit_ptexample(void)
{
	PyObject* m;

	m = PyModule_Create(&PtExampleModule);
	if (m == NULL)
	{
		return NULL;
	}

	/* Import sample, loading its API functions */
	if (!import_sample())
	{
		return NULL;
	}

	return m;
}