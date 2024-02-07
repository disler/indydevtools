import sys
import subprocess


def main():
    subprocess.run(["tox"], check=True)


if __name__ == "__main__":
    main()
