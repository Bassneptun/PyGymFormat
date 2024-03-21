from setuptools import setup, find_packages

setup(
    name="PyGymFormat",
    version="0.0.1",
    packages=find_packages(),
    license="MIT",
    description="Base classes for making games that comply with Openai Gym enviroment creation standards",
    long_description=open("README.md").read(),
    install_requires=["pygame", "numpy", "vectormath"],
    author="Jeremy Neumann",
    author_email="jeremytaylorneumann@gmail.com"
)