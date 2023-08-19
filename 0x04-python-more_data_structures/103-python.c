#include <python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about python lists
 * @p: a PyObject list object
 */

void print_python_list(PyObject *p)
{
	int size, memallo, x;
	const char *datatype;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	memalloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", memalloc);

	for (a = 0; a < size; a++)
	{
		datatype = list->ob_item[a]->ob_type->tp_name;
		printf("Elements %d: %s\n", a, type);
		if (strcmp(datatype, "bytes") == 0)
			print_python_bytes(list->ob_item[a]);
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes objects
 * @p: A PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char a, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyvarObject *)p)->ob_size + 1;

	printf(" first %d bytes: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
