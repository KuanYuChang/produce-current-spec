import subprocess

def get_command_output(com):
  return subprocess.check_output(com, shell=True).strip().decode()

def get_username():
  command = "echo $USER"
  return get_command_output(command)
