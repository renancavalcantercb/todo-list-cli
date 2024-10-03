import typer
import json
import os

app = typer.Typer()

TODO_FILE = "todo.json"


def create_todo_file():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as file:
            json.dump([], file)


def add_task(title: str):
    """Add a new task to the todo list"""
    create_todo_file()

    with open(TODO_FILE, "r") as file:
        data = json.load(file)

    data.append({"id": len(data) + 1, "title": title, "done": False})

    with open(TODO_FILE, "w") as file:
        json.dump(data, file, indent=4)

    typer.echo(f"Task '{title}' added!")


def remove_task(identifier: str):
    """Remove a task by title or id"""
    create_todo_file()

    with open(TODO_FILE, "r") as file:
        data = json.load(file)

    found = False
    for task in data:
        if task["title"] == identifier or str(task["id"]) == identifier:
            data.remove(task)
            found = True
            break

    if found:
        with open(TODO_FILE, "w") as file:
            json.dump(data, file, indent=4)
        typer.echo(f"Task '{identifier}' removed!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def check_task(identifier: str):
    """Check a task as done"""
    create_todo_file()

    with open(TODO_FILE, "r") as file:
        data = json.load(file)

    found = False
    for task in data:
        if task["title"] == identifier or str(task["id"]) == identifier:
            task["done"] = True
            found = True
            break

    if found:
        with open(TODO_FILE, "w") as file:
            json.dump(data, file, indent=4)
        typer.echo(f"Task '{identifier}' checked!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def uncheck_task(identifier: str):
    """Uncheck a task"""
    create_todo_file()

    with open(TODO_FILE, "r") as file:
        data = json.load(file)

    found = False
    for task in data:
        if task["title"] == identifier or str(task["id"]) == identifier:
            task["done"] = False
            found = True
            break

    if found:
        with open(TODO_FILE, "w") as file:
            json.dump(data, file, indent=4)
        typer.echo(f"Task '{identifier}' unchecked!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def list_tasks():
    """List all tasks"""
    create_todo_file()

    with open(TODO_FILE, "r") as file:
        data = json.load(file)

    if data:
        typer.echo("Todo list:")
        for task in data:
            done_status = "✔" if task["done"] else "✘"
            typer.echo(f"{task['id']}: {task['title']} - Done: {done_status}")
    else:
        typer.echo("No tasks found!")


def interactive_shell():
    """Enter an interactive mode"""
    typer.echo(
        "Welcome to the todo CLI! Type commands (add, remove, check or list) or 'exit' to quit."
    )

    while True:
        try:
            command = input("> ").strip()
            if command == "exit":
                typer.echo("Exiting...")
                break

            elif command.startswith("add "):
                title = command[4:]
                add_task(title)

            elif command.startswith("check "):
                identifier = command[6:]
                check_task(identifier)

            elif command.startswith("uncheck "):
                identifier = command[8:]
                uncheck_task(identifier)

            elif command.startswith("remove "):
                identifier = command[7:]
                remove_task(identifier)

            elif command == "list" or command == "ls":
                list_tasks()

            else:
                typer.echo(f"Unknown command: {command}")
        except (KeyboardInterrupt, EOFError):
            typer.echo("\nExiting...")
            break


@app.command()
def start_shell():
    """Start the interactive mode"""
    interactive_shell()


if __name__ == "__main__":
    app()
