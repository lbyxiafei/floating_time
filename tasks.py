from invoke import task


@task
def clean(c):
    """Clean up temporary files."""
    c.run("rm -rf build dist")


@task
def build(c):
    """Build the project."""
    c.run("python setup.py sdist bdist_wheel")


@task
def test(c):
    """Run tests."""
    c.run("pytest")


@task
def lint(c):
    """Lint the code."""
    c.run("black .")


@task(pre=[lint, test])
def check(c):
    """Check the code quality and run tests."""
    pass


@task(pre=[clean, build])
def release(c):
    """Clean up, build, and release the project."""
    pass


@task
def run(c):
    c.run("python ./src/main.py")
