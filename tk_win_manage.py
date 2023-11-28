import tkinter as tk


def generate_table(out):
    main_window = tk.Tk()
    main_window.title("Sweep Pinger")

    table = tk.Frame(main_window)
    table.pack()

    table_mac = ttk.Treeview(table)

    table_mac['columns'] = ("id", "IP", "MAC", "Producer")

    table_mac.column("#0", width=0, stretch=tk.NO)
    table_mac.column("id", anchor=tk.CENTER, width=80)
    table_mac.column("IP", anchor=tk.CENTER, width=80)
    table_mac.column("MAC", anchor=tk.CENTER, width=80)
    table_mac.column("Producer", anchor=tk.CENTER, width=80)

    table_mac.heading("#0", text="", anchor=tk.CENTER)
    table_mac.heading("id", text="id", anchor=tk.CENTER)
    table_mac.heading("IP", text="IP", anchor=tk.CENTER)
    table_mac.heading("MAC", text="MAC", anchor=tk.CENTER)
    table_mac.heading("Producer", text="Producer", anchor=tk.CENTER)

    for i in range(len(out)):
        if len(out[i]) > 1:
            table_mac.insert(parent="", index="end", iid=i + 1, text="",
                             values=(i + 1, out[i][0], out[i][1], out[i][2]))