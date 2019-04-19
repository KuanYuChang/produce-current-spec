from base_func import get_command_output
import collections

def get_board_name():
  command = "cat /sys/devices/virtual/dmi/id/board_name"
  return get_command_output(command)

def get_processor_name():
  command = "lscpu | grep name | awk -F ':' '{print $2}'"
  return get_command_output(command)

def get_graphics_name():
  gpu_dict = collections.OrderedDict()
  command = "nvidia-smi --format=csv,noheader,nounits --query-gpu=index,name"
  for l in get_command_output(command).split("\n"):
    gpu_dict[l.split(",")[0]] = l.split(",")[1][1:]
  return gpu_dict
