from distutils.core import setup

setup(
    # Application name:
    name="SuperUtilities",

    # Version number:
    version="0.1.1",

    # Application author details:
    author="EnvyingGolem47",
    author_email="envyinggolem47@projectnightfall.net",

    # Packages
    packages=["super_utilities"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/EnvyingGolem47/SuperUtilities-Python3",

    #
    # license="LICENSE.txt",
    description="All Rights Reserved",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)