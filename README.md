# plawnekjx-python

Python bindings for [Plawnekjx](https://plawnekjx.re).

# Some tips during development

To build and test your own wheel, do something along the following lines:

```
set PLAWNEKJX_VERSION=16.0.1-dev.7 # from C:\src\plawnekjx\build\tmp-windows\plawnekjx-version.h
set PLAWNEKJX_EXTENSION=C:\src\plawnekjx\build\plawnekjx-windows\x64-Release\lib\python3.10\site-packages\_plawnekjx.pyd
cd C:\src\plawnekjx\plawnekjx-python\
pip wheel .
pip uninstall plawnekjx
pip install plawnekjx-16.0.1.dev7-cp34-abi3-win_amd64.whl
```
