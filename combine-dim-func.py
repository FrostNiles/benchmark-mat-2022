import runpy
import re
import sys
import matlab.engine

skipped = {6}
eng = matlab.engine.start_matlab()
for i in range(1, 13):
    if i in skipped:
        continue
    # CEC 2022 has 12 functions
    for j in [10, 20]:
        for k in range(1, j+1):
            args = {
                'arg1': str(i),
                'arg2': str(j),
                'arg3': str(k),
                'eng': eng
            }
            
            runpy.run_path('./run-tests.py', init_globals=args)

eng.quit()

