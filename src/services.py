import asyncio
import pathlib as path
from typing import Dict, List
from src.logger import logger
from src.models.models import CareerCurriculum
from src.data_transform import _parse_pdf_sync
from config import JSON_DIR, PDF_DIR


class CatalogService:
    data: Dict[str, CareerCurriculum]

    def __init__(self):
        logger.debug(JSON_DIR)

    def get_catalog(self):
        return {}


class CurriculumService:
    def __init__(self):
        pass

    async def parse_pdf(self, pdf_file: path.Path) -> CareerCurriculum:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, _parse_pdf_sync, pdf_file)

    async def parse_multiple_pdfs(self, pdf_files: List[path.Path]) -> List[CareerCurriculum]:
        tasks = [self.parse_pdf(pdf_file) for pdf_file in pdf_files]
        return await asyncio.gather(*tasks)

    async def process_all_pdfs_in_directory(self, directory: str = PDF_DIR) -> List[CareerCurriculum]:
        """Process all PDFs in a directory concurrently"""
        pdf_files = list(path.Path(directory).glob("*.pdf"))
        return await self.parse_multiple_pdfs(pdf_files)


catalogService = CatalogService()
curriculumService = CurriculumService()
