from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pymvvm_design",
    version="0.6.0",
    author="shinoj cm",
    author_email="shinojcm01@gmail.com",
    description="A simplified MVVM framework for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fridayowl/PyMVVM",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        # Add any dependencies here
    ],
)