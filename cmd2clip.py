import argparse
import platform
import re

import pyperclip

parser = argparse.ArgumentParser()
parser.add_argument("--linux", "-l", action="store_true")
args = parser.parse_args()


def remove_prefix(message: str) -> str:
    WINDOWS_PREFIX = r"(\n)?C:.*?\n(\(.*?\)\s+)*\$"
    LINUX_PREFIX = r"(\n)?.*?\$"

    current_os = platform.system()
    if current_os == "Windows":
        # use Cmder
        prefix = WINDOWS_PREFIX
    elif current_os == "Linux":
        prefix = LINUX_PREFIX

    if args.linux:
        prefix = LINUX_PREFIX

    return re.sub(prefix, "\n$", message)


def remove_return_char(message: str) -> str:
    return message.replace("\r", "")


cmd: str = pyperclip.paste()

if "\r" in cmd:
    cmd = remove_return_char(cmd)

out: str = remove_prefix(cmd)
pyperclip.copy(out)
print(out)
