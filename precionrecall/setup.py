import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="venkataraman",
    version="1.0.0",
    description="precision recall machine number",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="venkataraman",
    author_email="jimvenkat999@gmail.com",
    license="GNU GENERAL PUBLIC LICENSE",
    classifiers=[
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["square"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "precision.__main__:main",
        ]
    },
)