#!/usr/bin/env python3


import argparse


def create_dockerfile():

    parser = argparse.ArgumentParser(description="create a Dockerfile")
    parser.add_argument("--fr", type=str, help="what is your base os?", required=True)
    parser.add_argument("--workdir", type=str, help="specify the working directory", default="/usr/src/app")
    parser.add_argument("--run", type=str, required=True, help="which shell command should be run during build" )
    parser.add_argument("--copy", type=str, required=True, help="copy folder from your machine to container's base os directory")
    parser.add_argument("--cmd", type=str, required=True, help="which command should be run when the container starts")
    parser.add_argument("--filepath", type=str, required=False, help="where should the dockerfile be created", default="Dockerfile")


    args = parser.parse_args()

    dockerfile=f"FROM {args.fr}\nWORKDIR {args.workdir}\nCOPY {args.copy} .\nRUN {args.run}\nCMD {args.cmd}\n"

    with open(args.filepath, "w") as file:
        file.write(dockerfile)
        print(f"dockerfile created successfully in {args.filepath}")


if __name__ == '__main__':
    create_dockerfile()
