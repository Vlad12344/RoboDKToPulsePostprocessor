import argparse

arguments = argparse.ArgumentParser()
arguments.add_argument("-s", "--save_path", type=str, default='processedPrograms',
    help="save program in special folder")
arguments.add_argument("-n", "--name", type=str, default="path",
    help="program name")
arguments.add_argument("-i", "--initial_program", type=str, default="RoboDKPrograms/Path.txt",
    help="program name")
arguments.add_argument("-o", "--host_name", type=str, default="127.0.0.1:8081", help="robot host name")