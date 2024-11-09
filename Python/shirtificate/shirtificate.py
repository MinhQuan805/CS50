from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "B", 48)
        self.cell(0, 60, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    logo = input("Logo: ")
    get_shirt(logo)


def get_shirt(logo):
   pdf = PDF()
   pdf.add_page(orientation="portrait", format="A4")
   pdf.set_font("Helvetica", size=24)
   pdf.set_text_color(0, 0, 0)
   pdf.cell(0, 213, f"{logo} Took CS50", align = "C")
   pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
