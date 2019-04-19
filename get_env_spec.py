from base_func import *
import collections

def get_env_variables():
  env_dict = collections.OrderedDict()
  username = get_username()
  base_command = "env"
  command = base_command + " | grep -v '_='"
  exclude_env_vars = ["XDG", "TERM", "SSH", "LS_COLORS", "MAIL", "PWD", "PS1", "SHLVL", "LESS", "USER", "LOGNAME"]
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
