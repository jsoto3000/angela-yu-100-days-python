# Angela Yu - Python Day 16
## Python Packages and PyPi

- PyPi
  - Python Package Index
  - https://pypi.org/
    - The Python Package Index (PyPI) is a repository of software for the Python programming language. 
    - PyPI helps you find and install software developed and shared by the Python community. 
  - package, project, and release
    - There are a number of terms to describe software available on PyPI:
      - projects
        - name of a collection of releases and files, and information about them.  
        - are made and shared by other members of the Python community so that you can use them.
      - releases
        - specific version of a project
          - For example, the requests project has many releases
          - like "requests 2.10" and "requests 1.2.1". 
          - A release consists of one or more "files".
      - package
        - file, also known as a "package", is something that you can download and install. 
        - Because of different hardware, operating systems, and file formats, a release may have several files (packages)
          - like an archive containing source code, or
          - a binary wheel.  


- How to install a file (package) from PyPI?
  - Use pip for Installing 
    - pip is the recommended installer. 
    - The most common usage of pip is to install from the Python Package Index using a requirement specifier. 
    - Generally speaking, a requirement specifier is composed of a project name followed by an optional version specifier. 
    - PEP 440 contains a full specification of the currently supported specifiers. Below are some examples. 
      - To install the latest version of “SomeProject”:
        - Unix/macOS
          - python3 -m pip install "SomeProject"
        - Windows
          - py -m pip install --user SomeProject
      - To install a specific version:
        - Unix/macOS
          - python3 -m pip install "SomeProject==1.4"
        - Windows
          - py -m pip install "SomeProject==1.4"
        - To install greater than or equal to one version and less than another:
          - Unix/macOS
            - python3 -m pip install "SomeProject>=1,<2"
          - Windows 
            - py -m pip install "SomeProject>=1,<2"
      - To install a version that’s “compatible” with a certain version: 4 
        - Unix/macOS 
          - python3 -m pip install "SomeProject~=1.4.2"
        - Windows
          - py -m pip install "SomeProject~=1.4.2"
        - In this case, this means to install any version “==1.4.*” version that’s also “>=1.4.2”.  


- Source Distributions vs Wheels 
  - pip can install from either Source Distributions (sdist) or Wheels
    - but if both are present on PyPI, pip will prefer a compatible wheel. 
    - You can override pip`s default behavior by e.g. using its –no-binary option. 
  - Wheels are a pre-built distribution format that provides faster installation compared to Source Distributions (sdist)
    - especially when a project contains compiled extensions.
  - If pip does not find a wheel to install, it will locally build a wheel and cache it for future installs
    - instead of rebuilding the source distribution in the future.  


- Upgrading packages
  - Upgrade an already installed SomeProject to the latest from PyPI. 
    - Unix/macOS
      - python3 -m pip install --upgrade SomeProject 
    - Windows
      - py -m pip install --upgrade SomeProject

- PyCharm
  - File >>> Settings >>> Python Interpreter
  - add (+) package
