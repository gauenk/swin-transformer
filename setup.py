from setuptools import setup, find_packages
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(name='swin',
      package_dir={"": "lib"},
      packages=find_packages("."),
      package_data={'': ['*.so']},
      include_package_data=True,
      ext_modules=[
          CUDAExtension('swin_cuda', [
              'lib/csrc/swin_window_process_kernel.cpp',
              'lib/csrc/swin_window_process_kernel.cu',
          ],
          )
      ],
      cmdclass={'build_ext': BuildExtension},
)

