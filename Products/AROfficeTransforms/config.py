PROJECTNAME='AROfficeTransforms'

TRANSFORMS = [
  "word_to_text",
  "word_to_html",
  "excel_to_html",
  "ppt_to_html",
  "ooo_to_html",
  "oo2_to_html",
  "pdf_to_html",
  "zip_to_text",
  "docx_to_html"
]

try:
    # Plone 4 and higher
    import plone.app.upgrade
    PLONE_VERSION = 4
except ImportError:
    PLONE_VERSION = 3
