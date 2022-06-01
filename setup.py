import GPUtil
from distutils.core import setup

setup(
      name='GPUtil',
      packages=['GPUtil'],
      version=GPUtil.__version__,
      description = 'GPUtil is a Python module for getting the GPU status from NVIDA GPUs using nvidia-smi.',
      long_description=open("README.md", "r", errors="ignore").read(),
      long_description_content_type="text/markdown",
      author='Romanin',
      author_email='semina054@gmail.com',
      url='https://github.com/romanin-rf/GPUtils.py',
      keywords=['gpu','utilization','load','memory','available','usage','free','select','nvidia'],
      classifiers=[],
      license='MIT'
)
