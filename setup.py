import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="the-true",
    version="0.0.4",
    author="Chisa Yomoda",
    author_email="mengele@schutzstaffel.agency",
    description="The True",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/h4n1virus/the-true",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
