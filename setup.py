import setuptools
import os, sys, shutil

if sys.argv[-1] == "publish":
    here = os.path.abspath(os.path.dirname(__file__))
    shutil.rmtree(os.path.join(here, "dist"))
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload --repository pypi dist/*')
    sys.exit()

with open("README.md", "r") as readme_file:
    github_readme = readme_file.read()

setuptools.setup(
    name="jsmethods",
    version="1.0.0",
    author="Theodike",
    author_email="gvedichi@gmail.com",
    description="Implementing standard JavaScript iterable objects methods for python iterable objects",
    keywords=["chaining", "list methods", "array methods", "js", "javascript"],
    long_description=github_readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Theodikes/jsmethods",
    install_requires=[],
    test_require=["pytest"],
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
