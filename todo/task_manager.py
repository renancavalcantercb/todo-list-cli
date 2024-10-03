from .file_utils import load_todo_file, save_todo_file
import typer


def find_task(data, identifier):
    """Find a task by title or id"""
    for task in data:
        if task["title"] == identifier or str(task["id"]) == identifier:
            return task
    return None


def add_task(title: str):
    """Add a new task to the todo list"""
    data = load_todo_file()

    data.append({"id": len(data) + 1, "title": title, "done": False})

    save_todo_file(data)
    typer.echo(f"Task '{title}' added!")


def remove_task(identifier: str):
    """Remove a task by title or id"""
    data = load_todo_file()

    task = find_task(data, identifier)

    if task:
        data.remove(task)
        save_todo_file(data)
        typer.echo(f"Task '{identifier}' removed!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def check_task(identifier: str):
    """Check a task as done"""
    data = load_todo_file()

    task = find_task(data, identifier)

    if task:
        task["done"] = True
        save_todo_file(data)
        typer.echo(f"Task '{identifier}' checked!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def uncheck_task(identifier: str):
    """Uncheck a task"""
    data = load_todo_file()

    task = find_task(data, identifier)

    if task:
        task["done"] = False
        save_todo_file(data)
        typer.echo(f"Task '{identifier}' unchecked!")
    else:
        typer.echo(f"No task found with title or id '{identifier}'")


def list_tasks():
    """List all tasks"""
    data = load_todo_file()

    if data:
        typer.echo("Todo list:")
        for task in data:
            done_status = "✔" if task["done"] else "✘"
            typer.echo(f"{task['id']}: {task['title']} - Done: {done_status}")
    else:
        typer.echo("No tasks found!")
