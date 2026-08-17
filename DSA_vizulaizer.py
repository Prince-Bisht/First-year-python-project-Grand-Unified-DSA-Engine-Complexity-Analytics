import tkinter as tk
from tkinter import ttk, messagebox
import math
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np


# ================================================================
# CORE DATA-STRUCTURE ENGINES
# ================================================================

class HashTableEngine:
    def __init__(self, size=5):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def insert(self, key, value):
        index = key % self.size
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])


class BSTEngine:
    def __init__(self):
        self.structure = {}

    def insert(self, value):
        if not self.structure:
            self.structure[value] = {"left": None, "right": None}
            return

        current = next(iter(self.structure))
        while True:
            if value < current:
                if self.structure[current]["left"] is None:
                    self.structure[current]["left"] = value
                    self.structure[value] = {"left": None, "right": None}
                    return
                current = self.structure[current]["left"]
            elif value > current:
                if self.structure[current]["right"] is None:
                    self.structure[current]["right"] = value
                    self.structure[value] = {"left": None, "right": None}
                    return
                current = self.structure[current]["right"]
            else:
                return


class GraphEngine:
    def __init__(self):
        self.matrix = {
            "A": ["B", "C"],
            "B": ["A", "D"],
            "C": ["A", "D"],
            "D": ["B", "C"],
        }

    def add_edge(self, u, v):
        self.matrix.setdefault(u, [])
        self.matrix.setdefault(v, [])

        if v not in self.matrix[u]:
            self.matrix[u].append(v)
        if u not in self.matrix[v]:
            self.matrix[v].append(u)


# ================================================================
# MAIN APPLICATION
# ================================================================

