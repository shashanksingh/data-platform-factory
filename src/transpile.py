import click
import glob
from src.dag.dag_factory import DAGFactory


@click.command()
@click.option(
    "--url", prompt="URL to Crawl", required=True, help="The URL you want us to crawl"
)
def transpile(directory: str) -> None:
    """
    CLI interface for .
    :param dir: URL that needs to be crawled, and push it to queue
    :return: True or False depending on whether it was able to crawl url
    """
    click.echo(f"Hello {directory}!!")
    files = glob.glob(f"{directory}/*.toml")
    dag_factory = DAGFactory()
    for file in files:
        output = dag_factory.render(dag_factory.read_etl_description(file_path=file))
        with open("build/{file.split('.')[0]}.py", mode="w") as file_context:
            file_context.write(output)


if __name__ == "__main__":
    transpile()
