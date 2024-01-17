# pylint: disable = C0114
# pylint: disable = E0401

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChatbotAPI",
    version="2.5",
    author="HilFing",
    author_email="indradip.paul@outlook.com",
    description="Library to make AI chatbot with other additional utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hilfing/ChatbotAPI",
    project_urls={
        "Bug Tracker": "https://github.com/hilfing/ChatbotAPI/issues",
        "Wiki": "https://github.com/hilfing/ChatbotAPI/wiki/Python"
    },
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers'
        "Environment :: Console",
        "Natural Language :: English"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['requests', 'pyjokes', 'textblob'],
    python_requires='>=3',
)
