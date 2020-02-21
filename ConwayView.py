import tkinter as tk
from Conway import *


def name(i, j):
    return "i" + str(i) + "j" + str(j)


class Application(tk.Frame):

    def __init__(self, n, master=None):
        self.keep_running = False
        if master is None:
            master = tk.Tk()
        super().__init__(master)
        self.n = n
        self.conway = ConwayGame(self.n)
        self.master = master
        self.pack()
        self.__create_widgets()
        self.create_rectangles()
        self.update_display()
        self.after(500, self.task())

    def task(self):
        """If keep_running is true, will increment by one time step every half second.
        Should only be called once.
        """
        self.after(500, self.task)
        if self.keep_running:
            self.time_step()

    def __create_widgets(self):
        """Creates the frame with the buttons and canvas to display."""
        # Frame to put in all the buttons
        self.top_frame = tk.Frame(self)
        self.top_frame.pack(side="top")
        # Time step button
        self.time_button = tk.Button(self.top_frame, text="Time Step", command=self.time_step)
        self.time_button.pack(side="left")
        # Start running
        self.start_button = tk.Button(self.top_frame, text="Start", command=self.start_running)
        self.start_button.pack(side="left")
        # Stop Running
        self.stop_button = tk.Button(self.top_frame, text="Stop", command=self.stop_running)
        self.stop_button.pack(side="left")
        # Restart Button
        self.restart_button = tk.Button(self.top_frame, text="Restart", command=self.restart)
        self.restart_button.pack(side="left")
        # Randomize button
        self.rand_button = tk.Button(self.top_frame, text="Randomize", command=self.randomize)
        self.rand_button.pack(side="left")
        # Create a quit button
        self.quit = tk.Button(self.top_frame, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="left")
        # Canvas where we draw the Conway Game
        canvas_width = 520
        canvas_height = 520
        self.w = tk.Canvas(self, width=canvas_width, height=canvas_height)
        self.w.bind("<Button-1>", self.clicked_canvas)
        self.w.pack()

    def create_rectangles(self):
        """Initializing the set of rectangles to display on the main canvas."""
        for i in range(self.n):
            for j in range(self.n):
                self.w.create_rectangle(10 + i * 10, 10 + j * 10, 20 + i * 10, 20 + j * 10,
                                        fill="#000000", tag=name(i, j))

    def randomize(self):
        """Creates a grid with random starting state. 50% of all rectangles will be alive."""
        self.conway.randomize()
        self.update_display()

    def restart(self):
        """Clears the current grid."""
        self.conway.zeros()
        self.update_display()

    def time_step(self):
        """Tells the grid to proceed one time step."""
        self.conway.next_conway()
        self.update_display()

    def start_running(self):
        """Tells the game to start autoupdating."""
        self.keep_running = True

    def stop_running(self):
        """Tells the game to stop autoupdating."""
        self.keep_running = False

    def update_display(self):
        """Reads from the current grid and updates the display according to the current state."""
        for x in self.conway:
            if x[2] == 0:
                color = "#ffffff"
            else:
                color = "#000000"
            self.w.itemconfig(name(x[0], x[1]), fill=color)

    def clicked_canvas(self, event):
        """Switches the state of the grid at the mouse pointer."""
        row = (event.x - 10) // 10
        col = (event.y - 10) // 10
        self.conway.flip_square(row, col)
        self.update_display()


app = Application(50)
app.mainloop()
