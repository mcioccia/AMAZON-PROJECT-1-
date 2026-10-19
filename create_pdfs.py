"""Optional PDF rendering: requires reportlab. AI-assisted education, not advice."""
import re
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT=Path(__file__).resolve().parent
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyCustom',fontName='Helvetica',fontSize=10.5,leading=15,spaceAfter=10,textColor=colors.HexColor('#213347')))
styles['Title'].textColor=colors.HexColor('#172a3c')
styles['Title'].fontSize=23; styles['Title'].leading=28

def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(colors.HexColor('#f6a137'));canvas.line(48,43,564,43)
    canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#637489'))
    canvas.drawString(48,30,'FIN 43900 | Amazon | AI-assisted working draft | October 19, 2026')
    canvas.drawRightString(564,30,str(doc.page));canvas.restoreState()

def render(source,target):
    content=(ROOT/'docs'/source).read_text(encoding='utf-8')
    story=[]
    for block in content.split('\n\n'):
        block=block.strip()
        if not block:continue
        block=block.replace('\u2014','-').replace('\u2013','-').replace('\u2019',"'")
        style=styles['Title'] if block.startswith('# ') else styles['BodyCustom']
        if block.startswith('# '):block=block[2:]
        text=escape(block)
        text=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',text)
        text=text.replace('\n','<br/>')
        story.append(Paragraph(text,style));story.append(Spacer(1,4))
    SimpleDocTemplate(str(ROOT/'docs'/target),pagesize=(612,792),rightMargin=48,leftMargin=48,topMargin=45,bottomMargin=58,title=target.replace('.pdf',''),author='AI-assisted coursework draft').build(story,onFirstPage=footer,onLaterPages=footer)

if __name__=='__main__':
    for source,target in [('research-evolution.md','Research-Evolution.pdf'),('decision-memo.md','Decision-Memo.pdf'),('validation-and-ai-use.md','Validation-and-AI-Use.pdf')]:
        render(source,target);print(target)
