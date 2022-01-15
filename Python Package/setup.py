import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChatbotAPI",
    version="2.0.0",
    author="HilFing",
    author_email="indradip.paul@outlook.com",
    description="Lib to make AI chatbot with other additional utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hilfing/ChatbotAPI",
    project_urls={
        "Bug Tracker": "https://github.com/hilfing/ChatbotAPI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	'Intended Audience :: Developers'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['requests','pyjokes','wikipedia','textblob'],
    python_requires='>=3',
)
