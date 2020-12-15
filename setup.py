import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="happy-AntoineHo",
    version="0.2.1",
    author="Antooine Houtain",
    author_email="antoine.houtain@gmail.com",
    description="Haploidy with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntoineHo/HapPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)