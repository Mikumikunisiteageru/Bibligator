# Bibligator

Bibligator is designed to merge PDF files named as `<s> <n>.pdf` or `<s> <n>-<m>.pdf` in the ascending order of `<n>`, where `<n>` and `<m>` are both natural numbers satisfying `n <= m`. These integer intervals suffixing the file names should be coherent.

本工具可合并名称形如 `<s> <n>.pdf` 或 `<s> <n>-<m>.pdf` 的 PDF 文件，其中 `<n>` 和 `<m>` 为自然数，满足 `n <= m`。这些在文件名中的整数区间需要相互衔接。PDF 文件将依 `<n>` 的顺序排列。

## Installation 安装

## Usage 使用说明

Bibligator can be directly run in command line, passing the path of one PDF file in the sequence as input.

本工具可直接在命令行中运行，接收一个参数，该参数为 PDF 文件序列中任一文件的路径。

```sh
bibligator [-h] FILENAME
```
