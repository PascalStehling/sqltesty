"""Core test runner for SQL tests."""

from pathlib import Path

import click
import pandas as pd

from sqltesty.helpers import extract_order_by_columns, load_csv_files, run_query_duckdb

from sqltesty.output_formatter import (
    format_success_message,
    format_error_message,
    format_dataframe_diff,
    format_test_summary,
)


def run_sql_test(sql_file: Path, test_dir: Path, verbose: bool = False) -> bool:
    """Run a single SQL test against its fixture data.

    Args:
        sql_file: Path to the SQL file to test
        test_dir: Path to the directory containing test fixtures
        verbose: Whether to print detailed output

    Returns:
        True if the test passed, False otherwise
    """
    if verbose:
        click.echo(f"Testing {sql_file.relative_to(sql_file.parent.parent)}")

    # Find the test directory for this SQL file
    test_name = sql_file.stem
    fixture_dir = test_dir / test_name

    if not fixture_dir.exists():
        click.echo(f"Error: No test fixtures found for {test_name}", err=True)
        return False

    # Find and load table CSV files
    table_files = [f for f in fixture_dir.glob("*.csv") if f.name != "output.csv"]
    output_file = fixture_dir / "output.csv"

    if not output_file.exists():
        click.echo(f"Error: No output.csv found for {test_name}", err=True)
        return False

    if not table_files:
        click.echo(f"Error: No table CSV files found for {test_name}", err=True)
        return False

    tables, sql_query = load_csv_files(table_files, sql_file, verbose)

    try:
        actual_result = run_query_duckdb(tables, sql_query)
    except Exception as e:
        click.echo(f"Error executing SQL for {test_name}: {e}", err=True)
        return False

    # Load expected output
    expected_result = pd.read_csv(output_file)

    order_by_columns = extract_order_by_columns(sql_query)

    # Compare results with more flexible comparison
    try:
        # First check that we have the same columns
        if set(actual_result.columns) != set(expected_result.columns):
            raise AssertionError(
                f"Column mismatch: {set(actual_result.columns)} != {set(expected_result.columns)}"
            )

        # Then check that we have the same number of rows
        if len(actual_result) != len(expected_result):
            raise AssertionError(
                f"Row count mismatch: {len(actual_result)} != {len(expected_result)}"
            )

        for col in actual_result.columns:
            if actual_result[col].dtype != expected_result[col].dtype:
                raise AssertionError(f"Column '{col}' has different dtypes")

            if col in order_by_columns:
                if not actual_result[col].equals(expected_result[col]):
                    raise AssertionError(f"Values in column '{col}' don't match")
            else:
                if (
                    not actual_result[col]
                    .sort_values()
                    .reset_index(drop=True)
                    .equals(expected_result[col].sort_values().reset_index(drop=True))
                ):
                    raise AssertionError(
                        f"Values in column '{col}' don't match after sorting"
                    )

        if verbose:
            format_success_message(test_name)
        return True
    except AssertionError as e:
        error_message = str(e)
        error_type = (
            error_message.split(":")[0] if ":" in error_message else "Assertion Error"
        )

        if not verbose:
            click.echo(f"✗ Test failed: {test_name}", err=True)
        else:
            format_error_message(test_name, error_type, error_message)
            format_dataframe_diff(expected_result, actual_result)
        return False


def run_sql_tests(test_dir: Path, verbose: bool = False) -> bool:
    """Run all SQL tests in the specified directory.

    Args:
        test_dir: Directory containing SQL test files and fixtures
        verbose: Whether to print detailed output

    Returns:
        True if all tests passed, False otherwise
    """
    # Find all SQL files in the repo (parent directory of test_dir)
    repo_dir = test_dir.parent.parent if test_dir.name == "sqltest" else test_dir.parent
    sql_files = list(repo_dir.glob("**/*.sql"))

    if not sql_files:
        click.echo("No SQL files found to test", err=True)
        return False

    # Run tests for each SQL file
    results = []
    for sql_file in sql_files:
        results.append(run_sql_test(sql_file, test_dir, verbose))

    # Print summary
    total = len(results)
    passed = sum(results)
    failed = total - passed

    # Use the enhanced formatter for the summary
    format_test_summary(total, passed)

    return failed == 0
