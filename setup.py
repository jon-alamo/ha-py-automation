import setuptools

install_requires = [
    'requests',
    'websocket-client',
    'watchdog',
    'zha-quirks',
    'pydantic-settings',
    'pytz',
    'python-dateutil'
]


setuptools.setup(
    name='hapy',
    version='0.1',
    author="jon-alamo",
    author_email="jonrivala@gmail.com",
    description="Home Assistant (Pure)Python Automation Tool",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'hapy-start = hapy.commands:start_project',
        ],
    },
)
