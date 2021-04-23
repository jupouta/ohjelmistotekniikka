from tkinter import ttk, constants, Message, IntVar

class AfterLoginView:

    def __init__(self, root, ingredients, handle_after_login, username):
        self._root = root
        self._ingredients = ingredients
        self._handle_mark = handle_after_login
        self._username = username
        self._frame = None

        self._boxes = []

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = Message(master=self._frame, text="You are logged in!")
        text_label = ttk.Label(master=self._frame,
                               text="These ingredients will soon become waste.\nPlease eat them soon. :(")

        label.grid(row=0, column=1, padx=5, pady=5)
        text_label.grid(row=1, column=1, padx=5, pady=5)

        i = 2
        for elem in self._ingredients:
            new_var = IntVar()
            new_check_button = ttk.Checkbutton(master=self._frame, text=elem, variable=new_var)
            new_check_button.grid(row=i, column=1, padx=5, pady=5)
            self._boxes.append(new_var)
            i+=1

        button = ttk.Button(
            master=self._frame,
            text="Mark as eaten",
            command=lambda:self._handle_mark(self._username, self._boxes)
        )
        button.grid(column=1)
        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
