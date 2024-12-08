from setuptools import setup, find_packages
setup(
    name='MMsuit',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'dash',
        'scipy',
        'plotly',
    ],
    entry_points={
        "console_scripts": [
            "MMsuit=MMsuit:MMsuit",  # Update this if you want to provide a CLI
        ],
    }
)