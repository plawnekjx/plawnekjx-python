from pprint import pformat

from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer

import plawnekjx

print("Local parameters:", highlight(pformat(plawnekjx.query_system_parameters()), PythonLexer(), Terminal256Formatter()))
print(
    "USB device parameters:",
    highlight(pformat(plawnekjx.get_usb_device().query_system_parameters()), PythonLexer(), Terminal256Formatter()),
)
