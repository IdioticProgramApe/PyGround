#ifndef PYSAMPLE_C_API
#define PYSAMPLE_C_API

#include "Python.h"
#include "sample.h"

#ifdef __cplusplus
extern "C" {
#endif // __cplusplus

/* public API table */
typedef struct 
{
	Point* (*aspoint)(PyObject*);
	PyObject* (*frompoint)(Point*, int);
} _PointAPIMethods;

#ifndef PYSAMPLE_MODULE

/* Method table in external module */
static _PointAPIMethods* _point_api = 0;

/* Import the API table from sample */
static int import_sample(void)
{
	_point_api = (_PointAPIMethods*)PyCapsule_Import("sample._point_api", 0);
	return (_point_api != NULL) ? 1 : 0;
}

#define PyPoint_AsPoint(obj) (_point_api->aspoint)(obj)
#define PyPoint_FromPoint(obj) (_point_api->frompoint)(obj)
#endif // !PYSAMPLE_MODULE

#ifdef __cplusplus
}
#endif // __cplusplus

#endif // !PYSAMPLE_C_API

