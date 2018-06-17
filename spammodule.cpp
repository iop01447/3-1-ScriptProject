#include "python.h" 
#include <iostream>
#include <fstream>
#include <string>

static PyObject *
spam_save(PyObject *self, PyObject *args)
{
	const char* str = NULL;
	
	if (!PyArg_ParseTuple(args, "s", &str)) 
		return NULL;

	std::ofstream out("data.txt");
	std::string s(str);
	out << s;
}

//static PyObject*
//spam_load(PyObject *self, PyObject *args)
//{
//	std::ifstream in("data.txt");
//	std::string str;
//	while (!in.eof())
//		str.push_back(in.get());
//
//	return Py_BuildValue("s", str.c_str());
//}

static PyMethodDef SpamMethods[] = {
	{ "save", spam_save, METH_VARARGS, "ofstream output file." },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",         
	"It is out project module.", 
	-1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
	return PyModule_Create(&spammodule);
}
