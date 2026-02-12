from setuptools import setup, find_packages

setup(
    name="filesorter",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'filesorter = filesorter.main:run',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="Simple GUI tool to copy files by extension and/or name filter",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/filesorter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
)