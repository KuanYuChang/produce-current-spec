from base_func import get_command_output

def get_processor_name():
  command = "lscpu | grep name | awk -F ':' '{print $2}'"
  return get_command_output(command)

def get_board_name():
  command = "cat /sys/devices/virtual/dmi/id/board_name"
  return get_command_output(command)

def get_graphics_name():
  gpu_dict = dict()
  command = "nvidia-smi --format=csv,noheader,nounits --query-gpu=index,name"
  for l in get_command_output(command).split("\n"):
    gpu_dict[int(l.split(",")[0])] = l.split(",")[1][1:]
  return gpu_dict

def main():
  import json
  print(
    json.dumps(
      {
        "processor": get_processor_name(),
        "board": get_board_name(),
        "graphics": get_graphics_name()
      }, indent=2
      )
    )

if __name__ == '__main__':
  main()
