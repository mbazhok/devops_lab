from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    scripts=["snapshot"],
    version="0.1",
    author="Maksim Bazhok",
    author_email="custom@gmail.com",
    description="This app creates snapshots.",
    license="MIT"
)
