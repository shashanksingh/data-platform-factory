import click
import glob
from src.dag.dag_factory import DAGFactory

COUNT_OF_ITEMS_WITH_ONE_SUBDIRECTORY: int = 2


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
    files = glob.glob(f"{directory}/**/*.toml")
    dag_factory = DAGFactory()
    for file in files:
        dag_description = dag_factory.read_etl_description(file_path=file)
        output = dag_factory.render(dag_description)
        if len(file.split("/")) > COUNT_OF_ITEMS_WITH_ONE_SUBDIRECTORY:
            project_name = file.split("/")[1]
        else:
            raise Exception("Project Name as subdirectory is needed")
        dag_name = dag_factory.generate_dag_name(dag_description)
        with open(f"dags/{dag_name}_for_{project_name}.py", mode="w") as file_context:
            file_context.write(output)


if __name__ == "__main__":
    generate_dags()
