from tkinter import ttk, constants

class AfterLoginView:

    def __init__(self, root, ingredients, handle_after_login):
        self._root = root
        self._ingredients = ingredients
        self._handle_hello = handle_after_login
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="You are logged in!")
        text_label = ttk.Label(master=self._frame,
                               text="These ingredients will soon become waste.\nPlease eat them soon. :(")

        label.grid(row=0, column=0)
        text_label.grid(row=1, column=0)

        i = 2
        for elem in self._ingredients:
            new_label = ttk.Label(master=self._frame, text=elem)
            new_label.grid(row=i, column=0)

        # button = ttk.Button(
        #     master=self._frame,
        #     text="Say hello",
        #     command=self._handle_hello
        # )

        #button.grid(row=1, column=0)