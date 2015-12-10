# datapackage-bigquery-py

[![Travis](https://img.shields.io/travis/okfn/datapackage-bigquery-py.svg)](https://travis-ci.org/okfn/datapackage-bigquery-py)
[![Coveralls](http://img.shields.io/coveralls/okfn/datapackage-bigquery-py.svg?branch=master)](https://coveralls.io/r/okfn/datapackage-bigquery-py?branch=master)

Generate and load BigQuery tables based on Data Package.

## Usage

This section is intended to be used by end-users of the library.

> See section below how to get authentificated service.

Package represents Data Package stored as Big Query dataset:

```python
from dpbq import Package

package = Package(<service>, 'project_id', 'dataset_id')
package.get_resources()
package.export()
```

Dataset represents a native Big Query dataset:

```python
from dpbq import Dataset

dataset = Dataset(<service>, 'project_id', 'dataset_id')
dataset.get_tables()
```

### Authentification

To start using Google BigQuery service:
- Create a project - [link](https://console.developers.google.com/home/dashboard)
- Create a service key - [link](https://console.developers.google.com/apis/credentials)
- Add environment variables extracted from previous step json:
    - GOOGLE_CLIENT_EMAIL
    - GOOGLE_PRIVATE_KEY (for bash `export VAR=$'...'` to no not escape newlines)

Then you can use environment variables to get `client_email` and `private_key`:

```python
import os

client_email = os.environ['GOOGLE_CLIENT_EMAIL']
private_key = os.environ['GOOGLE_PRIVATE_KEY']
```

## Development

This section is intended to be used by tech users collaborating
on this project.

### Getting Started

To activate virtual environment, install
dependencies, add pre-commit hook to review and test code
and get `run` command as unified developer interface:

```
$ source activate.sh
```

### Reviewing

The project follow the next style guides:
- [Open Knowledge Coding Standards and Style Guide](https://github.com/okfn/coding-standards)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

To check the project against Python style guide:

```
$ run review
```

### Testing

To run tests with coverage check:

```
$ run test
```

Coverage data will be in the `.coverage` file.
