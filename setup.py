from setuptools import setup, find_packages

setup(
    name="sac_model",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "brian2",
        "seaborn"
    ],
    description="SAC Model for bipolar cells and starburst amacrine cells",
    author="Original authors + contributors"
) 