import subprocess
# op Windows vervang je -c door -n!
# er is hier geen input
completed = subprocess.run("ping -c 2 www.google.be", capture_output=True,text=True,shell=True)
print(completed.returncode)
print(completed.stdout)
print(completed.stderr)
