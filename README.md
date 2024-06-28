# FormaServe Training - Python Examples

<img src="/static/images/Logo.png" align="right">

This repository showcases FormaServe’s training capabilities and provides a simple web-service application.

This will run on the IFS of the IBM i.  Requires python and sqlite open-source packages installed.

## Features

* Provides a webservice application
* Provides endpoints for
* Allows for column sorting.

## Installation

* Clone this repository to your local machine.
* Install the necessary dependencies (e.g., Python, etc.).
* Run the application using the provided scripts.

**It is advised to check-out & run the section on virtual environments with python before proceeding with the install of this app.**

## Pre-req's

Insure that you use PIP to install the following packages (pip install bottle etc).

- flask
- jsonify

## Running

Start the server by running;

```
python server.py
```

then point your browser to the following;
```
your_server:5050
```

## Virtual Environment

As with all python projects, it is recommended to run this application in a virtual environment.  Follow the instructions below to get started.

### Create the Virtual Environment

Use the venv module to create a virtual environment inside the project folder. Run the following command:

```bash
# Run the Python command to create a virtual environment in the current directory
python -m venv --system-site-packages ~/.venv
```
Replace .venv with your preferred name for the virtual environment.

### Activate the Virtual Environment

To activate the virtual environment, use the appropriate command based on your operating system:\

#### On IBM i

```bash
source ~/.venv/bin/activate
```

### Deactivate the Virtual Environment

When you’re done working in the virtual environment, deactivate it:

```bash
deactivate
```

**Remember to activate it whenever you work on your project. 😊**

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Authors

* FormaServe Systems Ltd - *All work* - [FormaServe](https://www.formaserve.co.uk)

## Acknowledgments

* Andy Youens - FormaServe Systems Ltd 1990 - All rights reserved.
* Nick Youens - FormaServe Systems Ltd 1990 - All rights reserved.
* Jane Youens - FormaServe Systems Ltd 1990 - All rights reserved.

## Copyright © 2024 FormaServe Systems Ltd
