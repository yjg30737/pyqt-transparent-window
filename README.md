# pyqt-transparent-window
PyQt transparent window

## Requirements
PyQt5>=5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-transparent-window.git --upgrade```

## Included Package
* <a href="https://github.com/yjg30737/pyqt-resize-frame.git">pyqt-resize-frame</a>

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    app.exec_()
```

Result

Transparent window except for border (white).

![image](https://user-images.githubusercontent.com/55078043/147629109-5025fd5c-ec38-46e2-895d-a0d55bb8c10f.png)

Resize frame (blue)

![image](https://user-images.githubusercontent.com/55078043/147629222-4fbc7e4b-1d68-46d8-8b02-4f06945ddb1d.png)

This is Windows screenshot feature so mouse cursor cannot be seen. At least cursor reshaping works like a charm so far.

## Note
It can be expanded or shrinked only right or bottom direction.

Technically I can make that happen top or left direction as well but it makes window jitter.

This is not movable.

One more thing, When something interrupt the focus of this windows(pressing Windows+R button for examples), Resize frame's function will be broken miserably. So i do have to get rid of that malfunction.



