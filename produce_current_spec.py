import collections
import subprocess
import oyaml as yaml

def new_empty_section (spec, sec):
  spec[sec] = collections.OrderedDict()
  return spec[sec]

def get_command_output(com):
  return subprocess.check_output(com, shell=True).strip().decode()

def get_processor_name():
  command = "lscpu | grep name | awk -F ':' '{print $2}'"
  return get_command_output(command)

def get_graphics_name():
  gpu_dict = collections.OrderedDict()
  command = "nvidia-smi --format=csv,noheader,nounits --query-gpu=index,name"
  for l in get_command_output(command).split("\n"):
    gpu_dict[l.split(",")[0]] = l.split(",")[1][1:]
  return gpu_dict

def get_kernel_release():
  command = "uname -r"
  return get_command_output(command)

def get_os_name():
  command = "grep PRETTY_NAME /etc/os-release | awk -F '=' '{print $2}' | tr -d '\"'"
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

def get_username():
  command = "echo $USER"
  return get_command_output(command)

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
  command = "pip list --format json"
  pkg_list = eval(get_command_output(command))
  for pkg in pkg_list:
    pip_dict[pkg["name"]] = pkg["version"]
  return pip_dict

def main():
  specification = collections.OrderedDict()

  current_section = new_empty_section(specification, "hardware")
  current_section["processor"] = get_processor_name()
  current_section["graphics"] = get_graphics_name()

  current_section = new_empty_section(specification, "software")
  current_section["kernel"] = get_kernel_release()
  current_section["os"] = get_os_name()
  current_section["nv_driver"] = get_nv_driver_release()
  current_section["cuda"] = get_cuda_release()
  current_section["python"] = get_python_release()

  specification["env"] = get_env_variables()
  specification["pip"] = get_pip_packages()

  with open('current_spec.yml', 'w') as yaml_file:
    yaml.dump(specification, yaml_file, default_flow_style=False)

if __name__ == '__main__':
  main()
