from setuptools import setup, find_packages

setup(
    name="signalkit",
    version="0.1.0",
    description="Ground Water Quality Toolkit - Tools and skills for analyzing groundwater quality and characterizing contamination zones",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Water Authority",
    author_email="haimk@water.gov.il",
    url="https://github.com/haimk-max/ground-water-quality-toolkit",
    packages=find_packages(where="pylib"),
    package_dir={"": "pylib"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19",
        "scipy>=1.5",
        "pandas>=1.0",
    ],
    extras_require={
        "dev": ["pytest>=6.0", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "signalkit-trend=signalkit.trend_analysis:main",
            "signalkit-severity=signalkit.severity_calculator:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
)
