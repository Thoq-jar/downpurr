#!/usr/bin/env python3

import os
import sys


def load_template(file):
    with open(file) as f:
        return f.read()


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: downpurr <website>")
        exit(1)

    website = args[1]
    if not website.startswith("http"):
        print("Invalid website, must start with http:// or https://!")
        exit(1)

    name = website.split("/")[-1].split(".")[0].capitalize()

    print(f"Generating app for: {name}")

    raw_template = load_template("assets/template.py")

    template = (raw_template.replace("%%{NAME}%%", name).replace("%%{SITE}%%", website))

    with open(name, "w") as f:
        f.write(template)
        f.close()

    os.system(f"chmod +x {name}")
    print(f"Generated: {name} app in current directory!")


if __name__ == '__main__':
    main()
