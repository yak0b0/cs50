from fpdf import FPDF


class PDF_Information(FPDF):
    def __init__(self, name="John Locke"):
        super().__init__(orientation="P", format="A4")
        self.name = name

    def header(self):
        self.set_font("Arial", size=24)
        self.set_xy(0, 10)
        self.cell(w=210, h=10, txt="CS50 Shirtificate",
                  border=0, align="C", ln=1)

    def add_shirtificate(self):
        self.image("set_8/shirtificate/shirtificate.png",
                   x=(210 - 150) / 2, y=40, w=150)
        self.set_text_color(255, 255, 255)
        self.set_font("Arial", size=20)
        self.set_xy((210 - 100) / 2, 100)
        self.cell(
            w=100, h=10, txt=f"{self.name} took CS50", border=0, align="C")


def get_text_4_pdf():
    name = input("Name: ")
    return PDF_Information(name)


def main():
    pdf = get_text_4_pdf()
    pdf.add_page()
    pdf.header()
    pdf.add_shirtificate()
    pdf.output("set_8/shirtificate/shirtificate.pdf")


if __name__ == "__main__":
    main()
