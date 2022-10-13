from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("logo.png", 10, 8, 45)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 25)
        # Moving cursor to the right:
        self.cell(110)
        # Printing title:
        self.cell(80, 10, "Diagnostický list", new_x="LMARGIN", new_y="NEXT", align='C')
        # Performing a line break:
        self.ln(2)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"-{self.page_no()}/{{nb}}-", align="C")

data = (
    ("Siemens s.r.o.", "Tel: 800 122 552"),
    ("Oparating company digital Industries", "Tel: 326 516 889"),
    ("www.siemens.cz", "E-mail: servis.cz@siemens.com"),
)


# Instantiation of inherited class
pdf = PDF()
pdf.add_page()

pdf.set_font("helvetica","",8);

for row in data:
    for datum in row:
        pdf.multi_cell(50, 5, datum, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
    pdf.ln(7)

pok = 'border="L,R,B",new_x="RIGHT", new_y="TOP"'

pdf.set_font("helvetica","",10);
pdf.set_line_width(0.25)
pdf.set_draw_color(r=0, g=0, b=0)
pdf.line(x1=0, y1=45, x2=250, y2=45)
pdf.ln(10)
pdf.cell(30,7,"Zakaznik",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"jmeno_firmy",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(7)
pdf.cell(30,7,"Motor",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"1ftnevim6?",border=1,new_x="RIGHT", new_y="TOP")
pdf.ln(7)
pdf.cell(30,7,"Adresa",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"svermova",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(7)
pdf.cell(30,7,"Z",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"/",border=1,new_x="RIGHT", new_y="TOP")
pdf.ln(7)
pdf.cell(30,7,"jmeno",pok)
pdf.cell(45.5,7,"1borec",pok)
pdf.cell(7)
pdf.cell(30,7,"seriove ",pok)
pdf.cell(45.5,7,"54818541541c",pok)
pdf.ln(7)
pdf.cell(30,7,"Tel:",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"712541812",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(7)
pdf.cell(30,7,"Datum",border=1,new_x="RIGHT", new_y="TOP")
pdf.cell(45.5,7,"13.10.2022",border=1,new_x="RIGHT", new_y="TOP")
pdf.ln(7)

DATA=["Stator",47.5,"Izolacni odpor",25,"Mezi. R",25,"Mech. posk.",25,"1820v/28go",47.5,"OK",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,15,2):
    pdf.cell(DATA[i+1],7,DATA[i],pok)
    if i== 6:
        pdf.ln(7)

pdf.ln(7)
DATA1=["Rotor",25,"Mezi. napeti",25,"Mech. posk.",25,"98.8V",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,11,2):
    pdf.cell(DATA1[i+1],7,DATA1[i],pok)
    if i== 4:
        pdf.ln(7)

pdf.ln(7)
DATA2=["Brzda",25,"Elektricky",25,"Mechanicky",25,"15Nm",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,11,2):
    pdf.cell(DATA2[i+1],7,DATA2[i],pok)
    if i== 4:
        pdf.ln(7)
        
pdf.ln(7)
DATA3=["ODMEROVANI",32,"Signaly",25,"Mechanicky",25,"DQ",25,"ERN smi", 32,"OK",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,15,2):
    pdf.cell(DATA3[i+1],7,DATA3[i],pok)
    if i== 6:
        pdf.ln(7)

pdf.ln(7)
DATA4=["KONEKTORY",32,"Signalovy",25,"Silovy",25,"Sig. kab.", 25,"1,5",7,"sro",25,"OK",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,17,2):
    pdf.cell(DATA4[i+1],7,DATA4[i],pok)
    if i== 6:
        pdf.ln(7)

pdf.ln(7)
DATA5=["LOZISKOVY STIT",35,"Zadni",25,"Predni",25,"",35,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,11,2):
    pdf.cell(DATA5[i+1],7,DATA5[i],pok)
    if i== 4:
        pdf.ln(7)
        
pdf.ln(7)
DATAt=["tep. c.",25,"kostra",25,"odpor",25,"",25,"OK",25,"OK",25]
pdf.ln(7)
for i in range(0,11,2):
    pdf.cell(DATAt[i+1],7,DATAt[i],pok)
    if i== 4:
        pdf.ln(7)        

pdf.ln(7)
DATA6=["Loziska",25,"OK",25,]
pdf.ln(7)
for i in range(0,4,2):
    pdf.cell(DATA6[i+1],7,DATA6[i],pok)
    if i== 4:
        pdf.ln(7)        

pdf.ln(7)
DATA7=["Znecisteni",25,"OK",25,]
pdf.ln(7)
for i in range(0,4,2):
    pdf.cell(DATA7[i+1],7,DATA7[i],pok)
    if i== 4:
        pdf.ln(7)  

pdf.output("nic.pdf")

