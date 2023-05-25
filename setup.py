import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DroneLIB",
    version="0.0.1",
    author="Ryan Rudd",
    author_email="ryan.ruddd@gmail.com",
    description="DroneLib is a Python library that leverages physics-based calculations to approximate the movement and predict the physics of bimotored RPAS, enabling accurate simulations and insights into drone dynamics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ryan-Rudd/DroneLIB",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

