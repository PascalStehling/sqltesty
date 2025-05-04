# sqltesty

A command-line tool to test SQL queries using DuckDB and CSV fixtures.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation

```bash
pip install sqltesty
```

## Usage

The `sqltesty` command looks for SQL files in your project and tests them against fixture data.

```bash
# Run all SQL tests with default settings
sqltesty

# Specify a custom test directory
sqltesty --test-dir=custom/tests/path

# Run with verbose output
sqltesty --verbose
```

The verbose output now includes enhanced error highlighting with color coding:
- Green for matching values and passed tests
- Red for mismatched values and failed tests
- Yellow for structural differences

Key features of the enhanced output:
- **Vertical alignment** of differences for improved visual clarity
- **Row-by-row comparison** that clearly shows which specific rows have issues
- **Color-coded output** to quickly identify discrepancies
- **Detailed column analysis** to understand patterns in the data

This makes it easier to identify and fix issues in your SQL queries, especially when dealing with complex datasets.

## Test Structure

- Place your SQL files anywhere in your repository
- Create a test directory (default: `tests/sqltesty`)
- For each SQL file, create a subdirectory with the same name (without extension)
- Within each subdirectory, place:
  - `output.csv`: The expected output of your SQL query
  - Other CSV files named after tables referenced in your SQL query

### Example Structure

```
/your-project
  /some-dir
    query1.sql
    query2.sql
  /tests
    /sqltesty
      /query1
        customers.csv     # Table data
        products.csv      # Table data
        output.csv        # Expected query result
      /query2
        table1.csv        # Table data
        output.csv        # Expected query result
```

## Development

```bash
# Install development dependencies
uv sync --all-groups

# Run tests
uv run pytest
```

If you want to run the examples, just do

```
cd examples

sqltesty
```
