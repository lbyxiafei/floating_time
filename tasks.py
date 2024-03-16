from invoke import task


@task
def run(c):
    c.run("python ./src/main.py")


@task
def clean(c):
    """Clean up temporary files."""
    c.run("rm -rf build dist")
    c.run("git clean -xdf")


@task
def build(c):
    """Build the project."""
    c.run("python -m build")


@task(pre=[clean, build])
def release(c):
    """Clean up, build, and release the project."""
    c.run("twine upload dist/*")


@task
def test(c):
    """Run tests."""
    c.run("pytest")


@task
def lint(c):
    """Lint the code."""
    c.run("black .")
    c.run("flake8 .")


@task(pre=[lint, test])
def check(c):
    """Check the code quality and run tests."""
    pass
