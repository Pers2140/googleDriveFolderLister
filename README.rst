diff-cover |pypi-version| |conda-version| |build-status| |coverage-status|
========================================================================================

Automatically find diff lines that need test coverage.
Also finds diff lines that have violations (according to tools such
as pycodestyle, pyflakes, flake8, or pylint).
This is used as a code quality metric during code reviews.

Overview
--------

Diff coverage is the percentage of new or modified
lines that are covered by tests.  This provides a clear
and achievable standard for code review: If you touch a line
of code, that line should be covered.  Code coverage
is *every* developer's responsibility!

The ``diff-cover`` command line tool compares an XML coverage report
with the output of ``git diff``.  It then reports coverage information
for lines in the diff.