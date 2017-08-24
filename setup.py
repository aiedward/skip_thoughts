from distutils.core import setup

setup(name='Tensorflow Skipthoughts',
      version='1.0',
      description='This is a TensorFlow implementation of the model described in: Jamie Ryan Kiros, Yukun Zhu, Ruslan Salakhutdinov, Richard S. Zemel, Antonio Torralba, Raquel Urtasun, Sanja Fidler. Skip-Thought Vectors. In NIPS, 2015.',
      packages=['skip_thoughts',],
      install_requires=[
          'gensim',
          'tensorflow',
          'nltk',
          'scikit-learn',
      ])
