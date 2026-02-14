# prac-py-rapid-fuzz

Testing AI generated rapid fuzz

## Project Setup

This project uses [uv](https://docs.astral.sh/uv/) as the package manager, which provides fast Python package installation and management.

### Prerequisites

- Python 3.12 or higher
- uv package manager

### Installing uv

If you don't have uv installed, install it using pip:

```bash
pip install uv
```

Or using the standalone installer:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Project Installation

1. Clone the repository:
```bash
git clone https://github.com/Supasiti/prac-py-rapid-fuzz.git
cd prac-py-rapid-fuzz
```

2. Install the project and its dependencies:
```bash
uv sync
```

This will create a virtual environment and install all dependencies defined in `pyproject.toml`.

### Development

#### Installing Development Dependencies

Development dependencies (pytest, ruff, etc.) are automatically installed when you run:

```bash
uv sync --group dev
```

#### Running the Application

You can run the main application using:

```bash
uv run prac-py-rapid-fuzz
```

Or directly:

```bash
uv run python -m prac_py_rapid_fuzz
```

#### Running Tests

Run all tests using pytest:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=src --cov-report=html
```

#### Linting and Formatting

This project uses Ruff for linting and formatting.

Check code style:

```bash
uv run ruff check .
```

Format code:

```bash
uv run ruff format .
```

Auto-fix issues:

```bash
uv run ruff check --fix .
```

### Project Structure

```
prac-py-rapid-fuzz/
├── src/
│   └── prac_py_rapid_fuzz/
│       └── __init__.py          # Main module
├── tests/
│   ├── __init__.py
│   └── test_main.py             # Test files
├── pyproject.toml               # Project configuration and dependencies
├── .python-version              # Python version specification
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

### Adding Dependencies

To add a new dependency:

```bash
uv add package-name
```

To add a development dependency:

```bash
uv add --dev package-name
```

### Building the Project

To build the project as a package:

```bash
uv build
```

This will create distribution files in the `dist/` directory.

## License

This project is for testing and educational purposes.
