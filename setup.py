from setuptools import setup, find_packages

setup(
    name="diffprompt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "groq",
        "python-dotenv",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "diffprompt=diffprompt.cli:main",
        ],
    },
)