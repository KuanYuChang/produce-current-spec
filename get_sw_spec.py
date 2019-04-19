from base_func import get_command_output

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
