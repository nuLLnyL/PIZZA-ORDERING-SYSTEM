import tkinter as tk
from tkinter import ttk, messagebox

# PIZZA MENU
pizza_prices = {
    "Pepperoni": 150,
    "Hawaiian": 180,
    "Ham & Cheese": 120,
    "Durian": 100
}

size_prices = {
    "Small": 0,
    "Medium": 25,
    "Large": 50
}

topping_prices = {
    "Extra Cheese": 30,
    "Mushrooms": 40,
    "Bacon": 50
}


# WINDOW
window = tk.Tk()
window.title("🍕 Pizza Ordering System")
window.geometry("900x800")
window.minsize(800, 700)
window.configure(bg="#FFF8E1")
window.resizable(True, True)


# VARIABLES
pizza_display = [
    f"{pizza} - ₱{price}"
    for pizza, price in pizza_prices.items()
]

pizza_var = tk.StringVar(
    value=f"Pepperoni - ₱{pizza_prices['Pepperoni']}"
)
size_var = tk.StringVar(value="Small")
quantity_var = tk.IntVar(value=1)

topping_vars = {
    topping: tk.BooleanVar(value=False)
    for topping in topping_prices
}


# STYLE
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground="#FFF8E1",
    background="#FFB74D",
    foreground="black"
)


# TITLE
title = tk.Label(
    window,
    text="🍕 PIZZA ORDERING SYSTEM 🍕",
    font=("Segoe UI", 24, "bold"),
    bg="#43A047",
    fg="#FFD54F",
    pady=15
)
title.pack(fill="x", pady=10)


# ORDER FRAME
order_frame = tk.Frame(
    window,
    bg="#6D4C41",
    padx=25,
    pady=20
)
order_frame.pack(fill="x", padx=25)


# PIZZA FLAVOR
tk.Label(
    order_frame,
    text="Select Pizza Flavor:",
    font=("Segoe UI", 12, "bold"),
    bg="#6D4C41",
    fg="white"
).pack(anchor="w")

pizza_dropdown = ttk.Combobox(
    order_frame,
    textvariable=pizza_var,
    values=pizza_display,
    state="readonly",
    font=("Segoe UI", 11)
)
pizza_dropdown.pack(fill="x", pady=8)


# PIZZA SIZE
tk.Label(
    order_frame,
    text="Select Pizza Size:",
    font=("Segoe UI", 12, "bold"),
    bg="#6D4C41",
    fg="white"
).pack(anchor="w", pady=(12, 5))

for size, price in size_prices.items():
    tk.Radiobutton(
        order_frame,
        text=f"{size} (+₱{price})",
        variable=size_var,
        value=size,
        font=("Segoe UI", 11),
        bg="#6D4C41",
        fg="white",
        selectcolor="#E53935",
        activebackground="#43A047",
        activeforeground="white"
    ).pack(anchor="w")


# TOPPINGS
tk.Label(
    order_frame,
    text="Extra Toppings:",
    font=("Segoe UI", 12, "bold"),
    bg="#6D4C41",
    fg="white"
).pack(anchor="w", pady=(12, 5))

for topping, price in topping_prices.items():
    tk.Checkbutton(
        order_frame,
        text=f"{topping} (+₱{price})",
        variable=topping_vars[topping],
        font=("Segoe UI", 11),
        bg="#6D4C41",
        fg="white",
        selectcolor="#E53935",
        activebackground="#43A047",
        activeforeground="white"
    ).pack(anchor="w")


# QUANTITY
tk.Label(
    order_frame,
    text="Quantity:",
    font=("Segoe UI", 12, "bold"),
    bg="#6D4C41",
    fg="white"
).pack(anchor="w", pady=(12, 5))

quantity_spinbox = tk.Spinbox(
    order_frame,
    from_=1,
    to=50,
    textvariable=quantity_var,
    width=10,
    font=("Segoe UI", 12)
)
quantity_spinbox.pack(anchor="w")


