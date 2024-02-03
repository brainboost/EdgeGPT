from pathlib import Path

from setuptools import find_packages, setup

DOCS_PATH = Path(__file__).parents[0] / "docs/README.md"
PATH = Path("README.md")
if not PATH.exists():
    with Path.open(DOCS_PATH, encoding="utf-8") as f1:
        with Path.open(PATH, "w+", encoding="utf-8") as f2:
            f2.write(f1.read())

setup(
    name="EdgeGPT-plus",
    version="0.13.4",
    license="The Unlicense",
    author="Antonio Cheong + others",
    author_email="acheong@student.dalat.org",
    description="Reverse engineered Edge Chat API",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/brainboost/EdgeGPT",
    project_urls={"Bug Report": "https://github.com/brainboost/EdgeGPT/issues/new"},
    entry_points={
        "console_scripts": [
            "edge-gpt = EdgeGPT.main:main",
            "edge-gpt-image = EdgeGPT.ImageGen:main",
        ],
    },
    install_requires=[
        "httpx[socks]>=0.24.0",
        "aiohttp",
        "websockets",
        "rich",
        "certifi",
        "prompt_toolkit",
        "requests",
        "BingImageCreator>=0.4.4",
    ],
    long_description=Path.open(PATH, encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["EdgeGPT", "EdgeUtils", "ImageGen"],
    classifiers=[
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
