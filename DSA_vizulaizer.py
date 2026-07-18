import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# =========================================================================
# 🧠 CORE ALGORITHMIC STRUCTURAL ENGINES
# =========================================================================

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
        curr = list(self.structure.keys())[0]
        while True:
            if value < curr:
                if self.structure[curr]["left"] is None:
                    self.structure[curr]["left"] = value
                    self.structure[value] = {"left": None, "right": None}
                    break
                curr = self.structure[curr]["left"]
            elif value > curr:
                if self.structure[curr]["right"] is None:
                    self.structure[curr]["right"] = value
                    self.structure[value] = {"left": None, "right": None}
                    break
                curr = self.structure[curr]["right"]
            else:
                break

class GraphEngine:
    def __init__(self):
        self.matrix = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}
        
    def add_edge(self, u, v):
        if u not in self.matrix: 
            self.matrix[u] = []
        if v not in self.matrix: 
            self.matrix[v] = []
        if v not in self.matrix[u]: 
            self.matrix[u].append(v)
        if u not in self.matrix[v]: 
            self.matrix[v].append(u)

# =========================================================================
# 🖥️ GUI ENGINE FRAMEWORK
# =========================================================================

class GrandDSAVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Unified 7-in-1 DSA Structural Visualizer")
        self.root.geometry("1150x760")
        self.root.configure(bg="#0F172A")

        # Core Engine Datasets
        self.array_data = [23, 45, 12, 67, 89]
        self.linked_list = [10, 20, 30]
        self.stack = [15, 30]
        self.queue = [11, 22]
        self.hash_table = HashTableEngine()
        self.bst = BSTEngine()
        self.graph = GraphEngine()

        # Seed Sample Values
        for x in [45, 23, 65]: 
            self.bst.insert(x)
        self.hash_table.insert(12, "DataA")
        self.hash_table.insert(17, "CollisionB")

        self.setup_ui_dashboard()

    def setup_ui_dashboard(self):
        header = tk.Frame(self.root, bg="#1E293B", height=65)
        header.pack(fill="x")
        
        title = tk.Label(header, text="⚔️ Grand Unified DSA Engine & Complexity Analytics", font=("Helvetica", 14, "bold"), fg="#38BDF8", bg="#1E293B")
        title.pack(side="left", padx=25, pady=15)
        
        badge = tk.Label(header, text="VERIFIED PRODUCTION LAYER", font=("Helvetica", 9, "bold"), fg="#0F172A", bg="#34D399", padx=10, pady=5)
        badge.pack(side="right", padx=25, pady=15)

        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=15, pady=15)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TNotebook', background="#0F172A", borderwidth=0)
        style.configure('TNotebook.Tab', background="#1E293B", foreground="#94A3B8", padding=[12, 6], font=("Helvetica", 9, "bold"))
        style.map('TNotebook.Tab', background=[('selected', "#38BDF8")], foreground=[('selected', "#0F172A")])

        # Main Tab Frames Mapping
        self.tab_linear = tk.Frame(notebook, bg="#1E293B")
        self.tab_tree = tk.Frame(notebook, bg="#1E293B")
        self.tab_net = tk.Frame(notebook, bg="#1E293B")
        self.tab_analytics = tk.Frame(notebook, bg="#1E293B")

        notebook.add(self.tab_linear, text=" 💾 Array / LL / Stack / Queue ")
        notebook.add(self.tab_tree, text=" 🌲 BST / Hash Table ")
        notebook.add(self.tab_net, text=" 🕸️ Network Graph ")
        notebook.add(self.tab_analytics, text=" 📊 Matplotlib Complexity ")

        self.init_linear_structures()
        self.init_tree_hash_structures()
        self.init_graph_structures()
        self.init_complexity_analytics()

    # ---------------------------------------------------------------------
    # 🗂️ MODULE 1: LINEAR LOGIC RENDERING
    # ---------------------------------------------------------------------
    def init_linear_structures(self):
        ctrl = tk.Frame(self.tab_linear, bg="#1E293B")
        ctrl.pack(fill="x", pady=10)

        tk.Label(ctrl, text="Value Entry:", fg="#94A3B8", bg="#1E293B").pack(side="left", padx=5)
        self.lin_input = tk.Entry(ctrl, width=6, bg="#0F172A", fg="white", bd=1, relief="solid")
        self.lin_input.pack(side="left", padx=5)
        self.lin_input.insert(0, "50")

        tk.Button(ctrl, text="Push Stack", bg="#EC4899", fg="white", font=("Helvetica", 8, "bold"), command=self.op_stack_push).pack(side="left", padx=5)
        tk.Button(ctrl, text="Pop Stack", bg="#F43F5E", fg="white", font=("Helvetica", 8, "bold"), command=self.op_stack_pop).pack(side="left", padx=2)
        tk.Button(ctrl, text="Enqueue", bg="#EAB308", fg="#0F172A", font=("Helvetica", 8, "bold"), command=self.op_queue_enq).pack(side="left", padx=10)
        tk.Button(ctrl, text="Dequeue", bg="#CA8A04", fg="white", font=("Helvetica", 8, "bold"), command=self.op_queue_deq).pack(side="left", padx=2)
        tk.Button(ctrl, text="Insert LL", bg="#8B5CF6", fg="white", font=("Helvetica", 8, "bold"), command=self.op_ll_ins).pack(side="left", padx=10)

        self.lin_canvas = tk.Canvas(self.tab_linear, bg="#0F172A", bd=0, highlightthickness=0)
        self.lin_canvas.pack(fill="both", expand=True, padx=15, pady=5)
        self.draw_linear_canvas()

    def draw_linear_canvas(self):
        canvas = self.lin_canvas
        canvas.delete("all")
        
        # 1. Array Layout
        canvas.create_text(80, 40, text="[ARRAY DATABLOCK]", fill="#38BDF8", font=("Helvetica", 10, "bold"))
        ax = 50
        for idx, val in enumerate(self.array_data):
            canvas.create_rectangle(ax, 60, ax+60, 100, fill="#38BDF8", outline="#0EA5E9", width=2)
            canvas.create_text(ax+30, 80, text=str(val), fill="#0F172A", font=("Helvetica", 10, "bold"))
            canvas.create_text(ax+30, 115, text=f"[{idx}]", fill="#64748B", font=("Courier", 8))
            ax += 70

        # 2. Linked List Nodes
        canvas.create_text(80, 160, text="[LINKED LIST MAPPED]", fill="#8B5CF6", font=("Helvetica", 10, "bold"))
        lx = 50
        for idx, val in enumerate(self.linked_list):
            canvas.create_rectangle(lx, 180, lx+70, 215, fill="#8B5CF6", outline="#A78BFA", width=2)
            canvas.create_text(lx+35, 197, text=f"Val: {val}", fill="white", font=("Helvetica", 9, "bold"))
            if idx < len(self.linked_list) - 1:
                canvas.create_line(lx+70, 197, lx+110, 197, fill="#34D399", arrow=tk.LAST, width=2)
            else:
                canvas.create_text(lx+95, 197, text="NULL", fill="#EF4444", font=("Helvetica", 8, "bold"))
            lx += 110

        # 3. Stack Elements Layout
        canvas.create_text(600, 160, text="[STACK SYSTEM (LIFO)]", fill="#EC4899", font=("Helvetica", 10, "bold"))
        canvas.create_line(580, 200, 580, 360, fill="#64748B", width=2)
        canvas.create_line(680, 200, 680, 360, fill="#64748B", width=2)
        canvas.create_line(580, 360, 680, 360, fill="#64748B", width=2)
        sy = 330
        for idx, item in enumerate(self.stack):
            canvas.create_rectangle(585, sy, 675, sy+25, fill="#EC4899", outline="#F472B6")
            canvas.create_text(630, sy+12, text=str(item), fill="white", font=("Helvetica", 9, "bold"))
            if idx == len(self.stack)-1: 
                canvas.create_text(715, sy+12, text="➔ TOP", fill="#EC4899", font=("Helvetica", 9, "bold"))
            sy -= 30

        # 4. Queue Buffer Interface
        canvas.create_text(100, 270, text="[QUEUE BUFFER (FIFO)]", fill="#EAB308", font=("Helvetica", 10, "bold"))
        canvas.create_line(50, 300, 450, 300, fill="#64748B", width=2)
        canvas.create_line(50, 350, 450, 350, fill="#64748B", width=2)
        qx = 70
        for idx, item in enumerate(self.queue):
            canvas.create_rectangle(qx, 305, qx+50, 345, fill="#EAB308", outline="#FBBF24")
            canvas.create_text(qx+25, 325, text=str(item), fill="#0F172A", font=("Helvetica", 10, "bold"))
            if idx == 0: 
                canvas.create_text(qx+25, 290, text="FRONT", fill="#EF4444", font=("Helvetica", 8, "bold"))
            if idx == len(self.queue)-1: 
                canvas.create_text(qx+25, 365, text="REAR", fill="#10B981", font=("Helvetica", 8, "bold"))
            qx += 65

    def op_stack_push(self):
        try:
            self.stack.append(int(self.lin_input.get()))
            self.draw_linear_canvas()
        except ValueError: 
            pass
            
    def op_stack_pop(self):
        if self.stack: 
            self.stack.pop()
            self.draw_linear_canvas()
            
    def op_queue_enq(self):
        try:
            self.queue.append(int(self.lin_input.get()))
            self.draw_linear_canvas()
        except ValueError: 
            pass
            
    def op_queue_deq(self):
        if self.queue: 
            self.queue.pop(0)
            self.draw_linear_canvas()
            
    def op_ll_ins(self):
        try:
            self.linked_list.append(int(self.lin_input.get()))
            self.draw_linear_canvas()
        except ValueError: 
            pass

    # ---------------------------------------------------------------------
    # 🌲 MODULE 2: BST & HASH CHAINS VISUALIZATION
    # ---------------------------------------------------------------------
    def init_tree_hash_structures(self):
        ctrl = tk.Frame(self.tab_tree, bg="#1E293B")
        ctrl.pack(fill="x", pady=10)

        tk.Label(ctrl, text="Integer Key:", fg="#94A3B8", bg="#1E293B").pack(side="left", padx=5)
        self.tree_key = tk.Entry(ctrl, width=6, bg="#0F172A", fg="white", bd=1, relief="solid")
        self.tree_key.pack(side="left", padx=5) 
        self.tree_key.insert(0, "30")

        tk.Button(ctrl, text="Insert into BST Node Tree", bg="#EC4899", fg="white", font=("Helvetica", 8, "bold"), command=self.op_bst_add).pack(side="left", padx=10)
        tk.Button(ctrl, text="Map into Linked Hash bucket", bg="#38BDF8", fg="#0F172A", font=("Helvetica", 8, "bold"), command=self.op_hash_add).pack(side="left", padx=5)

        self.tree_canvas = tk.Canvas(self.tab_tree, bg="#0F172A", bd=0, highlightthickness=0)
        self.tree_canvas.pack(fill="both", expand=True, padx=15, pady=5)
        self.draw_tree_hash_canvas()

    def draw_tree_hash_canvas(self):
        canvas = self.tree_canvas
        canvas.delete("all")

        # 1. BST Drawing Pipeline
        canvas.create_text(200, 25, text="[BINARY SEARCH TREE DISPERSION]", fill="#EC4899", font=("Helvetica", 10, "bold"))
        if self.bst.structure:
            root = list(self.bst.structure.keys())[0]
            self._canvas_plot_bst(root, x=220, y=60, x_offset=60)

        # 2. Hash Table Overflow Chains Mapping
        canvas.create_text(750, 25, text="[HASH TABLE OVERFLOW CHAINS]", fill="#38BDF8", font=("Helvetica", 10, "bold"))
        hy = 60
        for slot in range(self.hash_table.size):
            canvas.create_rectangle(650, hy, 720, hy+30, fill="#1E293B", outline="#38BDF8")
            canvas.create_text(685, hy+15, text=f"Slot [{slot}]", fill="#38BDF8", font=("Courier", 9, "bold"))
            
            hx = 750
            for pair in self.hash_table.table[slot]:
                canvas.create_rectangle(hx, hy, hx+80, hy+30, fill="#38BDF8", outline="#0EA5E9")
                canvas.create_text(hx+40, hy+15, text=f"K:{pair[0]} [{pair[1]}]", fill="#0F172A", font=("Helvetica", 8, "bold"))
                canvas.create_line(hx-10, hy+15, hx, hy+15, fill="#34D399", arrow=tk.LAST, width=1.5)
                hx += 95
            hy += 45

    def _canvas_plot_bst(self, node, x, y, x_offset):
        if node is None: 
            return
        self.tree_canvas.create_oval(x-18, y-18, x+18, y+18, fill="#EC4899", outline="#F472B6", width=2)
        self.tree_canvas.create_text(x, y, text=str(node), fill="white", font=("Helvetica", 9, "bold"))
        
        left = self.bst.structure[node]["left"]
        right = self.bst.structure[node]["right"]

        if left is not None:
            self.tree_canvas.create_line(x-12, y+12, x-x_offset+10, y+35, fill="#94A3B8")
            self._canvas_plot_bst(left, x-x_offset, y+45, x_offset*0.5)
        if right is not None:
            self.tree_canvas.create_line(x+12, y+12, x+x_offset-10, y+35, fill="#94A3B8")
            self._canvas_plot_bst(right, x+x_offset, y+45, x_offset*0.5)

    def op_bst_add(self):
        try:
            self.bst.insert(int(self.tree_key.get()))
            self.draw_tree_hash_canvas()
        except ValueError: 
            pass
            
    def op_hash_add(self):
        try:
            k = int(self.tree_key.get())
            self.hash_table.insert(k, "BlockVal")
            self.draw_tree_hash_canvas()
        except ValueError: 
            pass

    # ---------------------------------------------------------------------
    # 🕸️ MODULE 3: NETWORK ADJACENCY MAPPING
    # ---------------------------------------------------------------------
    def init_graph_structures(self):
        ctrl = tk.Frame(self.tab_net, bg="#1E293B")
        ctrl.pack(fill="x", pady=10)

        tk.Label(ctrl, text="Node U:", fg="#94A3B8", bg="#1E293B").pack(side="left", padx=5)
        self.g_u = tk.Entry(ctrl, width=4, bg="#0F172A", fg="white", bd=1, relief="solid")
        self.g_u.pack(side="left", padx=5) 
        self.g_u.insert(0, "A")

        tk.Label(ctrl, text="Node V:", fg="#94A3B8", bg="#1E293B").pack(side="left", padx=5)
        self.g_v = tk.Entry(ctrl, width=4, bg="#0F172A", fg="white", bd=1, relief="solid")
        self.g_v.pack(side="left", padx=5) 
        self.g_v.insert(0, "E")

        tk.Button(ctrl, text="Construct Link Edge", bg="#EAB308", fg="#0F172A", font=("Helvetica", 8, "bold"), command=self.op_graph_link).pack(side="left", padx=10)

        self.net_canvas = tk.Canvas(self.tab_net, bg="#0F172A", bd=0, highlightthickness=0)
        self.net_canvas.pack(fill="both", expand=True, padx=15, pady=5)
        self.draw_graph_canvas()

    def draw_graph_canvas(self):
        canvas = self.net_canvas
        canvas.delete("all")
        
        fixed_positions = {"A": (150, 100), "B": (450, 100), "C": (150, 300), "D": (450, 300), "E": (300, 200), "F": (600, 200)}
        
        drawn_edges = set()
        for node, neighbors in self.graph.matrix.items():
            p1 = fixed_positions.get(node, (300, 200))
            for nbr in neighbors:
                p2 = fixed_positions.get(nbr, (300, 200))
                fingerprint = tuple(sorted([node, nbr]))
                if fingerprint not in drawn_edges:
                    canvas.create_line(p1[0], p1[1], p2[0], p2[1], fill="#64748B", width=2, dash=(4,2))
                    drawn_edges.add(fingerprint)

        for node, pos in fixed_positions.items():
            if node in self.graph.matrix:
                canvas.create_rectangle(pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20, fill="#38BDF8", outline="#0EA5E9", width=2)
                canvas.create_text(pos[0], pos[1], text=node, fill="#0F172A", font=("Helvetica", 11, "bold"))

    def op_graph_link(self):
        u = self.g_u.get().strip().upper()
        v = self.g_v.get().strip().upper()
        if u and v and u != v:
            self.graph.add_edge(u, v)
            self.draw_graph_canvas()

    # ---------------------------------------------------------------------
    # 📊 MODULE 4: PYPLOT OPERATIONAL TIME COMPLEXITY ANALYTICS
    # ---------------------------------------------------------------------
    def init_complexity_analytics(self):
        ctrl = tk.Frame(self.tab_analytics, bg="#1E293B")
        ctrl.pack(fill="x", pady=10)

        tk.Button(ctrl, text="Plot Structural Operations Trend", bg="#34D399", fg="#0F172A", font=("Helvetica", 9, "bold"), command=self.render_matplotlib_complexity).pack(side="left", padx=20)
        
        self.fig, self.ax = plt.subplots(figsize=(7, 3.8), facecolor="#1E293B")
        self.ana_canvas = FigureCanvasTkAgg(self.fig, master=self.tab_analytics)
        self.ana_canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=10)
        self.render_matplotlib_complexity()

    def render_matplotlib_complexity(self):
        self.ax.clear()
        self.ax.set_facecolor("#0F172A")

        n = np.linspace(1, 20, 100)
        
        c_o1 = np.ones(100)                          
        c_ologn = np.log2(n)                         
        c_on = n                                     
        c_onlogn = n * np.log2(n)                    

        self.ax.plot(n, c_o1, label="Hash Table Search: O(1)", color="#34D399", lw=2.5)
        self.ax.plot(n, c_ologn, label="BST Element Search: O(log N)", color="#EAB308", lw=2.5)
        self.ax.plot(n, c_on, label="Array / LL Scan: O(N)", color="#38BDF8", lw=2.5)
        self.ax.plot(n, c_onlogn, label="Optimal Sorting Target: O(N log N)", color="#EC4899", lw=2.5, linestyle="--")

        self.ax.set_title("Operational Time Complexity Bounds Mapping Suite", color="#94A3B8", fontsize=11, fontweight="bold")
        self.ax.set_xlabel("Data Set Size Elements (N)", color="#94A3B8", fontsize=9)
        self.ax.set_ylabel("Execution Step Metrics", color="#94A3B8", fontsize=9)
        self.ax.tick_params(colors="#94A3B8", labelsize=8)
        self.ax.grid(True, color="#1E293B", linestyle=":", alpha=0.6)
        
        leg = self.ax.legend(facecolor="#1E293B", edgecolor="#64748B")
        for text in leg.get_texts(): 
            text.set_color("#94A3B8")

        self.fig.tight_layout()
        self.ana_canvas.draw()


if __name__ == "__main__":
    main_window = tk.Tk()
    app = GrandDSAVisualizer(main_window)
    main_window.mainloop()