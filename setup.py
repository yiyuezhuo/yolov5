import setuptools

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="yolov5",
    version="0.0.0",
    install_requires=install_requires,
    packages=setuptools.find_packages(),
)
