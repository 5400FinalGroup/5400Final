import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='matcher',
    version='0.0.1',
    author='5400Group',
    author_email='jp2132@georgetown.edu',
    description='A package to analyze toxicity.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "autopep8"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
