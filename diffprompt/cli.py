import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from diffprompt.llm import run_prompt
from diffprompt.differ import compute_diff, compute_similarity

console = Console()

@click.group()
def main():
    """diffprompt — compare LLM behaviour across prompt variations."""
    pass

@main.command()
@click.option("--a", required=True, help="First prompt")
@click.option("--b", required=True, help="Second prompt")
@click.option("--model", default="llama-3.3-70b-versatile", help="Groq model to use")
def diff(a, b, model):
    """Run two prompts and show a diff of their outputs."""

    console.print(Panel(f"[bold]Prompt A:[/bold] {a}", style="cyan"))
    console.print(Panel(f"[bold]Prompt B:[/bold] {b}", style="magenta"))

    with console.status("Running Prompt A..."):
        output_a = run_prompt(a, model)

    with console.status("Running Prompt B..."):
        output_b = run_prompt(b, model)

    console.print("\n[bold cyan]Output A:[/bold cyan]")
    console.print(Panel(output_a, style="cyan"))

    console.print("\n[bold magenta]Output B:[/bold magenta]")
    console.print(Panel(output_b, style="magenta"))

    diff_result = compute_diff(output_a, output_b)

    similarity = compute_similarity(output_a, output_b)
    score_color = "green" if similarity > 0.7 else "yellow" if similarity > 0.4 else "red"
    console.print(f"\n[bold {score_color}]Similarity score: {similarity:.0%}[/bold {score_color}]")

    if not diff_result.strip():
        console.print("\n[bold green]✓ Outputs are identical[/bold green]")
    else:
        console.print("\n[bold yellow]Diff:[/bold yellow]")
        text = Text()
        for line in diff_result.splitlines():
            if line.startswith("+"):
                text.append(line + "\n", style="green")
            elif line.startswith("-"):
                text.append(line + "\n", style="red")
            else:
                text.append(line + "\n", style="dim")
        console.print(Panel(text))