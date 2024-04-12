import click
import glob
from pathlib import Path
from src.dag.dag_factory import DAGFactory


@click.command()
@click.option(
    "--directory",
    prompt="Directory to Crawl",
    required=True,
    help="The directory containing the TOML files",
)
def generate_dags(directory: str) -> None:
    """
    CLI interface for .
    :param directory: The directory containing the TOML files
    :return: True or False depending on whether it was able to crawl url
    """
    click.echo(f"Hello {directory}!!")
    files = glob.glob(f"{directory}/*.toml")
    dag_factory = DAGFactory()
    for file in files:
        output = dag_factory.render(dag_factory.read_etl_description(file_path=file))
        filename = Path(file).name
        with open(f"build/{filename.split('.')[0]}.py", mode="w") as file_context:
            file_context.write(output)


if __name__ == "__main__":
    generate_dags()
