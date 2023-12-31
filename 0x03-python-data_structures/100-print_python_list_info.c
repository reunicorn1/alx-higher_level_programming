#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p a PyObject of a list
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	int i, size, allocated;
	PyListObject *list;
	PyTypeObject* type;
	char* typeName;

	if (PyList_Check(p))
	{
		size = (int)PyList_Size(p);
		printf("[*] Size of the Python List = %d\n", size);
		list = (PyListObject*)p;
		allocated = (int)list->allocated;
		printf("[*] Allocated = %d\n", allocated);
		for (i = 0; i < size; i++)
		{
			type = Py_TYPE(PyList_GetItem(p, (Py_ssize_t)i));
			typeName = (char*)type->tp_name;
			printf("Element %d: %s\n", i, typeName);
		}
	}
}
