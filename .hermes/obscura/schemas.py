"""JSON Schema tool definitions for the obscura Hermes plugin."""

obscura_fetch_page = {
    "name": "obscura_fetch_page",
    "description": (
        "Fetch a single web page and return its content as HTML, plain text, or a list of links. "
        "Uses obscura headless browser for JavaScript-rendered pages. "
        "Optionally extract only a specific element via CSS selector."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "URL of the page to fetch.",
            },
            "dump": {
                "type": "string",
                "description": "Output format: 'html' for raw HTML, 'text' for plain text, 'links' for all links on the page.",
                "enum": ["html", "text", "links"],
                "default": "text",
            },
            "selector": {
                "type": "string",
                "description": "CSS selector to wait for and extract a specific element from the page.",
            },
            "stealth": {
                "type": "boolean",
                "description": "Enable anti-detection mode to bypass bot protection.",
                "default": False,
            },
        },
        "required": ["url"],
    },
}

obscura_scrape_urls = {
    "name": "obscura_scrape_urls",
    "description": (
        "Scrape multiple URLs in parallel and return structured results. "
        "Use this for batch collection when you have a known list of URLs to process. "
        "Returns JSON or text output per URL."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "urls": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of URLs to scrape in parallel.",
                "minItems": 1,
            },
            "format": {
                "type": "string",
                "description": "Output format: 'json' for structured data, 'text' for plain text.",
                "enum": ["json", "text"],
                "default": "json",
            },
            "concurrency": {
                "type": "integer",
                "description": "Number of parallel workers for scraping.",
                "default": 5,
            },
        },
        "required": ["urls"],
    },
}

obscura_extract_markdown = {
    "name": "obscura_extract_markdown",
    "description": (
        "Fetch a URL and return clean markdown content with scripts, styles, "
        "and navigation stripped. Ideal for reading article content or documentation pages."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "URL of the page to extract markdown from.",
            },
            "stealth": {
                "type": "boolean",
                "description": "Enable anti-detection mode to bypass bot protection.",
                "default": False,
            },
        },
        "required": ["url"],
    },
}

ALL_SCHEMAS = [
    obscura_fetch_page,
    obscura_scrape_urls,
    obscura_extract_markdown,
]
