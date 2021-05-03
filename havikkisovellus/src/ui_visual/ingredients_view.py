from tkinter import ttk, constants, Message, IntVar, StringVar

class IngredientsView:

    def __init__(self, root, ingredients, handle_mark):
        self._root = root
        self._ingredients = ingredients
        self._handle_mark = handle_mark

        self._frame = None
        self._label_var = None

        self._boxes = []

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _create_mark_button(self):
        if self._ingredients:
            button = ttk.Button(
                master=self._frame,
                text="Mark as eaten",
                command=lambda:self._handle_mark(self._boxes)
            )
            return button
        return None

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

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
        text_label.grid(row=0, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        i = 1
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
