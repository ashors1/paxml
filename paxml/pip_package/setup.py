# coding=utf-8
# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup.py file for paxml."""

from setuptools import setup, find_namespace_packages

setup(
    name='paxml',
    version='0.1.0', # use major/minor version number, e.g. "0.1.0"
    description=('Framework to configure and run machine learning experiments '
                 'on top of Jax.'),
    author='PAX team',
    author_email='pax-dev@google.com',
    packages=find_namespace_packages(include=['paxml*']),
    python_requires='>=3.7',
    install_requires=[
        'praxis', 'pyglove', 'absl-py', 'jax', 'tensorflow==2.7.3',
        'tensorflow-text==2.7.3', 'numpy', 'flax',
        'clu', 'lingvo', 't5', 'seqio-nightly', 'tensorstore',
        'etils', 'orbax'
    ],
    url='https://github.com/google/paxml',
    license='Apache-2.0',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False,
)
