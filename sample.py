import os;
import sys;

print(os.path.dirname(__file__))
print(os.path.basename(__file__))

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
