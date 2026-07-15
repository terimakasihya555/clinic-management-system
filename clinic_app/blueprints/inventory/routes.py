from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from clinic_app.models import db
from clinic_app.models.medicine import Medicine
from clinic_app.models.prescription import PrescriptionItem
from clinic_app.security import role_required
from clinic_app.utils.export_excel import create_excel_response

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")


@inventory_bp.route("/")
@login_required
@role_required("admin", "receptionist")
def index():
    keyword = request.args.get("q", "").strip()
    stock_status = request.args.get("stock_status", "").strip()

    query = Medicine.query

    if keyword:
        query = query.filter(Medicine.name.ilike(f"%{keyword}%"))

    if stock_status == "low":
        query = query.filter(Medicine.stock <= 10, Medicine.stock > 0)
    elif stock_status == "empty":
        query = query.filter(Medicine.stock <= 0)
    elif stock_status == "safe":
        query = query.filter(Medicine.stock > 10)

    medicines = query.order_by(Medicine.name.asc()).all()

    total_medicines = Medicine.query.count()
    total_stock = db.session.query(db.func.sum(Medicine.stock)).scalar() or 0
    low_stock = Medicine.query.filter(Medicine.stock <= 10, Medicine.stock > 0).count()
    empty_stock = Medicine.query.filter(Medicine.stock <= 0).count()

    stats = {
        "total_medicines": total_medicines,
        "total_stock": total_stock,
        "low_stock": low_stock,
        "empty_stock": empty_stock,
    }

    return render_template(
        "inventory/list.html",
        medicines=medicines,
        stats=stats,
        keyword=keyword,
        selected_stock_status=stock_status
    )


@inventory_bp.route("/export")
@login_required
@role_required("admin", "receptionist")
def export_inventory():
    keyword = request.args.get("q", "").strip()
    stock_status = request.args.get("stock_status", "").strip()

    query = Medicine.query

    if keyword:
        query = query.filter(Medicine.name.ilike(f"%{keyword}%"))

    if stock_status == "low":
        query = query.filter(Medicine.stock <= 10, Medicine.stock > 0)
    elif stock_status == "empty":
        query = query.filter(Medicine.stock <= 0)
    elif stock_status == "safe":
        query = query.filter(Medicine.stock > 10)

    medicines = query.order_by(Medicine.name.asc()).all()

    headers = [
        "Nama Obat",
        "Kategori",
        "Unit",
        "Stok",
        "Status",
        "Deskripsi"
    ]

    rows = []

    for medicine in medicines:
        if medicine.stock <= 0:
            status = "Habis"
        elif medicine.stock <= 10:
            status = "Stok Rendah"
        else:
            status = "Aman"

        rows.append([
            medicine.name,
            medicine.category or "-",
            medicine.unit,
            medicine.stock,
            status,
            medicine.description or "-"
        ])

    return create_excel_response(
        filename_prefix="inventori_obat",
        sheet_title="Inventori Obat",
        headers=headers,
        rows=rows
    )


@inventory_bp.route("/create", methods=["POST"])
@login_required
@role_required("admin")
def create():
    name = request.form.get("name", "").strip()
    unit = request.form.get("unit", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()
    stock_raw = request.form.get("stock", "0").strip()

    if not name:
        flash("Nama obat wajib diisi.", "danger")
        return redirect(url_for("inventory.index"))

    if not unit:
        flash("Unit obat wajib diisi.", "danger")
        return redirect(url_for("inventory.index"))

    try:
        stock = int(stock_raw)
    except ValueError:
        flash("Stok awal harus berupa angka.", "danger")
        return redirect(url_for("inventory.index"))

    if stock < 0:
        flash("Stok awal tidak boleh negatif.", "danger")
        return redirect(url_for("inventory.index"))

    medicine = Medicine(
        name=name,
        unit=unit,
        category=category,
        description=description,
        stock=stock
    )

    db.session.add(medicine)
    db.session.commit()

    flash("Obat berhasil ditambahkan.", "success")
    return redirect(url_for("inventory.index"))


@inventory_bp.route("/update/<int:medicine_id>", methods=["POST"])
@login_required
@role_required("admin")
def update(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)

    name = request.form.get("name", "").strip()
    unit = request.form.get("unit", "").strip()
    category = request.form.get("category", "").strip()
    description = request.form.get("description", "").strip()

    if not name:
        flash("Nama obat wajib diisi.", "danger")
        return redirect(url_for("inventory.index"))

    if not unit:
        flash("Unit obat wajib diisi.", "danger")
        return redirect(url_for("inventory.index"))

    medicine.name = name
    medicine.unit = unit
    medicine.category = category
    medicine.description = description

    db.session.commit()

    flash("Data obat berhasil diperbarui.", "success")
    return redirect(url_for("inventory.index"))


@inventory_bp.route("/adjust-stock/<int:medicine_id>", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def adjust_stock(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)

    adjustment_type = request.form.get("adjustment_type", "").strip()
    qty_raw = request.form.get("qty", "0").strip()

    try:
        qty = int(qty_raw)
    except ValueError:
        flash("Jumlah stok harus berupa angka.", "danger")
        return redirect(url_for("inventory.index"))

    if qty <= 0:
        flash("Jumlah stok harus lebih dari 0.", "danger")
        return redirect(url_for("inventory.index"))

    if adjustment_type == "in":
        medicine.stock += qty
        flash(f"Stok {medicine.name} berhasil ditambahkan sebanyak {qty}.", "success")

    elif adjustment_type == "out":
        if medicine.stock < qty:
            flash(
                f"Stok {medicine.name} tidak cukup. "
                f"Stok tersedia: {medicine.stock} {medicine.unit}.",
                "danger"
            )
            return redirect(url_for("inventory.index"))

        medicine.stock -= qty
        flash(f"Stok {medicine.name} berhasil dikurangi sebanyak {qty}.", "success")

    else:
        flash("Jenis penyesuaian stok tidak valid.", "danger")
        return redirect(url_for("inventory.index"))

    db.session.commit()
    return redirect(url_for("inventory.index"))


@inventory_bp.route("/delete/<int:medicine_id>", methods=["POST"])
@login_required
@role_required("admin")
def delete(medicine_id):
    medicine = Medicine.query.get_or_404(medicine_id)

    used_count = PrescriptionItem.query.filter_by(medicine_id=medicine.id).count()

    if used_count > 0:
        flash(
            "Obat tidak dapat dihapus karena sudah pernah digunakan dalam resep.",
            "danger"
        )
        return redirect(url_for("inventory.index"))

    db.session.delete(medicine)
    db.session.commit()

    flash("Obat berhasil dihapus.", "success")
    return redirect(url_for("inventory.index"))