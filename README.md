# FormaServe Training - Python Examples

<img src="/static/images/Logo.png" align="right">

This repository showcases FormaServe’s training capabilities and provides a simple web-service application.

This project is a Flask web service application that interfaces with the Chinook SQLite database. It provides endpoints to retrieve information about tracks and employees from the database and includes custom error handling for pages not found.

This will run on the IFS of the IBM i.  Requires python and sqlite open-source packages installed.

It requires a copy of the SQLite sample database chinook which can be found in the data directory.  If you require a fresh copy of the SQLite sample database it can be found [here]([http://sqlite](https://www.sqlitetutorial.net/sqlite-sample-database/))

## Features

* Provides a web-service application
* Provides four endpoints for employees & tracks

## Installation

Clone this repository to your local machine.

```bash
git clone https://github.com/FormaServe/python-webservice.git

```

**It is advised to check-out & run the section on virtual environments with python before proceeding with the install of this app.**

Install the necessary dependencies

```bash
pip install flask jsonify

```

## Endpoints

### Get Employee by ID

URL: /employee/<int:employee_id>\
Method: GET\
Description: Retrieves a specific employee by their EmployeeId.\
Response: JSON object representing the employee, or a 404 error if not found.

### Get All Employees

URL: /employees\
Method: GET\
Description: Retrieves all employees from the employees table.\
Response: JSON array of employee objects.

## Get Track by ID

URL: /track/<int:track_id>\
Method: GET\
Description: Retrieves a specific track by its TrackId.\
Response: JSON object representing the track, or a 404 error if not found.

## Get All Tracks

URL: /tracks\
Method: GET\
Description: Retrieves all tracks from the tracks table.\
Response: JSON array of track objects.

## Pre-req's

Insure that you use PIP to install the following packages (pip install bottle etc).

```bash
pip install flask jsonify

```

## Running

Start the server by running;

```bash
python server.py

```

then call the various endpoints as documented above.

## Virtual Environment

As with all python projects, it is recommended to run this application in a virtual environment.  Follow the instructions below to get started.

### Create the Virtual Environment

Use the venv module to create a virtual environment inside the project folder. Run the following command:

```bash
# Run the Python command to create a virtual environment in the current directory
python -m venv --system-site-packages .venv
```

Replace .venv with your preferred name for the virtual environment.

### Activate the Virtual Environment

To activate the virtual environment.

#### On IBM i

```bash
source .venv/bin/activate

```

### Deactivate the Virtual Environment

When you’re done working in the virtual environment, deactivate it:

```bash
deactivate

```

**Remember to activate it whenever you work on your project. 😊**

## Error Handling

The application includes custom error handling for 404 Not Found errors.

### Custom 404 Error Page

When an endpoint is not found, the application returns a custom JSON response indicating the error.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Authors

* FormaServe Systems Ltd - *All work* - [FormaServe](https://www.formaserve.co.uk)

## Acknowledgments

* Andy Youens - FormaServe Systems Ltd 1990 - All rights reserved.
* Nick Youens - FormaServe Systems Ltd 1990 - All rights reserved.
* Jane Youens - FormaServe Systems Ltd 1990 - All rights reserved.

## Copyright © 2024 FormaServe Systems Ltd
