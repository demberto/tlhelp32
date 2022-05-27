# Installation

## Via `pip` from PyPi:

```
pip install tlhelp32
```

## Via Github:

1.  Clone the repo:

    ```
    git clone https://github.com/demberto/tlhelp32
    ```

2.  Navigate to the newly created directory.

    ```
    cd tlhelp32
    ```

3.  Install via `pip` in either:

    - Development mode (editable install):

      ```
      pip install -e tlhelp32
      ```

      *I would prefer using a virtualenv if I were using this for development.*

    *OR*

    - Install mode:

      ```
      pip install .
      ```

      *Almost similar to directly installing it with pip from PyPi, except you
      get the latest changes first, provided you keep your local copy synced.*

## Via Github Releases

1.  Go to [Releases](https://github.com/demberto/tlhelp32/releases) section
2.  Download the **.whl** (wheel / build distribution) or the **.tar.gz**
    (source tarball) from your preferred version.
3.  In the directory where you download them, run:

    ```
    pip install tlhelp32-0.1.0-py3-none-any.whl
    ```
