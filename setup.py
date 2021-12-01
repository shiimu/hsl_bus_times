from setuptools import setup

setup(
    name="hsl_bus_times",
    version="1.0",
    description="",
    keywords="",
    author="",
    packages=["hsl_bus_times"],
    entry_points={"console_scripts": ["hsl_bus_times=hsl_bus_times.main:main"]},
    include_package_data=True,
    zip_safe=False
    )