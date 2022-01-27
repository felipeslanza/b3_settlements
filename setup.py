import setuptools


setuptools.setup(
    name="b3_setttements",
    version="0.01",
    author="fsl",
    author_email="felipeslanza@gmail.com",
    description="Retrieve futures' settlement data from B3 exchange",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/felipeslanza/b3_settlements",
    packages=setuptools.find_packages(),
    install_requires=[
        "bs4",
        "lxml",
        "html5lib",
        "pandas",
        "requests",
    ],
    python_requires=">=3.8",
)
