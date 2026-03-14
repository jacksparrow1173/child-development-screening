from reportlab.platypus import SimpleDocTemplate,Paragraph,Image,Spacer
from reportlab.lib.styles import getSampleStyleSheet


def create_report(student,result,chart):

    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Developmental Screening Report",styles['Title']))

    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"Name: {student['name']}",styles['Normal']))

    elements.append(Paragraph(f"Age (months): {student['age_months']}",styles['Normal']))

    elements.append(Paragraph(f"Gender: {student['gender']}",styles['Normal']))

    elements.append(Paragraph(f"School: {student['school']}",styles['Normal']))

    elements.append(Spacer(1,20))

    elements.append(Paragraph(f"Risk Level: {result['risk']}",styles['Normal']))

    elements.append(Paragraph(f"Risk Percentage: {round(result['percent'],2)}%",styles['Normal']))

    elements.append(Paragraph(f"Total Score: {result['total']}",styles['Normal']))

    elements.append(Spacer(1,20))

    elements.append(Image(chart,width=400,height=250))

    filename = "report.pdf"

    pdf = SimpleDocTemplate(filename)

    pdf.build(elements)

    return filename