import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BrainshopChatbotAPI",
    version="0.5.dev1",
    author="HilFing",
    author_email="indradip.paul@outlook.com",
    description="Brainshop API handler to make AI chatbot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hilfing/BrainshopChatbotAPI",
    project_urls={
        "Bug Tracker": "https://github.com/hilfing/BrainshopChatbotAPI/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	'Intended Audience :: Developers'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=['requests'],
    python_requires='>=3',
)