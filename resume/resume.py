from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

# Header
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Abhishek Kumar Kamat", ln=True, align="C")
pdf.set_font("Arial", size=11)
pdf.cell(0, 8, "New Area, Jakkanpur, Laxmi Market, Kedar Nath Gali, Patna, Bihar - 800001", ln=True, align="C")
pdf.cell(0, 8, "+91 9693964596 | abhishekkamat142@gmail.com", ln=True, align="C")
pdf.cell(0, 8, "LinkedIn: linkedin.com/in/abhishek-kamat | GitHub: github.com/kamat-abhi", ln=True, align="C")
pdf.ln(10)

# Sections
def add_section(title, content):
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, title, ln=True)
    pdf.set_font("Arial", size=11)
    for line in content.split("\n"):
        pdf.multi_cell(0, 8, line)
    pdf.ln(5)

# Add sections
add_section("Professional Summary", 
    "Motivated and detail-oriented Computer Science graduate with a strong foundation in JavaScript and backend development. "
    "Passionate about building robust applications from scratch and solving real-world problems through code. Seeking an opportunity "
    "to contribute and grow in a dynamic tech environment.")

add_section("Skills", 
    "- Programming Languages: C, C++, JavaScript (very proficient)\n"
    "- Web Development: HTML, CSS, Node.js\n"
    "- Problem Solving\n"
    "- Tools & Platforms: Git, GitHub, VS Code")

add_section("Education", 
    "B.Tech - Computer Science & Engineering (Currently in 5th Semester)\n"
    "Rashtrakavi Ramdhari Singh Dinker College of Engineering\n"
    "GPA: 7.8")

add_section("Projects", 
    "- Auth Service: GitHub: https://github.com/kamat-abhi/Auth_Service\n"
    "Implemented an authentication service for user login and registration using JavaScript.\n\n"
    "- URL Shortener: GitHub: https://github.com/kamat-abhi/Url-shorten\n"
    "Built a web application to shorten long URLs using JavaScript.\n\n"
    "- AirTicketBookingService: GitHub: https://github.com/kamat-abhi/AirTicketBookingService\n"
    "Developed a dummy booking service and store data using MySql.\n\n"
    "- Reminder Service: GitHub: https://github.com/kamat-abhi/ReminderService\n"
    "Created a task reminder service using JavaScript and Node.js with email notifications.")

# Save PDF
pdf.output("Abhishek_Kamat_Updated_Resume.pdf")
