import json
import os
from turtle import fillcolor
from fpdf import FPDF

# Find JSON file
CurrentDirectory = os.getcwd()
print(CurrentDirectory)
jsonFile = "%s/%s" % (CurrentDirectory, "personal_details.json")
jsonData = {}

# Read JSON file and store in jsonData
with open(jsonFile) as data_file:
    jsonData = json.load(data_file)

# Set JSON Data # personal details
firstName = jsonData["First Name"]
lastName = jsonData["Last Name"]
birthday = jsonData["Birthday"]
age = jsonData["Age"]
sex = jsonData["Sex"]
contactNo = jsonData["Contact Number"]
# Social media accounts
gmail = jsonData["Gmail"]
facebook = jsonData["Facebook Account"]
instagram = jsonData["Instagram Account"]
github = jsonData["Github Account"]
# Forte
expertise = jsonData["Expertise"]
forte = jsonData["Forte"]
appsUsed = jsonData["Applications Using"]
# Skills
skills1a = jsonData["Additional Skills"][0]
skills1b = jsonData["Additional Skills"][1]
skills1c = jsonData["Additional Skills"][2]
# Experiences
olCom = jsonData["Online Commissions"][0]
olCom1 = jsonData["Online Commissions"][1]
olCom2 = jsonData["Online Commissions"][2]
olCom3 = jsonData["Online Commissions"][3]
contest = jsonData["Digital Art Online Contest"]
# Education
seniorH = jsonData["Senior High School"]
seniorH1a = jsonData["SHS description"][0]
seniorH1b = jsonData["SHS description"][1]
college = jsonData["College"]
college1 = jsonData["College description1"]
college2 = jsonData["College description2"]

# Create PDF
pdf = FPDF("P", "cm", "A4")
pdf.add_page()

# Header
pdf.set_font("times", "B", 20)
pdf.set_fill_color(200,144,117)
pdf.cell(0, 5, "              " + firstName + " " + lastName, ln=1, align="L", fill=1)
pdf.image('idpic.jpg', 15, 1, 5)


pdf.cell(0,1, "            ", align="L", ln=1)
pdf.set_font("times", "B", 15)
pdf.set_text_color(200,144,117)
pdf.set_fill_color(0,0,0)
pdf.cell(0,1, "Personal Information", align="R", ln=1, fill=1)
pdf.set_fill_color(200,144,117)
pdf.set_text_color(0,0,0)
pdf.cell(9,0.7, "Experiences (February 2020 - Present)", align="L", fill=1)

pdf.set_font("times", "", 15)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "Birthday: " + birthday, align="R", ln=1)
pdf.set_font("times", "B", 15)
pdf.cell(0,0.75, "   Online Commissions", align="L")
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "Age: " + age, align="R", ln=1)
pdf.cell(0,0.75, "      " + olCom2, align="L")
pdf.cell(0,0.75, "Sex: " + sex, align="R", ln=1)
pdf.cell(0,0.75, "      " + olCom3, align="L")
pdf.cell(0,0.75, "Contact Number: " + contactNo, align="R", ln=1)
pdf.cell(0,0.75, "      " + olCom, align="L", ln=1)
pdf.cell(0,0.75, "      " + olCom1, align="L", ln=1)
pdf.cell(0,0.5, "         ", align="R", ln=1)

pdf.set_font("times", "B", 15)
pdf.cell(0,0.75, "   Digital Art Online Contest", align="L", ln=1)
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "      " + contest, align="L", ln=1)


pdf.set_font("times", "B", 15)
pdf.set_text_color(200,144,117)
pdf.set_fill_color(0,0,0)
pdf.cell(0,1, "Social Accounts", align="R", ln=1, fill=1)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(200,144,117)
pdf.cell(8,0.7, "Education (College 2021 - Present)", align="L", fill=1)

pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "Gmail: " + gmail, align="R", ln=1)
pdf.set_font("times", "B", 15)
pdf.cell(0,0.75, "        ", align="L")
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "Facebook: " + facebook, align="R", ln=1)
pdf.set_font("times", "B", 15)
pdf.cell(0,0.75, "    " + college, align="L")
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "Instagram: " + instagram, align="R", ln=1)
pdf.set_font("times", "", 14)
pdf.cell(0,0.75, college1, align="L")
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, "GitHub: " + github, align="R", ln=1)
pdf.set_font("times", "", 14)
pdf.cell(0,0.75, "  " + college2, align="L")
pdf.cell(0,1, "         ", align="R", ln=1)

pdf.set_font("times", "B", 15)
pdf.set_text_color(200,144,117)
pdf.set_fill_color(0,0,0)
pdf.cell(0,1, "Other Skills", align="R", ln=1, fill=1)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(200,144,117)
pdf.cell(8.5,0.7, "Education (Senior High 2018 - 2020)", align="L", fill=1)

pdf.set_font("times", "", 15)
pdf.cell(0,0.75, skills1a, align="R", ln=1)
pdf.cell(0,0.75, skills1b, align="R", ln=1)
pdf.set_font("times", "B", 15)
pdf.cell(0,0.75, "    " + seniorH, align="L")
pdf.set_font("times", "", 15)
pdf.cell(0,0.75, skills1c, align="R", ln=1)
pdf.set_font("times", "", 14)
pdf.cell(0,0.75, seniorH1a, align="L", ln=1)
pdf.cell(0,0.75, seniorH1b, align="L")
pdf.cell(0,1, "         ", align="R", ln=1)

pdf.set_font("times", "B", 15)
pdf.set_text_color(0,0,0)
pdf.set_fill_color(200,144,117)
pdf.cell(0,1, "Professional Summary", align="C", ln=1, fill=1)
pdf.set_font("times", "", 15)
pdf.set_text_color(0,0,0)
pdf.cell(0,0.75, "     I have been in the field of arts since 2018 and my expertise is in " + expertise + " and my", align="L", ln=1)
pdf.cell(0,0.75, "forte is creating " + forte + " and highlighting small details.", align="L", ln=1)

# PDF output
pdf.output("GALVEZ_LARAMARIEISABEL.pdf")