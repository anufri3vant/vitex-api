import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vitex-api", # Replace with your own username
    version="0.0.2",
    author="Anton Anufriev",
    author_email="anufri3vant@gmail.com",
    description="Vitex API Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antonanufriev/vitex-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)