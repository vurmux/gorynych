from ..core import module

class Scraper(Module):
    """
    """

    # Module metainfo
    meta = {
        "name": "",
        "author": "",
        "supertype": None,
        "type": "scraper",
        "required_keys": [],
        "short_description": "",
        "long_description": "",
        "tags": []
    }

    options = {}

    def __init__(self):
        super(Scraper, self).__init__()

        # Extracted data
        self.extracted_data = {
            'type': '',
            'steps': []
        }
        self.max_steps = 5

    def run(self, *args, **kwargs):
        self.setup(*args, **kwargs)
        for _ in range(self.max_steps):
            result = self.step()
            self.extracted_data['steps'].append(result)
            self._update_step_state()
            self.freeze()
        self.finish()
