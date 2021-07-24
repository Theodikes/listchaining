import setuptools

with open("README.md", "r") as readme_file:
    github_readme = readme_file.read()

setuptools.setup(
    name="jsmethods",
    version="1.0.0",
    author="Theodike",
    author_email="gvedichi@gmail.com",
    description="Implementing standard JavaScript iterable objects methods for python iterable objects",
    long_description=github_readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Theodikes/jsmethods",
    install_requires=[],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)