"""Main entry point"""

import sys

if sys.argv[0].endswith("__main__.py"):
    sys.argv[0] = "python -m bhrc_accounting"
from . import main

main()
