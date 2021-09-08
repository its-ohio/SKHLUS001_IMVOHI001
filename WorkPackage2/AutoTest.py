import os
import subprocess

goldenMeasue = subprocess.run(['python','Python/PythonHeterodyning.py'],capture_output=True, text=True)
output = goldenMeasue.stdout
time = output.find("('Elapsed time:', '0:00:")
print(time)