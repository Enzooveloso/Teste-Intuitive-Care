import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from web_scraping.main import buscar_links_dos_pdfs

import pytest
import requests

class MockResponse:
    @staticmethod
    def get_test_html():
        return '''
            <html>
                <body>
                    <a href="/arquivos/Anexo_I_exemplo.pdf">Anexo I</a>
                    <a href="/arquivos/Anexo_II_exemplo.pdf">Anexo II</a>
                    <a href="/outra_coisa.pdf">Outro</a>
                </body>
            </html>
        '''
    @property
    def content(self):
        return self.get_test_html().encode("utf-8")

@pytest.fixture
def mock_requests_get(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, "get", mock_get)

def test_buscar_links_dos_pdfs(mock_requests_get):
    url = "http://site-fake.com"
    links = buscar_links_dos_pdfs(url)
    assert len(links) == 2
    assert links[0].endswith("Anexo_I_exemplo.pdf")
    assert links[1].endswith("Anexo_II_exemplo.pdf")