# FUNCTIONS
def calculate_total():

    selected_pizza = pizza_var.get()
    pizza = selected_pizza.split(" - ₱")[0]
    size = size_var.get()

    try:
        quantity = int(quantity_var.get())

        if quantity < 1 or quantity > 50:
            raise ValueError

    except (ValueError, tk.TclError):
        messagebox.showerror(
            "Invalid Quantity",
            "Please enter a quantity between 1 and 50."
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Order",
        "Are you sure you want to place this order?"
    )

    if not confirm:
        return

    pizza_price = pizza_prices[pizza]
    size_price = size_prices[size]

    selected_toppings = [
        topping
        for topping, var in topping_vars.items()
        if var.get()
    ]

    topping_price = sum(
        topping_prices[topping]
        for topping in selected_toppings
    )

    total_per_pizza = pizza_price + size_price + topping_price
    total = total_per_pizza * quantity

    receipt_text.delete("1.0", tk.END)

    receipt_text.insert(
        tk.END,
        "====================================\n"
    )

    receipt_text.insert(
        tk.END,
        "      🍕 PIZZA ORDER RECEIPT 🍕\n"
    )

    receipt_text.insert(
        tk.END,
        "====================================\n\n"
    )

    receipt_text.insert(
        tk.END,
        f"Flavor   : {pizza} (₱{pizza_price})\n"
    )

    receipt_text.insert(
        tk.END,
        f"Size     : {size}\n"
    )

    receipt_text.insert(
        tk.END,
        f"Quantity : {quantity}\n\n"
    )

    if selected_toppings:
        receipt_text.insert(
            tk.END,
            "Toppings:\n"
        )

        for topping in selected_toppings:
            receipt_text.insert(
                tk.END,
                f" • {topping} (₱{topping_prices[topping]})\n"
            )
    else:
        receipt_text.insert(
            tk.END,
            "Toppings : None\n"
        )

    receipt_text.insert(
        tk.END,
        "\n------------------------------------\n"
    )

    receipt_text.insert(
        tk.END,
        f"TOTAL AMOUNT : ₱{total:,.2f}\n"
    )

    receipt_text.insert(
        tk.END,
        "====================================\n"
    )

    receipt_text.insert(
        tk.END,
        "Thank you for ordering! ❤️"
    )


def reset_order():

    pizza_var.set(
    f"Pepperoni - ₱{pizza_prices['Pepperoni']}"
)
    size_var.set("Small")
    quantity_var.set(1)

    for variable in topping_vars.values():
        variable.set(False)

    receipt_text.delete("1.0", tk.END)


# BUTTONS
button_frame = tk.Frame(
    window,
    bg="#FFF3E0"
)
button_frame.pack(pady=15)

calculate_button = tk.Button(
    button_frame,
    text="🛒 PLACE ORDER",
    font=("Segoe UI", 12, "bold"),
    bg="#FF0099",
    fg="white",
    width=18,
    height=2,
    command=calculate_total
)
calculate_button.grid(row=0, column=0, padx=10)

reset_button = tk.Button(
    button_frame,
    text="🔄 RESET",
    font=("Segoe UI", 12, "bold"),
    bg="#8C2FAE",
    fg="white",
    width=12,
    height=2,
    command=reset_order
)
reset_button.grid(row=0, column=1, padx=10)


# RECEIPT AREA

tk.Label(
    window,
    text="📋 ORDER SUMMARY",
    font=("Segoe UI", 16, "bold"),
    bg="#FFF8E1",
    fg="#F41FBB"
).pack(pady=(5, 5))

receipt_frame = tk.Frame(
    window,
    bg="#FFF8E1"
)

receipt_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)

scrollbar = tk.Scrollbar(receipt_frame)

receipt_text = tk.Text(
    receipt_frame,
    font=("Consolas", 11),
    bg="#FFFDE7",
    fg="black",
    relief="solid",
    bd=2,
    wrap="word",
    yscrollcommand=scrollbar.set
)

scrollbar.config(
    command=receipt_text.yview
)

scrollbar.pack(
    side="right",
    fill="y"
)

receipt_text.pack(
    side="left",
    fill="both",
    expand=True
)


window.mainloop()