class DSAVisualizer:
    BG = "#0B1220"
    SURFACE = "#111827"
    CARD = "#172033"
    BORDER = "#263247"
    TEXT = "#E5E7EB"
    MUTED = "#94A3B8"
    BLUE = "#38BDF8"
    GREEN = "#34D399"
    PINK = "#F472B6"
    AMBER = "#FBBF24"
    RED = "#FB7185"
    PURPLE = "#A78BFA"

    def __init__(self, root):
        self.root = root
        self.root.title("DSA Studio | Interactive Data Structure Visualizer")
        self.root.geometry("1240x820")
        self.root.minsize(1050, 700)
        self.root.configure(bg=self.BG)

        # Existing data structures are intentionally preserved.
        self.array_data = [23, 45, 12, 67, 89]
        self.linked_list = [10, 20, 30]
        self.stack = [15, 30]
        self.queue = [11, 22]
        self.hash_table = HashTableEngine()
        self.bst = BSTEngine()
        self.graph = GraphEngine()

        for value in [45, 23, 65]:
            self.bst.insert(value)
        self.hash_table.insert(12, "DataA")
        self.hash_table.insert(17, "CollisionB")

        self._configure_styles()
        self._build_shell()

    # ------------------------------------------------------------
    # UI FOUNDATION
    # ------------------------------------------------------------

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background=self.BG, borderwidth=0)
        style.configure(
            "TNotebook.Tab",
            background=self.SURFACE,
            foreground=self.MUTED,
            padding=(15, 9),
            font=("Segoe UI", 9, "bold"),
            borderwidth=0,
        )
        style.map(
            "TNotebook.Tab",
            background=[("selected", self.BLUE)],
            foreground=[("selected", self.BG)],
        )

    def _build_shell(self):
        header = tk.Frame(self.root, bg=self.SURFACE, height=78)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="DSA STUDIO",
            font=("Segoe UI", 18, "bold"),
            fg=self.TEXT,
            bg=self.SURFACE,
        ).pack(side="left", padx=(24, 8), pady=20)

        tk.Label(
            header,
            text="Interactive structures • live analytics • algorithm reference",
            font=("Segoe UI", 9),
            fg=self.MUTED,
            bg=self.SURFACE,
        ).pack(side="left", pady=24)

        tk.Label(
            header,
            text="PROJECT READY",
            font=("Segoe UI", 8, "bold"),
            fg=self.BG,
            bg=self.GREEN,
            padx=10,
            pady=5,
        ).pack(side="right", padx=24)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=16, pady=16)

        self.tab_linear = tk.Frame(notebook, bg=self.SURFACE)
        self.tab_tree = tk.Frame(notebook, bg=self.SURFACE)
        self.tab_net = tk.Frame(notebook, bg=self.SURFACE)
        self.tab_analytics = tk.Frame(notebook, bg=self.SURFACE)
        self.tab_algo = tk.Frame(notebook, bg=self.SURFACE)

        notebook.add(self.tab_linear, text="  Linear Structures  ")
        notebook.add(self.tab_tree, text="  BST & Hash Table  ")
        notebook.add(self.tab_net, text="  Graph  ")
        notebook.add(self.tab_analytics, text="  Analytics  ")
        notebook.add(self.tab_algo, text="  Algorithm & Flow  ")

        self._init_linear_structures()
        self._init_tree_hash_structures()
        self._init_graph_structures()
        self._init_analytics()
        self._init_algorithm_flow()

    def _section_title(self, parent, title, subtitle):
        block = tk.Frame(parent, bg=self.SURFACE)
        block.pack(fill="x", padx=18, pady=(16, 8))
        tk.Label(block, text=title, font=("Segoe UI", 14, "bold"), fg=self.TEXT, bg=self.SURFACE).pack(anchor="w")
        tk.Label(block, text=subtitle, font=("Segoe UI", 9), fg=self.MUTED, bg=self.SURFACE).pack(anchor="w", pady=(2, 0))

    def _entry(self, parent, width=8, default=""):
        entry = tk.Entry(
            parent,
            width=width,
            bg=self.BG,
            fg=self.TEXT,
            insertbackground=self.TEXT,
            relief="flat",
            highlightthickness=1,
            highlightbackground=self.BORDER,
            highlightcolor=self.BLUE,
            font=("Segoe UI", 10),
        )
        entry.insert(0, default)
        return entry

    def _button(self, parent, text, command, color=None):
        return tk.Button(
            parent,
            text=text,
            command=command,
            bg=color or self.BLUE,
            fg=self.BG,
            activebackground=color or self.BLUE,
            activeforeground=self.BG,
            relief="flat",
            bd=0,
            padx=12,
            pady=7,
            cursor="hand2",
            font=("Segoe UI", 9, "bold"),
        )

    def _read_int(self, entry, label="value"):
        try:
            return int(entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", f"Please enter a valid integer for {label}.")
            return None

    # ------------------------------------------------------------
    # LINEAR STRUCTURES
    # ------------------------------------------------------------

    def _init_linear_structures(self):
        self._section_title(
            self.tab_linear,
            "Linear Data Structures",
            "Interact with the original array, linked list, stack and queue datasets.",
        )

        controls = tk.Frame(self.tab_linear, bg=self.CARD, padx=14, pady=12)
        controls.pack(fill="x", padx=18, pady=(0, 10))

        tk.Label(controls, text="Value", fg=self.MUTED, bg=self.CARD, font=("Segoe UI", 9, "bold")).pack(side="left")
        self.lin_input = self._entry(controls, width=8, default="50")
        self.lin_input.pack(side="left", padx=(8, 14))

        for text, command, color in [
            ("Push Stack", self._stack_push, self.PINK),
            ("Pop Stack", self._stack_pop, self.RED),
            ("Enqueue", self._queue_enqueue, self.AMBER),
            ("Dequeue", self._queue_dequeue, self.AMBER),
            ("Insert Linked List", self._linked_list_insert, self.PURPLE),
        ]:
            self._button(controls, text, command, color).pack(side="left", padx=4)

        self.linear_canvas = tk.Canvas(self.tab_linear, bg=self.BG, highlightthickness=0)
        self.linear_canvas.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        self._draw_linear()

    def _draw_linear(self):
        c = self.linear_canvas
        c.delete("all")

        c.create_text(54, 32, anchor="w", text="ARRAY", fill=self.BLUE, font=("Segoe UI", 10, "bold"))
        x = 54
        for index, value in enumerate(self.array_data):
            c.create_rectangle(x, 54, x + 62, 96, fill=self.BLUE, outline=self.BLUE)
            c.create_text(x + 31, 75, text=str(value), fill=self.BG, font=("Segoe UI", 10, "bold"))
            c.create_text(x + 31, 112, text=f"[{index}]", fill=self.MUTED, font=("Consolas", 8))
            x += 72

        c.create_text(54, 160, anchor="w", text="LINKED LIST", fill=self.PURPLE, font=("Segoe UI", 10, "bold"))
        x = 54
        for index, value in enumerate(self.linked_list):
            c.create_rectangle(x, 182, x + 74, 220, fill=self.PURPLE, outline=self.PURPLE)
            c.create_text(x + 37, 201, text=str(value), fill=self.TEXT, font=("Segoe UI", 9, "bold"))
            if index < len(self.linked_list) - 1:
                c.create_line(x + 74, 201, x + 108, 201, fill=self.GREEN, width=2, arrow=tk.LAST)
            else:
                c.create_text(x + 96, 201, text="NULL", fill=self.RED, font=("Segoe UI", 8, "bold"))
            x += 112

        c.create_text(590, 160, anchor="w", text="STACK • LIFO", fill=self.PINK, font=("Segoe UI", 10, "bold"))
        c.create_line(590, 195, 590, 355, fill=self.BORDER, width=2)
        c.create_line(700, 195, 700, 355, fill=self.BORDER, width=2)
        c.create_line(590, 355, 700, 355, fill=self.BORDER, width=2)
        y = 322
        for index, value in enumerate(self.stack):
            c.create_rectangle(596, y, 694, y + 27, fill=self.PINK, outline=self.PINK)
            c.create_text(645, y + 13, text=str(value), fill=self.TEXT, font=("Segoe UI", 9, "bold"))
            if index == len(self.stack) - 1:
                c.create_text(720, y + 13, anchor="w", text="TOP", fill=self.PINK, font=("Segoe UI", 8, "bold"))
            y -= 32

        c.create_text(54, 286, anchor="w", text="QUEUE • FIFO", fill=self.AMBER, font=("Segoe UI", 10, "bold"))
        c.create_line(54, 318, 470, 318, fill=self.BORDER, width=2)
        c.create_line(54, 370, 470, 370, fill=self.BORDER, width=2)
        x = 72
        for index, value in enumerate(self.queue):
            c.create_rectangle(x, 324, x + 54, 364, fill=self.AMBER, outline=self.AMBER)
            c.create_text(x + 27, 344, text=str(value), fill=self.BG, font=("Segoe UI", 9, "bold"))
            if index == 0:
                c.create_text(x + 27, 306, text="FRONT", fill=self.RED, font=("Segoe UI", 8, "bold"))
            if index == len(self.queue) - 1:
                c.create_text(x + 27, 386, text="REAR", fill=self.GREEN, font=("Segoe UI", 8, "bold"))
            x += 66

    def _stack_push(self):
        value = self._read_int(self.lin_input)
        if value is not None:
            self.stack.append(value)
            self._draw_linear()
            self._refresh_analytics_if_ready()

    def _stack_pop(self):
        if self.stack:
            self.stack.pop()
            self._draw_linear()
            self._refresh_analytics_if_ready()

    def _queue_enqueue(self):
        value = self._read_int(self.lin_input)
        if value is not None:
            self.queue.append(value)
            self._draw_linear()
            self._refresh_analytics_if_ready()

    def _queue_dequeue(self):
        if self.queue:
            self.queue.pop(0)
            self._draw_linear()
            self._refresh_analytics_if_ready()

    def _linked_list_insert(self):
        value = self._read_int(self.lin_input)
        if value is not None:
            self.linked_list.append(value)
            self._draw_linear()
            self._refresh_analytics_if_ready()

    # ------------------------------------------------------------
    # BST + HASH TABLE
    # ------------------------------------------------------------

    def _init_tree_hash_structures(self):
        self._section_title(
            self.tab_tree,
            "Tree & Hash Structures",
            "Visualize BST insertion and chained hash-table collisions.",
        )

        controls = tk.Frame(self.tab_tree, bg=self.CARD, padx=14, pady=12)
        controls.pack(fill="x", padx=18, pady=(0, 10))
        tk.Label(controls, text="Integer key", fg=self.MUTED, bg=self.CARD, font=("Segoe UI", 9, "bold")).pack(side="left")
        self.tree_key = self._entry(controls, width=8, default="30")
        self.tree_key.pack(side="left", padx=(8, 14))
        self._button(controls, "Insert into BST", self._bst_add, self.PINK).pack(side="left", padx=4)
        self._button(controls, "Insert into Hash", self._hash_add, self.BLUE).pack(side="left", padx=4)

        self.tree_canvas = tk.Canvas(self.tab_tree, bg=self.BG, highlightthickness=0)
        self.tree_canvas.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        self._draw_tree_hash()

    def _draw_tree_hash(self):
        c = self.tree_canvas
        c.delete("all")
        c.create_text(55, 30, anchor="w", text="BINARY SEARCH TREE", fill=self.PINK, font=("Segoe UI", 10, "bold"))
        c.create_text(650, 30, anchor="w", text="HASH TABLE • SEPARATE CHAINING", fill=self.BLUE, font=("Segoe UI", 10, "bold"))

        if self.bst.structure:
            root = next(iter(self.bst.structure))
            self._plot_bst(root, x=260, y=75, offset=115)

        y = 65
        for slot in range(self.hash_table.size):
            c.create_rectangle(650, y, 730, y + 34, fill=self.CARD, outline=self.BLUE)
            c.create_text(690, y + 17, text=f"Bucket {slot}", fill=self.BLUE, font=("Consolas", 8, "bold"))
            x = 765
            for key, value in self.hash_table.table[slot]:
                c.create_line(x - 30, y + 17, x, y + 17, fill=self.GREEN, width=2, arrow=tk.LAST)
                c.create_rectangle(x, y, x + 116, y + 34, fill=self.BLUE, outline=self.BLUE)
                c.create_text(x + 58, y + 17, text=f"{key} : {value}", fill=self.BG, font=("Segoe UI", 8, "bold"))
                x += 148
            y += 52

    def _plot_bst(self, node, x, y, offset):
        if node is None:
            return
        c = self.tree_canvas
        left = self.bst.structure[node]["left"]
        right = self.bst.structure[node]["right"]

        if left is not None:
            c.create_line(x, y + 20, x - offset, y + 73, fill=self.MUTED, width=2)
            self._plot_bst(left, x - offset, y + 92, max(42, offset * 0.58))
        if right is not None:
            c.create_line(x, y + 20, x + offset, y + 73, fill=self.MUTED, width=2)
            self._plot_bst(right, x + offset, y + 92, max(42, offset * 0.58))

        c.create_oval(x - 22, y - 22, x + 22, y + 22, fill=self.PINK, outline=self.PINK)
        c.create_text(x, y, text=str(node), fill=self.TEXT, font=("Segoe UI", 9, "bold"))

    def _bst_add(self):
        value = self._read_int(self.tree_key, "BST key")
        if value is not None:
            self.bst.insert(value)
            self._draw_tree_hash()
            self._refresh_analytics_if_ready()

    def _hash_add(self):
        value = self._read_int(self.tree_key, "hash key")
        if value is not None:
            self.hash_table.insert(value, "BlockVal")
            self._draw_tree_hash()
            self._refresh_analytics_if_ready()

    # ------------------------------------------------------------
    # GRAPH
    # ------------------------------------------------------------

    def _init_graph_structures(self):
        self._section_title(
            self.tab_net,
            "Network Graph",
            "Add undirected edges and inspect the adjacency structure visually.",
        )

        controls = tk.Frame(self.tab_net, bg=self.CARD, padx=14, pady=12)
        controls.pack(fill="x", padx=18, pady=(0, 10))
        tk.Label(controls, text="Node U", fg=self.MUTED, bg=self.CARD, font=("Segoe UI", 9, "bold")).pack(side="left")
        self.g_u = self._entry(controls, width=6, default="A")
        self.g_u.pack(side="left", padx=(8, 12))
        tk.Label(controls, text="Node V", fg=self.MUTED, bg=self.CARD, font=("Segoe UI", 9, "bold")).pack(side="left")
        self.g_v = self._entry(controls, width=6, default="E")
        self.g_v.pack(side="left", padx=(8, 12))
        self._button(controls, "Add Edge", self._graph_link, self.AMBER).pack(side="left")

        self.net_canvas = tk.Canvas(self.tab_net, bg=self.BG, highlightthickness=0)
        self.net_canvas.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        self._draw_graph()

    def _graph_positions(self):
        nodes = sorted(self.graph.matrix)
        if not nodes:
            return {}
        center_x, center_y = 520, 280
        radius = min(220, 85 + 20 * len(nodes))
        positions = {}
        for index, node in enumerate(nodes):
            angle = (2 * math.pi * index / len(nodes)) - math.pi / 2
            positions[node] = (
                center_x + radius * math.cos(angle),
                center_y + radius * math.sin(angle),
            )
        return positions

    def _draw_graph(self):
        c = self.net_canvas
        c.delete("all")
        positions = self._graph_positions()
        drawn_edges = set()

        for node, neighbors in self.graph.matrix.items():
            for neighbor in neighbors:
                edge = tuple(sorted((node, neighbor)))
                if edge in drawn_edges or neighbor not in positions:
                    continue
                x1, y1 = positions[node]
                x2, y2 = positions[neighbor]
                c.create_line(x1, y1, x2, y2, fill=self.BORDER, width=3)
                drawn_edges.add(edge)

        for node, (x, y) in positions.items():
            c.create_oval(x - 25, y - 25, x + 25, y + 25, fill=self.BLUE, outline=self.BLUE)
            c.create_text(x, y, text=node, fill=self.BG, font=("Segoe UI", 11, "bold"))

        c.create_text(
            24,
            24,
            anchor="nw",
            text=f"Nodes: {len(self.graph.matrix)}    Edges: {len(drawn_edges)}",
            fill=self.MUTED,
            font=("Segoe UI", 9, "bold"),
        )

    def _graph_link(self):
        u = self.g_u.get().strip().upper()
        v = self.g_v.get().strip().upper()
        if not u or not v:
            messagebox.showerror("Missing nodes", "Enter both node names.")
            return
        if u == v:
            messagebox.showwarning("Self edge", "Choose two different nodes for this visualizer.")
            return
        self.graph.add_edge(u, v)
        self._draw_graph()
        self._refresh_analytics_if_ready()

    # ------------------------------------------------------------
    # LIVE ANALYTICS
    # ------------------------------------------------------------

    def _init_analytics(self):
        self._section_title(
            self.tab_analytics,
            "Live Complexity Analytics",
            "The chart uses your selected N and marks the live sizes of the structures in this project.",
        )

        controls = tk.Frame(self.tab_analytics, bg=self.CARD, padx=14, pady=12)
        controls.pack(fill="x", padx=18, pady=(0, 8))
        tk.Label(controls, text="Maximum input size (N)", fg=self.MUTED, bg=self.CARD, font=("Segoe UI", 9, "bold")).pack(side="left")
        self.analytics_n = self._entry(controls, width=8, default="50")
        self.analytics_n.pack(side="left", padx=(8, 12))
        self._button(controls, "Plot Input", self._render_analytics, self.GREEN).pack(side="left", padx=4)
        self._button(controls, "Reset N", self._reset_analytics, self.BLUE).pack(side="left", padx=4)

        self.analytics_status = tk.Label(
            controls,
            text="",
            fg=self.MUTED,
            bg=self.CARD,
            font=("Segoe UI", 9),
        )
        self.analytics_status.pack(side="right")

        self.fig, self.ax = plt.subplots(figsize=(8.4, 4.6), facecolor=self.SURFACE)
        self.analytics_canvas = FigureCanvasTkAgg(self.fig, master=self.tab_analytics)
        self.analytics_canvas.get_tk_widget().pack(fill="both", expand=True, padx=18, pady=(0, 18))
        self._render_analytics()

    def _reset_analytics(self):
        self.analytics_n.delete(0, tk.END)
        self.analytics_n.insert(0, "50")
        self._render_analytics()

    def _refresh_analytics_if_ready(self):
        if hasattr(self, "analytics_canvas"):
            self._render_analytics(show_errors=False)

    def _render_analytics(self, show_errors=True):
        try:
            max_n = int(self.analytics_n.get())
            if max_n < 2 or max_n > 500:
                raise ValueError
        except ValueError:
            if show_errors:
                messagebox.showerror("Invalid N", "Enter an integer from 2 to 500.")
            return

        n = np.linspace(1, max_n, max(120, max_n * 4))
        self.ax.clear()
        self.ax.set_facecolor(self.BG)

        self.ax.plot(n, np.ones_like(n), label="Hash lookup • O(1)", linewidth=2.3)
        self.ax.plot(n, np.log2(n), label="Balanced BST search • O(log N)", linewidth=2.3)
        self.ax.plot(n, n, label="Linear scan • O(N)", linewidth=2.3)
        self.ax.plot(n, n * np.log2(n), label="Efficient sorting • O(N log N)", linewidth=2.3, linestyle="--")

        live_sizes = {
            "Array": len(self.array_data),
            "Linked List": len(self.linked_list),
            "Stack": len(self.stack),
            "Queue": len(self.queue),
            "BST": len(self.bst.structure),
            "Graph": len(self.graph.matrix),
        }

        # Live project inputs are plotted as points against O(N).
        for label, size in live_sizes.items():
            if size <= max_n:
                self.ax.scatter([size], [size], s=42, zorder=5)
                self.ax.annotate(label, (size, size), xytext=(5, 6), textcoords="offset points", fontsize=8)

        self.ax.set_title("Complexity Growth vs. Current Structure Sizes", color=self.TEXT, fontsize=12, fontweight="bold")
        self.ax.set_xlabel("Input size (N)", color=self.MUTED)
        self.ax.set_ylabel("Relative operation steps", color=self.MUTED)
        self.ax.tick_params(colors=self.MUTED, labelsize=8)
        self.ax.grid(True, linestyle=":", alpha=0.25)
        for spine in self.ax.spines.values():
            spine.set_color(self.BORDER)

        legend = self.ax.legend(facecolor=self.SURFACE, edgecolor=self.BORDER, fontsize=8)
        for text in legend.get_texts():
            text.set_color(self.TEXT)

        self.analytics_status.config(
            text=(
                f"Live sizes  •  Array {len(self.array_data)}  |  LL {len(self.linked_list)}  |  "
                f"Stack {len(self.stack)}  |  Queue {len(self.queue)}  |  BST {len(self.bst.structure)}"
            )
        )
        self.fig.tight_layout()
        self.analytics_canvas.draw_idle()

    # ------------------------------------------------------------
    # ALGORITHM + FLOWCHART
    # ------------------------------------------------------------

    def _init_algorithm_flow(self):
        self._section_title(
            self.tab_algo,
            "Algorithm Reference & Flowchart",
            "A compact explanation of how user input moves through the visualizer.",
        )

        body = tk.Frame(self.tab_algo, bg=self.SURFACE)
        body.pack(fill="both", expand=True, padx=18, pady=(0, 18))
        body.grid_columnconfigure(0, weight=1)
        body.grid_columnconfigure(1, weight=1)
        body.grid_rowconfigure(0, weight=1)

        algo = tk.Frame(body, bg=self.CARD, padx=18, pady=16)
        algo.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        tk.Label(algo, text="CORE ALGORITHM", fg=self.GREEN, bg=self.CARD, font=("Segoe UI", 11, "bold")).pack(anchor="w")

        algorithm_text = (
            "1. Read the value or node pair entered by the user.\n\n"
            "2. Validate the input before changing any structure.\n\n"
            "3. Execute the selected operation: push, pop, enqueue, dequeue, "
            "linked-list insert, BST insert, hash insert, or graph edge insertion.\n\n"
            "4. Update the underlying Python data structure.\n\n"
            "5. Redraw the corresponding canvas.\n\n"
            "6. Refresh the analytics chart so it reflects the latest structure sizes."
        )
        tk.Label(
            algo,
            text=algorithm_text,
            justify="left",
            wraplength=455,
            fg=self.TEXT,
            bg=self.CARD,
            font=("Segoe UI", 10),
        ).pack(anchor="nw", pady=(14, 0))

        flow = tk.Frame(body, bg=self.CARD, padx=14, pady=14)
        flow.grid(row=0, column=1, sticky="nsew", padx=(8, 0))
        tk.Label(flow, text="APPLICATION FLOW", fg=self.BLUE, bg=self.CARD, font=("Segoe UI", 11, "bold")).pack(anchor="w")

        canvas = tk.Canvas(flow, bg=self.CARD, highlightthickness=0, height=470)
        canvas.pack(fill="both", expand=True, pady=(8, 0))

        def box(y, text, color):
            canvas.create_rectangle(75, y, 390, y + 54, fill=self.BG, outline=color, width=2)
            canvas.create_text(232, y + 27, text=text, fill=self.TEXT, font=("Segoe UI", 9, "bold"), width=285)
            return y + 54

        y = 18
        steps = [
            ("USER INPUT", self.BLUE),
            ("VALIDATE INPUT", self.AMBER),
            ("SELECT DATA-STRUCTURE OPERATION", self.PURPLE),
            ("UPDATE INTERNAL DATA", self.PINK),
            ("REDRAW VISUALIZATION", self.GREEN),
            ("REFRESH ANALYTICS", self.BLUE),
        ]

        for index, (text, color) in enumerate(steps):
            bottom = box(y, text, color)
            if index < len(steps) - 1:
                canvas.create_line(232, bottom, 232, bottom + 22, fill=self.MUTED, width=2, arrow=tk.LAST)
            y = bottom + 28


if __name__ == "__main__":
    root = tk.Tk()
    app = DSAVisualizer(root)
    root.mainloop()