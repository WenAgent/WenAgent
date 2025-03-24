from setuptools import setup, find_packages

setup(
    name="wen-agent",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["openai==0.27.0"],
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered agent for Chinese culture insights",
    license="MIT",
    url="https://github.com/yourusername/wen-agent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
