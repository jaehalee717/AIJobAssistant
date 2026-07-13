"""
word_helper.py
AIJobAssistant
Version : v1.0.0

Common helper functions for Microsoft Word.
"""

from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE


def add_hyperlink(paragraph, text: str, url: str):
    """
    Add a clickable hyperlink to a Word paragraph.

    Parameters
    ----------
    paragraph : docx.paragraph.Paragraph
    text : str
        Display text.
    url : str
        Hyperlink target.
    """

    if not url:
        paragraph.add_run(text)
        return

    part = paragraph.part

    relationship_id = part.relate_to(
        url,
        RELATIONSHIP_TYPE.HYPERLINK,
        is_external=True,
    )

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(
        qn("r:id"),
        relationship_id,
    )

    run = OxmlElement("w:r")

    run_properties = OxmlElement("w:rPr")

    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")

    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")

    run_properties.append(color)
    run_properties.append(underline)

    run.append(run_properties)

    text_element = OxmlElement("w:t")
    text_element.text = text

    run.append(text_element)

    hyperlink.append(run)

    paragraph._p.append(hyperlink)