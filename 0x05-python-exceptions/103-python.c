#include <Python.h>

/**
 * print_python_float - prints basic info about Python float objects
 * @p: a PyObject pointer
 *
 * Return: Nothing.
 */

void print_python_float(PyObject *p)
{
	double value;
	PyFloatObject *floater;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (PyFloat_check(p))
	{
		floater = (PyFloatObject*)(p);
		value = floater->ob_fval;
		printf("  value: %lf\n", value);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: a PyObject pointer
 *
 * Return: Nothing.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t len;
	char *s = NULL;;
	int i, size;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (!(PyBytes_Check(p)))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = ((PyBytesObject *)p)->ob_sval;
	len = ((PyVarObject *)(p))->ob_size
	printf("  size: %d\n", (int)len);
	printf("  trying string: %s\n", s);
	size = (len + 1) < 10 ? (len + 1) : 10;
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

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
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
			if (PyFloat_Check(object))
				print_python_float(object);
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
