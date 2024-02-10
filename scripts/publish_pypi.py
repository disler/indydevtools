import subprocess


def main():
    subprocess.run(["poetry", "publish", "--build"], check=True)


if __name__ == "__main__":
    main()
