from tkinter import ttk, constants, Message, IntVar, StringVar

class AfterLoginView:

    def __init__(self, root, ingredients, handle_after_login, handle_after_logout, username):
        self._root = root
        self._ingredients = ingredients
        self._handle_mark = handle_after_login
        self._handle_logout = handle_after_logout
        self._username = username

        self._frame = None
        self._label_var = None
        self._boxes = []

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_labels_and_frame(self):
        self._frame = ttk.Frame(master=self._root)

        label = Message(master=self._frame, text="You are logged in!")

        self._label_var = StringVar()

        if self._ingredients:
            text_label_text = "These ingredients will soon become waste.\nPlease eat them soon. :("
            self._label_var.set(text_label_text)
            text_label = ttk.Label(master=self._frame,
                                textvariable=self._label_var)
        else:
            text_label_text = "Good job!\nYou have no ingredients that will become waste! :)"
            self._label_var.set(text_label_text)
            text_label = ttk.Label(master=self._frame,
                                textvariable=self._label_var)
        return label, text_label

    def _create_mark_button(self):
        if self._ingredients:

            button = ttk.Button(
                master=self._frame,
                text="Mark as eaten",
                command=lambda:self._handle_mark(self._username, self._boxes)
            )
            return button

    def _create_logout_button(self):
        button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._handle_logout
        )
        return button

    def _initialize(self):
        label, text_label = self._create_labels_and_frame()

        label.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        text_label.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        i = 2
        for ingredient in self._ingredients:
            new_var = IntVar()
            new_check_button = ttk.Checkbutton(master=self._frame,
                                               text=ingredient, variable=new_var)
            new_check_button.grid(row=i, column=1,
                                  sticky=(constants.E, constants.W),
                                  padx=5, pady=5)
            self._boxes.append((new_var, ingredient))
            i+=1

        mark_button = self._create_mark_button()
        if mark_button:
            mark_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        logout_button = self._create_logout_button()
        logout_button.grid(column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
