from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "M.UmerCV.png"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Muhammad Umer"
PAGE_ICON = ":wave:"
NAME = "Muhammad Umer"
DESCRIPTION = """
Aspiring progressive Electrical/Data Engineer seeking growth and professional development opportunities.
"""
EMAIL = "umerjalal100@gmail.com"
PHONE = "+92-3494965022"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@The_Mindful_Scholar",
    "LinkedIn": "https://www.linkedin.com/in/muhammad-umer-8aba4a125/",
    #"GitHub": "https://github.com/abbasrational",
}
PROJECTS = {
    "🏆 Solar and Wind Integration for Sustainable Energy Development in Pakistan": "https://abbasrational-umer-energy-report-app-hnky8l.streamlit.app/",
    "🏆 Data visualization and analytics for the direct start of DC machine": "https://abbasrational-ac-machine-drive-p1-app-e0x5ey.streamlit.app/",
    "🏆 An Intelligent Web Dashboard for Transmission Line Faults Analysis": "https://abbasrational-shabbir-py-0fzfic.streamlit.app/",
    
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.header(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    st.write ("📱", PHONE)
    


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- JOB 1
st.write("🎓", "**MS Electrical Power Engineering  | National University of Sciences & Technology (NUST) Islamabad**")
st.write("09/2022 - Present (CGPA: 3.2)")
st.write('\n')
# --- JOB 2
st.write('\n')
st.write("🎓", "**PGD Data Science With Artificial Intelligence | NED University of Engineering & Technology Karachi**")
st.write("11/2021 - 11/2022 (CGPA: 3.7)")

# --- JOB 3
st.write('\n')
st.write("🎓", "**BS Electrical Electronics Engineering | COMSATS Lahore**")
st.write("02/2013 - 08/2017 (CGPA:2.3)")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Work Experience ")
st.markdown("👨🏼‍🔧","**Trainee Engineer | Engineering Development Board**")
#st.write("**Trainee Engineer**")
st.write("03/2020 - 03/2022")
st.write(
    """
- ✔️ Conducting predictive trade analysis for Pakistan and key international markets (China, USA, Afghanistan, Sri Lanka, etc.). 
- ✔️ Applying Data Science techniques to automate and streamline Pakistan Bureau of Statistics (PBS) Import & Export data.
- ✔️ Performing sectoral analysis for Home Appliances, Fans, and Power Equipment.
- ✔️ Collaborating as a team member on a joint industrial survey program between EDB and Pakistan Business Council (PBC), focused on enhancing the competitiveness of Pakistan's Domestic Fan Industry (2020-21). 
- ✔️ Contributing to the development of the National Industrial Policy (NIP) by conducting specialized research and analysis for sectors such as Transformers, Pumps & Motors, Energy Meters, and Cables & Conductors. 
"""
)
st.write('\n')
st.markdown("👨‍💻","**Network Support Engineer | PTCL (Pakistan Telecommunication Company Ltd)**")
#st.write("**Network Support Engineer**")
st.write("10/2017 - 04/2018") 
st.write(
    """
- ✔️ Visualized and understand the working of PDH, SDH, DWDM and MPLS technologies of transmission. 
- ✔️ Performed different tasks regarding network device discovery, monitoring, performance analysis, cable cut issues and El configuration under NMS ZTE E300, NMS Huawei U2000 and NMS Fiber Home OTNM 2000.
- ✔️ Performed multiple tasks on Optical Time Domain Reflectometer (OTDR) including splice losses, maximum attenuation & power of an optical signal. 
- ✔️ Identify and analyze faults of power banks. 
- ✔️ Consolidate and compile month-wise ITR Bandwidth Utilization's data for 10G Aggregation Nodes and ZTE 2.5G MSAGs
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: C/C++, Python.
- 📊 Data Visulization: MS Excel, Plotly Express.
- 📚 Softwares: PSCAD, MATLAB, LT Spice.
- 🏗  Project Managment: Planning & scheduling, Technical Report Writing, Customs Tariff, Policy Making, Sector/Business development studies.
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
