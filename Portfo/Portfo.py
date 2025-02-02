import reflex as rx
from rxconfig import config


# 🎭 State
class State(rx.State):
    """The app state."""

    def button_clicked(self):
        print("🎉 Button clicked!")
        return rx.window_alert("🚀 Great! You clicked the button.")

    # 🌟 Navbar Component

class Navbar:
    def __init__(self):
        self.contact_links = rx.hstack(
            rx.link(
                rx.image(tag="mail", size=24),
                href="mailto:treshlol202@gmail.com",
                is_external=True
            ),
            rx.link(
                rx.icon(tag="github", size=24),  # Fixed: size should be an integer
                href="https://github.com/MehdiDinari",
                is_external=True
            ),
            rx.link(
                rx.icon(tag="linkedin", size=24),  # Fixed: size should be an integer
                href="https://www.linkedin.com/in/mehdi-dinari-b0487a2a9/",
                is_external=True
            ),
            gap="20px",
            font_size="18px",
            font_weight="bold",
        )

        self.nav_links = rx.hstack(
            rx.link("🏠 Home", href="#home"),
            rx.link("⚙️ Tech Stack", href="#tech"),
            rx.link("📌 Projects", href="#projects"),
            rx.link("📞 Contact", href="#contact"),
            gap="40px",
            font_size="18px",
            font_weight="bold",
        )

        self.navbar = rx.hstack(
            self.contact_links,
            rx.spacer(),
            self.nav_links,
            rx.spacer(),
            align_items="center",
            justify_content="space-between",
            width="100%",
            height="80px",
            background_color=rx.color_mode_cond("#ffffff", "#1a1a1a"),
            padding_x="60px",
            position="fixed",
            top="0",
            left="0",
            z_index="1000",
            box_shadow="0px 4px 8px rgba(0,0,0,0.1)",
        )


    def build(self):
        return self.navbar


# 🎭 Welcome Section
def welcome_section():
    return rx.vstack(
        rx.heading("🌍 Welcome to My Portfolio!", font_size="42px", font_weight="bold"),
        rx.text("Explore my work, skills, and projects.", font_size="20px", text_align="center"),
        padding="80px 20px",
        align_items="center",
        id="home",
        background="linear-gradient(135deg, #007bff 0%, #6610f2 100%)",
        color="white",
        border_radius="10px",
        box_shadow="0px 4px 10px rgba(0, 0, 0, 0.2)",
        width="80%",
        max_width="800px",
    )


# 🎭 Main Section (Nom et Expertise)
class Main:
    def __init__(self):
        self.box = rx.box(width="100%")
        self.name = rx.hstack(
            rx.heading(
                "👋 Hi - I'm Mehdi Dinari",
                font_size="3rem",
                font_weight="bold",
                color=rx.color_mode_cond("#222", "#fff"),
            ),
            align_items="center",
            justify_content="center",
        )

        self.expertise = rx.text(
            "🐍 Python Passionate | 📊 Data Scientist | 📈 Data Analyst | 🧠 Problem Solver",
            font_size="22px",
            font_weight="medium",
            text_align="center",
            color=rx.color_mode_cond("#444", "#ddd"),
        )

    def build(self):
        return rx.vstack(
            self.name,
            self.expertise,
            align_items="center",
            justify_content="center",
            padding="60px",
        )


# 🛠️ Tech Stack avec Logos
def tech_stack():
    techs = [
        ("Python", "/logos/python.svg"),
        ("NumPy", "/logos/numpy.svg"),
        ("Pandas", "/logos/pandas.png"),
        ("Scikit Learn", "/logos/sk.png"),
        ("TensorFlow", "/logos/TF.png"),
        ("PyTorch", "/logos/pytorch.svg"),
        ("FastAPI", "/logos/fastapi.svg"),
        ("Django", "/logos/django.svg"),
        ("Flask", "/logos/flask.svg"),
    ]

    return rx.vstack(
        rx.heading("🛠️ Technologies & Frameworks", font_size="26px", font_weight="bold", id="tech"),
        rx.hstack(
            *[
                rx.box(
                    rx.image(src=logo, width="50px", height="50px"),
                    rx.text(name, font_size="18px", font_weight="bold"),
                    align="center",
                    padding="10px",
                )
                for name, logo in techs
            ],
            gap="20px",
            wrap="wrap",
            justify="center"
        ),
        align_items="center",
        padding="40px",
    )


