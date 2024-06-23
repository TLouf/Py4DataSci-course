import sys
from pathlib import Path

from nbconvert.exporters import NotebookExporter
from nbconvert.preprocessors import TagRemovePreprocessor
from traitlets.config import Config


def clean(path, config, suffix="-sol"):
    exporter = NotebookExporter(config=config)
    exporter.register_preprocessor(TagRemovePreprocessor(config=config), True)

    # Configure and run our exporter - returns a tuple - first element with ipynb,
    # second with notebook metadata
    for p in Path(path).glob(f"**/*{suffix}.ipynb"):
        output = exporter.from_filename(str(p))
        p.with_stem(p.stem.removesuffix(suffix)).write_text(output[0])


if __name__ == "__main__":
    path = sys.argv[1]
    # Setup config
    c = Config()
    # Configure tag removal - be sure to tag your cells to remove  using the
    # words remove_cell to remove cells. You can also modify the code to use
    # a different tag word
    c.TagRemovePreprocessor.remove_cell_tags = ("hide-cell",)
    c.TagRemovePreprocessor.remove_all_outputs_tags = ("hide-output",)
    c.TagRemovePreprocessor.remove_input_tags = ("hide-input",)
    c.TagRemovePreprocessor.enabled = True
    # Configure and run out exporter
    c.NotebookExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]

    clean(path, c)
