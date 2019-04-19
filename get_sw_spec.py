from base_func import *

import collections

def get_kernel_release():
  command = "uname -r"
  return get_command_output(command)

def get_os_name():
  command = "grep PRETTY_NAME /etc/os-release | awk -F '=' '{print $2}' | tr -d '\"'"
  return get_command_output(command)

def get_gcc_release():
  command = "gcc --version | head -n1 | awk '{print $4}'"
  return get_command_output(command)

def get_nv_driver_release():
  command = "head -n1 /proc/driver/nvidia/version | awk '{print $8}'"
  return get_command_output(command)

def get_cuda_release():
  command = "nvcc --version | tail -n1 | awk '{print $5}' | tr -d ','"
  return get_command_output(command)

def get_python_release():
  command = "python -V | awk '{print $2}'"
  return get_command_output(command)

def get_env_variables():
  env_dict = collections.OrderedDict()
  username = get_username()
  base_command = "TERMCAP='' env"
  command = base_command + " | grep -v '_='"
  exclude_env_vars = ["XDG", "TERM", "SSH", "LS_COLORS", "MAIL", "PWD", "PS1", "SHLVL", "LESS", "USER", "LOGNAME", "STY", "WINDOW"]
  for ex_v in exclude_env_vars:
    command += ( " | grep -v " + ex_v )
  for l in get_command_output(command).split("\n"):
    env_dict[l.split("=")[0]] = l.split("=")[1].replace(username, "GENERAL_USER")
  return env_dict

def get_pip_packages():
  pip_dict = collections.OrderedDict()
  command = "pip freeze | grep -v 'pkg-resources==0.0.0'"
  for pkg in get_command_output(command).split("\n"):
    pip_dict[pkg.split("==")[0]] = pkg.split("==")[1]
  return pip_dict