# 📌 Projects Section sous forme de Cartes
def projects():
    project_list = [
        ("Diabetes Prediction", "/projects/Diabete.png", "https://github.com/MehdiDinari/Diabetes-Prediction-System"),
        ("Loan Calculator", "/projects/Loan.png", "https://github.com/MehdiDinari/Loan-Calculator"),
        ("Email Filter", "/projects/Email.png", "https://github.com/MehdiDinari/Email-Filter"),
        ("House Price Prediction", "/projects/House.png", "https://github.com/MehdiDinari/House-price-prediction"),
        ("Predict Fly Price", "/projects/Fly.png", "https://github.com/MehdiDinari/Predict-Fly-Price"),
        ("AimTrainer", "/projects/Aim.png", "https://github.com/MehdiDinari/AimTrainer"),
    ]

    return rx.vstack(
        rx.heading("🚀 Projects", font_size="26px", font_weight="bold", id="projects"),
        rx.grid(
            *[
                rx.box(
                    rx.image(src=img, width="100%", height="180px", border_radius="8px"),
                    rx.heading(name, font_size="20px", font_weight="bold", margin_top="10px", color="black"),
                    rx.link("🔗 View on GitHub", href=link, is_external=True, color="light-blue"),
                    padding="20px",
                    border="2px solid rgba(0, 0, 0, 0.1)",
                    border_radius="8px",
                    box_shadow="0px 4px 10px rgba(0, 0, 0, 0.1)",
                    _hover={"transform": "scale(1.05)", "transition": "0.3s"},
                    width="300px",
                    background_color="gray",
                    align="center",
                )
                for name, img, link in project_list
            ],
            columns="3",
            spacing="3",
            justify="center",
        ),
        align_items="center",
        padding="40px",
    )


# 📞 Contact Section
def contact():
    return rx.vstack(
        rx.heading("📞 Contact Me", font_size="28px", font_weight="bold", id="contact", margin_bottom="15px"),

        rx.box(
            rx.icon(tag="mail", size=20, color="white"),
            rx.text("Email: ", font_size="18px", font_weight="medium"),
            rx.link("treshlol202@gmail.com", href="mailto:treshlol202@gmail.com", is_external=True, color="black"),
            display="flex",
            align_items="center",
            gap="8px",
        ),

        rx.box(
            rx.icon(tag="github", size=20, color="white"),
            rx.text("GitHub: ", font_size="18px", font_weight="medium"),
            rx.link("MehdiDinari", href="https://github.com/MehdiDinari", is_external=True, color="black"),
            display="flex",
            align_items="center",
            gap="8px",
        ),

        rx.box(
            rx.icon(tag="linkedin", size=20, color="white"),
            rx.text("LinkedIn: ", font_size="18px", font_weight="medium"),
            rx.link("Mehdi Dinari", href="https://www.linkedin.com/in/mehdi-dinari-b0487a2a9/", is_external=True,
                    color="#black"),
            display="flex",
            align_items="center",
            gap="8px",
        ),

        align_items="center",
        padding="40px",
        background_color=rx.color_mode_cond("#f9f9f9", "#222"),
        border_radius="10px",
        box_shadow="0px 4px 10px rgba(0, 0, 0, 0.1)",
        width="80%",
        max_width="600px",
    )


# 📜 Main Page
@rx.page(route="/")
def landing() -> rx.Component:
    return rx.vstack(
        Navbar().build(),
        rx.spacer(size="40px"),
        welcome_section(),
        Main().build(),
        tech_stack(),
        projects(),
        contact(),
        min_height="100vh",
        align_items="center",
        justify_content="center",
        background_color=rx.color_mode_cond("#f8f9fa", "#1a1a1a"),
        padding_bottom="60px",
    )


# Reflex App Setup
app = rx.App()
app.add_page(landing)
