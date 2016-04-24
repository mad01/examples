from pip.req import parse_requirements
from setuptools import find_packages
from setuptools import setup
from subprocess import call
from setuptools.command.install import install as _install


install_requirements = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_requirements]


class install(_install):

    def __post_install(self, dir):
        call(['./auto_compleate_install.sh'])

    def run(self):
        _install.run(self)
        self.execute(
            self.__post_install,
            (self.install_lib,),
            msg="installing auto completion"
            )


setup(
    name='ecli',
    version='0.1a2',
    author=u'example',
    author_email='foo@example.com',
    description='Some description',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'ecli=ecli_lib.main:ecli',
        ]},
    cmdclass={'install': install},
    )
