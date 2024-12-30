"""Nox sessions for testing and linting."""

import nox
from nox_poetry import Session

nox.options.sessions = "lint"
locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.11"])
def lint(session: Session) -> None:
    """Lint using flake8."""
    args = session.posargs or locations
    session.install(
        "pyproject-flake8",
        "flake8-annotations",
        "flake8-black",
        "flake8-isort",
        "flake8-import-order",
        "flake8-docstrings",
    )
    session.run("pflake8", *args)


@nox.session(python="3.11")
def format(session: Session) -> None:
    """Run code formatter."""
    args = session.posargs or locations
    session.install("black", "isort")
    session.run("isort", *args)
    session.run("black", *args)
