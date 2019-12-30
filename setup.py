from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf8') as fp:
    long_description = fp.read()

with open('requirements.txt', "r", encoding='utf8') as f:
    install_requires = [l for l in f if l.strip() and not l.strip().startswith('#')]

setup(
    name="dingapi",
    version="0.0.5",
    keywords='dingding, ding, dtalk, dingtalk, sdk, api',
    author="hongjinpin",
    author_email="hongjinpin@qq.com",
    url="https://github.com/hongjinpin/dingapi",
    description="lightweight dingtalk api for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
