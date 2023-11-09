#include <Python.h>

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: a PyObject pointer
 *
 * Return: Nothing.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t *len = NULL;
	char *s = NULL;;
	int i, size;
	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &s, len);
	printf("  size: %d\n", (int)*len);
	printf("  trying string: %s\n", s);
	size = sizeof(s) ? sizeof(s) <= 10 : 10;
	printf("  first %d bytes: ", size);
	printf("%02x", s[0]);
	for (i = 1; i < size; i++)
		printf(" %02x", s[i]);
	printf("\n");
}

/**
 * print_python_list - prints basic info about Python lists
 * @p: a PyObject pointer
 *
 * Return: Nothing.
 */

void print_python_list(PyObject *p)
{
	int i, size, allocated;
	char *typeName;
	PyTypeObject *type;
	PyListObject *list;
	PyObject *object;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		size = (int)((PyVarObject*)(p))->ob_size;
		list = (PyListObject*)(p);
		allocated = list->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", (int)allocated);
		for (i = 0; i < size; i++)
		{
			object = list->ob_item[i];
			type = ((PyObject*)(object))->ob_type;
			typeName = (char*)type->tp_name;
			printf("Element %d: %s\n", i, typeName);
			if (PyBytes_Check(object))
				print_python_bytes(object);
		}
	}
}
