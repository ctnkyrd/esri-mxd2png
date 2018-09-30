import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mxd2jpg",
    version="1.0.1",
    author="Arda Cetinkaya",
    author_email="ardacetinkaya@windowslive.com",
    description="Esri's export to jpg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ctnkyrd/esri-mxd2png",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)