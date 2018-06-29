from ..core import module

class Harvester(Module):
    """
    """

    # Module metainfo
    meta = {
        "name": "",
        "author": "",
        "supertype": None,
        "type": "harvester",
        "required_keys": [],
        "short_description": "",
        "long_description": "",
        "tags": []
    }

    options = {}

    def __init__(self):
        super(Harvester, self).__init__()

        # Extracted graph
        self.extracted_graph = None

        # Max number of steps
        self.max_steps = 5

    def run(self, *args, **kwargs):
        self.setup(*args, **kwargs)
        for _ in range(self.max_steps):
            result = self.step(*args, **kwargs)
            self.extracted_graph.merge(result)
            self._update_step_state()
            self.freeze()
        self.finish()
