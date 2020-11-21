from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='chaos_service',
    version='0.0.1',
    description='Chaos service',
    long_description=readme,
    author='Gustavo de Lima',
    author_email='gusdlim@gmail.com',
    url='https://github.com/glimsil/chaos-service',
    license=license,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    install_requires=["click"],
    entry_points={
        'console_scripts': [ 
        'chaos-service=chaos_service.main:cli' 
        ] 
    }
)