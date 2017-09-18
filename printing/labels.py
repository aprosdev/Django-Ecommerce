from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing, Line
from reportlab.graphics import renderPDF
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak, Spacer
from reportlab.lib import colors
from reportlab.graphics.barcode.eanbc import Ean13BarcodeWidget
from reportlab.platypus import Flowable

from defaults.stylesheets import stylesheet, stylesheet_washinglabels, stylesheet_labels

from io import BytesIO

import textwrap

def simple_label_38x90(text):
    '''
    return a simple label, filled with the given text in a default font
    '''
    buffer = BytesIO()

    margin = 0*mm
    doc = SimpleDocTemplate(buffer,
            rightMargin=margin,
            leftMargin=margin,
            topMargin=margin,
            bottomMargin=margin,
            pagesize=(90*mm, 38*mm))

    elements = []
    styles = stylesheet_labels()

    elements.append(Paragraph(text, styles['BodyTextSmall']))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


def stock_label_38x90(materials):
    '''
    return label pdf for a simple box sku label
    '''
    buffer = BytesIO()

    margin = 5*mm
    doc = SimpleDocTemplate(buffer,
            rightMargin=margin,
            leftMargin=margin,
            topMargin=margin,
            bottomMargin=margin,
            pagesize=(90*mm, 38*mm))

    elements = []
    styles = stylesheet()

    for mat in materials:
        elements.append(Paragraph(mat.name, styles['BodyText']))
        elements.append(Paragraph('sku: {}'.format(mat.sku), styles['BodyText']))
        elements.append(PageBreak())

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf   


class BarCode(Flowable):
    # Based on https://stackoverflow.com/questions/18569682/use-qrcodewidget-or-plotarea-with-platypus
    # and https://stackoverflow.com/questions/38894523/apply-alignments-on-reportlab-simpledoctemplate-to-append-multiple-barcodes-in-n
    def __init__(self, value="1234567890", ratio=1):
        # init and store rendering value
        Flowable.__init__(self)
        self.value = value
        self.ratio = ratio

    def wrap(self, availWidth, availHeight):
        # Make the barcode fill the width while maintaining the ratio
        self.width = availWidth
        self.height = self.ratio * availWidth
        return self.width, self.height

    def draw(self):
        # Flowable canvas
        bar_code = Ean13BarcodeWidget(value=self.value)
        bounds = bar_code.getBounds()
        bar_width = bounds[2] - bounds[0]
        bar_height = bounds[3] - bounds[1]
        w = float(self.width)
        h = float(self.height)
        d = Drawing(w, h, transform=[w / bar_width, 0, 0, h / bar_height, 0, 0])
        d.add(bar_code)
        renderPDF.draw(d, self.canv, 0, 0)


def washinglabel(product):
    '''
    Return washinglabel pdf for a product with width: 3cm, length: 10cm
    Washinglabel contains:
    - barcode ean
    - umbrella_product name
    - colour
    - size
    - sku
    '''

    product_title = str(product.umbrella_product)
    product_colour = 'Colour: {}'.format(product.umbrella_product.colour)
    product_size = 'Size: {}'.format(product.product_model.size)
    product_sku = product.sku
    product_ean = product.ean_code
    
    buffer = BytesIO()

    margin = 1*mm
    doc = SimpleDocTemplate(buffer,
            rightMargin=margin,
            leftMargin=margin,
            topMargin=margin,
            bottomMargin=margin,
            pagesize=(30*mm, 100*mm))

    elements = []
    styles = stylesheet_washinglabels()

    ## Hack to add horizontal line
    style = TableStyle([
         ("LINEABOVE", (0,0), (-1,-1), 1, colors.black),
       ])
    table = Table([''])
    table.setStyle(style)
    elements.append(table)    

    elements.append(Spacer(30*mm, 15*mm))
    elements.append(BarCode(value=product_ean, ratio=0.9))
    elements.append(Spacer(30*mm, 10*mm))
    elements.append(Paragraph(product_title, styles['Bold']))
    elements.append(Paragraph(product_colour, styles['NormalSmall']))
    elements.append(Paragraph(product_size, styles['NormalSmall']))
    elements.append(Paragraph(product_sku, styles['NormalSmall']))

    doc.build(elements)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf 


def box_barcode_label(product):
    '''
    Return barcode pdf for a product barcode on the box including:
    - ean-code
    - umbrella product name
    - colour
    - size
    - sku
    label size: 35x89mm
     '''
    product_ean = product.ean_code
    product_title = product.umbrella_product.__unicode__()
    product_colour = product.umbrella_product.colour
    product_size = product.product_model.size
    product_sku = product.sku

    buffer = BytesIO()

    page_real_height = 35*mm  ## Cheating to fix layout, real value 38
    page_real_width = 89*mm  ## Cheating to fix layout, real value 90
    page_margin = 5*mm
    line_height = 2.8*mm
    font_size = 8

    p = canvas.Canvas(buffer)
    p.setPageSize((page_real_width, page_real_height))

    p.setLineWidth(.3)
    col1 = 0 
    col2 = page_real_width / 2 + page_margin

    ori_string_top_location = page_real_height - page_margin

    ## Left col
    string_top_location = ori_string_top_location - 10*mm

    ean = eanbc.Ean13BarcodeWidget(product_ean)
    ean.height = page_real_height
    ean.width = page_real_width / 2

    d = Drawing()
    d.add(ean)
    renderPDF.draw(d, p, page_margin, page_margin)

    ## Right col info
    p.setFont('Helvetica', font_size)
    to_draw_strings = textwrap.fill(product_title, 28).split('\n')
    to_draw_strings.append(u'Colour: {}'.format(product_colour))
    to_draw_strings.append(u'Size: {}'.format(product_size))
    to_draw_strings.append(u'{}'.format(product_sku))

    for s in to_draw_strings:
        p.drawString(col2, string_top_location, s)
        string_top_location -= line_height

    ## new page 
    p.showPage()

    p.save()
    pdf = buffer.getvalue()

    return pdf