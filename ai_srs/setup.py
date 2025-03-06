from setuptools import setup, find_packages

setup(
    name="ai_srs",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "python-dotenv",
        "pydantic"
    ],
)
