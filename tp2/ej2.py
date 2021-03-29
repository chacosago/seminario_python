import string

texto = """ # <img alt="NumPy" src="/branding/logo/primary/numpylogo.svg" height="60">

NumPy is the fundamental package needed for scientific computing with Python.

- **Website:** https://www.numpy.org
- **Documentation:** https://numpy.org/doc
- **Mailing list:** https://mail.python.org/mailman/listinfo/numpy-discussion
- **Source code:** https://github.com/numpy/numpy
- **Contributing:** https://www.numpy.org/devdocs/dev/index.html
- **Bug reports:** https://github.com/numpy/numpy/issues
- **Report a security vulnerability:** https://tidelift.com/docs/security

It provides:

- a powerful N-dimensional array object
- sophisticated (broadcasting) functions
- tools for integrating C/C++ and Fortran code
- useful linear algebra, Fourier transform, and random number capabilities

Testing:

NumPy requires `pytest`.  Tests can then be run after installation with:

    python -c 'import numpy; numpy.test()'


Call for Contributions
----------------------

The NumPy project welcomes your expertise and enthusiasm!

Small improvements or fixes are always appreciated; issues labeled as "good
first issue" may be a good starting point. If you are considering larger
contributions to the source code, please contact us through the [mailing
list](https://mail.python.org/mailman/listinfo/numpy-discussion) first. 

Writing code isn’t the only way to contribute to NumPy. You can also: 
- review pull requests
- triage issues
- develop tutorials, presentations, and other educational materials
- maintain and improve [our website](https://github.com/numpy/numpy.org)
- develop graphic design for our brand assets and promotional materials
- translate website content
- help with outreach and onboard new contributors
- write grant proposals and help with other fundraising efforts

If you’re unsure where to start or how your skills fit in, reach out! You can
ask on the mailing list or here, on GitHub, by opening a new issue or leaving a
comment on a relevant issue that is already open.

Our preferred channels of communication are all public, but if you’d like to
speak to us in private first, contact our community coordinators at
numpy-team@googlegroups.com or on Slack (write numpy-team@googlegroups.com for
an invite).

We also have a biweekly community call, details of which are announced on the
mailing list. You are very welcome to join. 

If you are new to contributing to open source, [this
guide](https://opensource.guide/how-to-contribute/) helps explain why, what,
and how to successfully get involved.



[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org)
"""

lineas = texto.split("\n")
palabras = []
for i in range(len(lineas)):
    lineas[i] = lineas[i].strip()
    lineas[i] = lineas[i].split(" ")
    for palabra in lineas[i]:
        if (not("http" in palabra)) and (not("/" in palabra)) and (not("@" in palabra)):
            aux = palabra.lower().strip(",").strip(".").strip("\"").strip("\'").strip("*").strip(";").strip("`").strip("(").strip(")").strip("[").strip("]").strip("#").strip("<").strip(">").strip("!").strip("-").strip(":")
        if (len(aux) != 0) and (aux.isalpha()):
            palabras.append(aux)

print("-" * 15 + "Lista de palabras:" + "-" * 15)

cant = 0
for palabra in palabras:
    cant = cant + 1
    print(f"{cant} * Palabra: " + palabra)

palabras_unicas = dict.fromkeys(palabras, 0)

print("\n --- Claves del diccionario: ", palabras_unicas.keys())
print("\n --- Diccionario: ", palabras_unicas.items())

max = 0
palabra_max = ""
for palabra in palabras_unicas:
    palabras_unicas[palabra] = palabras.count(palabra)
    if palabras_unicas[palabra] > max:
        palabra_max = palabra
        max = palabras_unicas[palabra]

print("\n --- Diccionario: ", palabras_unicas.items())
print(f"La palabra mas frecuente es {palabra_max} y aparece {max} veces")
