import subprocess

# Task 1
# try:
#     comnd = "ls -l /var/log/"
#     ps = subprocess.run(comnd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)#split to list without spaces
#     # ps = subprocess.run(['ls', '-l', '/var/log/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # run command ls -l /var/log in the shell

#     code = ps.returncode
#     if code == 0:
#         print(out_ps.decode())
#     else:
#         print("We have an ERROR")
#         print(err_ps.decode())
# except FileNotFoundError:
#     print("Command does not exist")
# except PermissionError:
#     print("You do not have permission to run this command please use sudo") 

#Task 2
try:
    cmd = "service status nginx"
    print("Running command: ")
    ps = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = ps.stdout.decode()
    running = "(running)" in output
    if running:
        time_running = output.splitlines()[2].split(";")[1].strip()
        print(f"Nginx is running {time_running}")
    else:
        cmd = "service restart nginx"
        ps = subprocess.run(cmd.split())
        if ps.returncode == 0:
            print("Nginx has been started")
        else:
            print("Nginx could not be started")    
except PermissionError:
    print("please use sudo")    

exit(100)

