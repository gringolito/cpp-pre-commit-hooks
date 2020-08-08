# cpp-pre-commit-hooks
Useful C++ hooks for pre-commit based on Google's C++ Style Guide

## Usage

To use these hooks, simply place the following snippet in you `.pre-commit-config.yaml`
(more details below):

```yaml
repos:
-   repo: https://github.com/gringolito/cpp-pre-commit-hooks
    rev: master
    hooks:
    -   id: check-using-namespace-directive
```

## check-using-namespace-directive

This hook verifies the usage of the `using namespace` directive according to the
[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html#Namespaces).

The argument `--allow-in-source` can be passed to this hook to provide a more
relaxed behavior and allow the usage of the `using namespace` directive in C++
source (`.c`, `.cc`, `.cpp`, and `.cxx`) files.

```yaml
-   repo: https://github.com/gringolito/cpp-pre-commit-hooks
    rev: master
    hooks:
    -   id: check-using-namespace-directive
    #   args: [--allow-in-source]
```
