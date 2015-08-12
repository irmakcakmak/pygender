#include <python2.7/Python.h>
#include "gender.c"

// Function that does the work.
static PyObject* py_getGender(PyObject* self, PyObject* args)
{
    char *name;
    PyArg_ParseTuple(args, "s", &name);
    return Py_BuildValue("c", get_gender(name,0,0));
}

// Bind python function to c function here
static PyMethodDef pygender_methods[] = {
    {"get_gender", py_getGender, METH_VARARGS},
    {NULL, NULL}
};

// Python module __init__ function is here. Name is important
void initpygender()
{
    (void) Py_InitModule("pygender", pygender_methods);
}
