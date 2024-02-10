import subprocess


def main():
    # Publish to TestPyPI
    subprocess.run(
        ["poetry", "publish", "--build", "--repository", "testpypi"], check=True
    )


if __name__ == "__main__":
    main()
