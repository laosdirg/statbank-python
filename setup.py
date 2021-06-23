import setuptools 

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="statbank",
    version="1.0.1",
    license="MIT",
    author="Bytes & Brains",
    author_email="developers@bytesandbrains.com",
    description="Statbank API client library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bytesandbrains/statbank-python",
    packages=setuptools.find_packages(),
    install_requires=[
        "python-dateutil",
    ],
    test_suite="tests",
)
