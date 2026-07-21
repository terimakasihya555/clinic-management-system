import os
import sys
import time
import shutil
import threading
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import messagebox


def get_base_dir():
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parent


BASE_DIR = get_base_dir()
os.chdir(BASE_DIR)


def ensure_runtime_folders():
    for folder in ["instance", "logs", "backups"]:
        Path(folder).mkdir(exist_ok=True)


def ensure_env_file():
    env_file = Path(".env")
    env_example = Path(".env.example")

    if not env_file.exists() and env_example.exists():
        shutil.copy(env_example, env_file)


def set_default_environment():
    os.environ.setdefault("APP_VERSION", "1.0.0")
    os.environ.setdefault("SECRET_KEY", "change-this-secret-key")
    os.environ.setdefault("DATABASE_URL", "sqlite:///clinic.sqlite")
    os.environ.setdefault("ENABLE_IP_RESTRICTION", "False")
    os.environ.setdefault("ALLOWED_IP_PREFIXES", "127.,192.168.,10.")
    os.environ.setdefault("RATE_LIMIT_MAX_REQUESTS", "200")
    os.environ.setdefault("RATE_LIMIT_WINDOW_SECONDS", "60")
    os.environ.setdefault("SESSION_TIMEOUT_MINUTES", "30")
    os.environ.setdefault("SESSION_COOKIE_SECURE", "False")


def open_browser():
    time.sleep(2)
    webbrowser.open("http://127.0.0.1:5000")


def ensure_default_users(app):
    from werkzeug.security import generate_password_hash

    from clinic_app.models import db
    from clinic_app.models.user import User

    with app.app_context():
        if User.query.count() > 0:
            return

        users = [
            User(
                name="Admin Klinik",
                email="admin@clinic.local",
                password_hash=generate_password_hash("admin123"),
                role="admin"
            ),
            User(
                name="Doctor Klinik",
                email="doctor@clinic.local",
                password_hash=generate_password_hash("doctor123"),
                role="doctor"
            ),
            User(
                name="Receptionist Klinik",
                email="reception@clinic.local",
                password_hash=generate_password_hash("reception123"),
                role="receptionist"
            ),
        ]

        db.session.add_all(users)
        db.session.commit()


def run_server():
    try:
        ensure_runtime_folders()
        ensure_env_file()
        set_default_environment()

        from waitress import serve

        from clinic_app import create_app
        from clinic_app.models import db, load_models

        app = create_app()

        with app.app_context():
            load_models()
            db.create_all()

        ensure_default_users(app)

        threading.Thread(target=open_browser, daemon=True).start()

        serve(
            app,
            host="127.0.0.1",
            port=5000,
            threads=4
        )

    except Exception as error:
        messagebox.showerror(
            "Clinic Management System Error",
            f"Application failed to start:\n\n{error}"
        )


def stop_application(root):
    confirm = messagebox.askyesno(
        "Stop Application",
        "Are you sure you want to stop Clinic Management System?"
    )

    if confirm:
        root.destroy()
        os._exit(0)


def create_control_window():
    root = tk.Tk()
    root.title("Clinic Management System")
    root.geometry("420x230")
    root.resizable(False, False)

    title = tk.Label(
        root,
        text="Clinic Management System",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=(25, 5))

    status = tk.Label(
        root,
        text="Application is running.",
        font=("Arial", 11)
    )
    status.pack(pady=5)

    url = tk.Label(
        root,
        text="http://127.0.0.1:5000",
        font=("Arial", 10),
        fg="blue"
    )
    url.pack(pady=5)

    open_button = tk.Button(
        root,
        text="Open in Browser",
        width=22,
        command=lambda: webbrowser.open("http://127.0.0.1:5000")
    )
    open_button.pack(pady=(15, 5))

    stop_button = tk.Button(
        root,
        text="Stop Application",
        width=22,
        command=lambda: stop_application(root)
    )
    stop_button.pack(pady=5)

    root.protocol("WM_DELETE_WINDOW", lambda: stop_application(root))

    root.mainloop()


def main():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    create_control_window()


if __name__ == "__main__":
    main()