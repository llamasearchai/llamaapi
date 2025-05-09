from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llamaapi-llamasearch",
    version="0.1.0",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    description="A flexible API client and server utilities package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://llamasearch.ai",
    project_urls={
        "Bug Tracker": "https://github.com/llamasearch/llamaapi/issues",
        "Documentation": "https://llamasearch.ai/docs/llamaapi",
        "Source Code": "https://github.com/llamasearch/llamaapi",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
        "pydantic>=1.9.0",
        "PyYAML>=6.0",
        "redis>=4.3.4",
        "ujson>=5.4.0",
        "httpx>=0.23.0",
        "marshmallow>=3.17.0",
        "openapi-spec-validator>=0.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.6.0",
            "isort>=5.10.1",
            "mypy>=0.971",
            "flake8>=5.0.4",
        ],
        "server": [
            "flask>=2.2.0",
            "fastapi>=0.85.0",
            "uvicorn>=0.18.3",
        ],
        "auth": [
            "pyjwt>=2.4.0",
            "cryptography>=37.0.4",
        ],
        "cache": [
            "cachetools>=5.2.0",
        ],
        "docs": [
            "mkdocs>=1.4.0",
            "mkdocs-material>=8.5.0",
            "mkdocstrings>=0.19.0",
        ],
    },
) 
# Updated in commit 5 - 2025-04-04 17:21:13

# Updated in commit 13 - 2025-04-04 17:21:14

# Updated in commit 21 - 2025-04-04 17:21:16

# Updated in commit 29 - 2025-04-04 17:21:17

# Updated in commit 5 - 2025-04-05 14:30:37

# Updated in commit 13 - 2025-04-05 14:30:38

# Updated in commit 21 - 2025-04-05 14:30:38

# Updated in commit 29 - 2025-04-05 14:30:38

# Updated in commit 5 - 2025-04-05 15:17:05

# Updated in commit 13 - 2025-04-05 15:17:05

# Updated in commit 21 - 2025-04-05 15:17:05

# Updated in commit 29 - 2025-04-05 15:17:05

# Updated in commit 5 - 2025-04-05 15:47:50

# Updated in commit 13 - 2025-04-05 15:47:50

# Updated in commit 21 - 2025-04-05 15:47:50

# Updated in commit 29 - 2025-04-05 15:47:50

# Updated in commit 5 - 2025-04-05 16:52:52

# Updated in commit 13 - 2025-04-05 16:52:52

# Updated in commit 21 - 2025-04-05 16:52:52

# Updated in commit 29 - 2025-04-05 16:52:52

# Updated in commit 5 - 2025-04-05 17:24:50

# Updated in commit 13 - 2025-04-05 17:24:50

# Updated in commit 21 - 2025-04-05 17:24:51

# Updated in commit 29 - 2025-04-05 17:24:51

# Updated in commit 5 - 2025-04-05 18:11:58

# Updated in commit 13 - 2025-04-05 18:11:58

# Updated in commit 21 - 2025-04-05 18:11:58

# Updated in commit 29 - 2025-04-05 18:11:58

# Updated in commit 5 - 2025-04-05 18:36:00

# Updated in commit 13 - 2025-04-05 18:36:00

# Updated in commit 21 - 2025-04-05 18:36:01

# Updated in commit 29 - 2025-04-05 18:36:01
