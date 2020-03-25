from argsParser import arguments
from postprocessor.programParser import program_parser, read_file
from postprocessor.RobodkUR2Pulse import Postprocessor

if __name__ == "__main__":
    args = arguments.parse_args()

    postprocessor = Postprocessor(robothost=args.host_name)
    program = read_file(args.initial_program)

    program_parser(program, postprocessor)
    postprocessor.progSave(args.save_path, args.name, show_result=True)