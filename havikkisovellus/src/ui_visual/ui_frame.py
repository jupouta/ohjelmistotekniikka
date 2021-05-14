"""Inheritance class for repeating frame functions."""
from tkinter import constants

class UIFrame:
    """Class for inheritable functions in the UI.

    Attributes:
        frame: The frame in the view to be modified."""

    def __init__(self, frame):
        """Class instructor.
        Args:
            frame: The frame in the view to be modified."""
        self._frame = frame

    def pack(self):
        """Fill the frame with elements."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroy and delete all the elements in the frame."""
        self._frame.destroy()
