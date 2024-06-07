from setuptools import setup

setup(
      name='falcon_lander_gym',
      version='0.1',
      url='https://github.com/Chathura-Ranasinghe/Falcon9-Lander-Gym',
      author='Chathura Ranasinghe',
      author_email='chathurar.99.bc@gmail.com',
      packages=['falcon_lander_gym', 'falcon_lander_gym.envs'],
      install_requires=[
            'gym',
            'box2d-py',
            'numpy',
      ],
      include_package_data=True,
      description='Custom Gym environment for Falcon 9 rocket landing simulation'
)