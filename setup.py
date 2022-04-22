import setuptools

setuptools.setup(
    name="src",
    version="0.1.0",
    description="",
    python_requires=">=3.7",
    install_requires=[],
    extras_requires={"develop": ["pre-commit~=2.18.1", "pytest~=7.1.1"]},
)
