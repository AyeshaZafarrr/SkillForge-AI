from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

styles = getSampleStyleSheet()


def generate_pdf(
    name,
    email,
    career,
    career_score,
    resume_score,
    skills,
    missing_skills,
    certifications
):

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    story = []

    # ===========================
    # Title
    # ===========================

    story.append(
        Paragraph(
            "<b>SkillForge AI Career Report</b>",
            styles["Title"]
        )
    )

    story.append(Spacer(1,20))

    # ===========================
    # User
    # ===========================

    story.append(
        Paragraph(
            f"<b>Name:</b> {name}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Email:</b> {email}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Dream Career:</b> {career}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,15))

        # ===========================
    # AI Scores
    # ===========================

    story.append(
        Paragraph("<b>AI Assessment</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            f"Career Readiness: {career_score}%",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"Resume Score: {resume_score}%",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 15))

    # ===========================
    # Current Skills
    # ===========================

    story.append(
        Paragraph("<b>Current Skills</b>", styles["Heading2"])
    )

    if skills:
        for skill in skills:
            story.append(
                Paragraph(f"• {skill}", styles["Normal"])
            )
    else:
        story.append(
            Paragraph("No skills provided.", styles["Normal"])
        )

    story.append(Spacer(1, 15))

    # ===========================
    # Missing Skills
    # ===========================

    story.append(
        Paragraph("<b>Missing Skills</b>", styles["Heading2"])
    )

    for skill in missing_skills:
        story.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    story.append(Spacer(1, 15))

    # ===========================
    # Certifications
    # ===========================

    story.append(
        Paragraph("<b>Recommended Certifications</b>", styles["Heading2"])
    )

    for cert in certifications:
        story.append(
            Paragraph(f"• {cert}", styles["Normal"])
        )

    story.append(Spacer(1, 20))

        # ===========================
    # AI Recommendations
    # ===========================

    story.append(
        Paragraph("<b>AI Recommendations</b>", styles["Heading2"])
    )

    story.append(
        Paragraph(
            "Focus on improving missing skills and building 2–3 real-world projects.",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Consistency in learning + portfolio building will significantly improve your career score.",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 25))

    # ===========================
    # Build PDF
    # ===========================

    doc.build(story)

    buffer.seek(0)

    return buffer