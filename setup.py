# This is custom for exile's repo, view the main one at: https://github.com/cop-discord/button_paginator
# All files are free to use.

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
desc = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="button_paginator",
    version="1.0.1",
    description="A module which allows easy implementation of button pagination for the discord bot exile.",
    long_description=desc,
    long_description_content_type="text/markdown",
    author="ozusecure & cop-discord",
    url="https://github.com/ozusecure/button_paginator",
    python_requires=">=3.6",
    packages=find_packages(include=["button_paginator", "button_paginator.*"]),
)
