import cowsay  # installing packages the same as modules
import sys

if len(sys.argv) == 2:
    cowsay.turtle("hello, " + sys.argv[1])
