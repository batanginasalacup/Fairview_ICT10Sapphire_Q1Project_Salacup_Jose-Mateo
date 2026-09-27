from pyscript import display, document


# RECEIPT GENERATOR

# Prices
Bangerz_price = 4500
BRAT_price = 2300
Prima_price = 2500
DETOUR_price = 1700
Olivia_price = 3000


def generate_receipt(e):

    # Clear previous receipt
    document.getElementById("receipt").innerHTML = ""

    # Get customer information
    customer_name = document.getElementById("customerName").value
    contact_number = document.getElementById("contactNumber").value

    # Get quantities
    Bangerz_quantity = int(document.getElementById("BangerzQty").value)
    BRAT_quantity = int(document.getElementById("BRATQty").value)
    Prima_quantity = int(document.getElementById("PrimaQty").value)
    DETOUR_quantity = int(document.getElementById("DETOURQty").value)
    Olivia_quantity = int(document.getElementById("OliviaQty").value)

    # Calculate subtotal
    subtotal = (
        (Bangerz_price * Bangerz_quantity)
        + (BRAT_price * BRAT_quantity)
        + (Prima_price * Prima_quantity)
        + (DETOUR_price * DETOUR_quantity)
        + (Olivia_price * Olivia_quantity)
    )

    # Calculate VAT
    vat = subtotal * 0.12

    # Calculate total
    total_amount = subtotal + vat

    # Display receipt
    display("===== RECEIPT =====", target="receipt")
    display(f"Customer Name: {customer_name}", target="receipt")
    display(f"Contact Number: {contact_number}", target="receipt")
    display("-------------------------", target="receipt")

    if Bangerz_quantity > 0:
        display(
            f"Bangerz x {Bangerz_quantity}: ₱{Bangerz_price * Bangerz_quantity:,.2f}",
            target="receipt"
        )

    if BRAT_quantity > 0:
        display(
            f"BRAT x {BRAT_quantity}: ₱{BRAT_price * BRAT_quantity:,.2f}",
            target="receipt"
        )

    if Prima_quantity > 0:
        display(
            f"Prima x {Prima_quantity}: ₱{Prima_price * Prima_quantity:,.2f}",
            target="receipt"
        )

    if DETOUR_quantity > 0:
        display(
            f"DETOUR x {DETOUR_quantity}: ₱{DETOUR_price * DETOUR_quantity:,.2f}",
            target="receipt"
        )

    if Olivia_quantity > 0:
        display(
            f"You Seem Pretty Sad x {Olivia_quantity}: "
            f"₱{Olivia_price * Olivia_quantity:,.2f}",
            target="receipt"
        )

    display("-------------------------", target="receipt")
    display(f"Subtotal: ₱{subtotal:,.2f}", target="receipt")
    display(f"VAT (12%): ₱{vat:,.2f}", target="receipt")
    display(f"Total Amount: ₱{total_amount:,.2f}", target="receipt")


# SKU GENERATOR

def generate_sku(e):

    # Clear previous SKU
    document.getElementById("skuOutput").innerHTML = ""

    # Get product information
    category = document.getElementById("category").value
    product_name = document.getElementById("productName").value
    stock_quantity = document.getElementById("stockQuantity").value

    # Convert category and product name to uppercase
    category = category.upper()
    product_name = product_name.upper()

    # Create the SKU
    sku = (
        category[:2]
        + product_name[:3]
        + stock_quantity.zfill(3)
    )

    # Display the SKU
    display(f"Generated SKU: {sku}", target="skuOutput")