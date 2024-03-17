import flet as ft 

def main (page: ft.Page):
    #funcion del boton
    def add_task(e):
        check = ft.Checkbox(label=task_name.value)
        page.add(check)
        task_name.value = ""
        task_name.focus
        page.update

    task_name = ft.TextField(label="Enter the task")
    add_but = ft.ElevatedButton(text= "Add task", on_click=add_task)
    appText = ft.Text("To Do App", size= 50)
    page.add(appText)
    page.add(task_name, add_but)

ft.app(target=main)