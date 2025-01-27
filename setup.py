from setuptools import setup, find_packages

setup(
    name="TaskPackage_",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Hani Tustanto",
    author_email="hanitustanto11@gmail.com.com",
    description="Contoh package untuk tugas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HanTanto/TaskPackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

