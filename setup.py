from setuptools import setup, find_packages

setup(name='rlkit',
      packages=find_packages(),
      version='0.0.1',
      install_requires=['cloudpickle', 'gym[all]', 'gitpython', 'gtimer', 'pygame', 'mujoco-py', 'opencv-python', 'python-dateutil', 'joblib'])
