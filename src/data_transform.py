import asyncio
import pdfplumber
import typing


def bundle_tables(pdf_file: pdfplumber.PDF):
    full_tables = []

    for page in pdf_file.pages:
        pass


def parse_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        pass


def main():
    pass


if __name__ == '__main__':
    main()
