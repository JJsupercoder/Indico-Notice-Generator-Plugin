from __future__ import unicode_literals
from setuptools import setup

setup(
    name="indico-pdf-generator",
    version="0.1",
    packages=["indico_pdf_generator"],
    zip_safe=False,
    include_package_data=True,
    package_data={
        'indico_pdf_generator': ['templates/indico_pdf_generator/*.html', 'templates/*.html'],
    },
    platforms="any",
    install_requires=["indico>=2.0", "Flask"],
    entry_points={
        "indico.plugins": {
            "indico_pdf_generator = indico_pdf_generator:PDFGeneratorPlugin",
        },
    },
)
