import subprocess

p = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # run command ls -l in the shell

out_b = p.stdout
out_b = out_b.decode()
print(out_b)

err_b = p.stderr
err_b = err_b.decode()
print(err_b)



D = subprocess.Popen("cmd", stdout=subprocess.PIPE, stderr=subprocess.PIPE)