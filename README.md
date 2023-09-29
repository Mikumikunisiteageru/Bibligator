# Bibligator

Bibligator is designed to merge PDF files named as `<s> <n>.pdf` or `<s> <n>-<m>.pdf` in the ascending order of `<n>`, where `<n>` and `<m>` are both natural numbers satisfying `n <= m`. These integer intervals suffixing the file names should be coherent.

本工具可合并名称形如 `<s> <n>.pdf` 或 `<s> <n>-<m>.pdf` 的 PDF 文件，其中 `<n>` 和 `<m>` 为自然数，满足 `n <= m`。这些在文件名中的整数区间须相互衔接。PDF 文件将依 `<n>` 的顺序排列。

## Installation 安装

At the root directory of this project run `python setup.py bdist_wheel` in command line, and a wheel file `bibligator-<...>.whl` will be generated under the `dist` subdirectory. Then, this package can be installed into Python by running `pip install dist/bibligator-<...>.whl`.

在命令行中定位到本项目的根目录，运行 `python setup.py bdist_wheel`，便应产生子目录 `dist` 及其下的 wheel 文件 `bibligator-<...>.whl`。再运行 `pip install dist/bibligator-<...>.whl`，便可安装此 Python 程序包。

The wheel file may also be found as a release in this repository.

在本仓库的 Releases 栏中也可找到能直接安装的 wheel 文件。

## Usage 使用说明

Bibligator can be directly run in command line, passing the path of one PDF file in the sequence as input.

本工具可直接在命令行中运行，接收一个参数，该参数为 PDF 序列中任一文件的路径。

```sh
bibligator [-h] FILENAME
```
