"""
Необходимо создать API для управления списком задач.
Каждая задача должна содержать заголовок и описание.
Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
Для этого использовать библиотеку Pydantic.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
import pandas as pd
from hw.work5.model import Tasks

app = FastAPI()

templates = Jinja2Templates(directory='hw/work5/templates')

list_ = []


@app.get('/tasks/', response_class=HTMLResponse)
def list_of_tasks(requ: Request):
	table = pd.DataFrame([vars(task) for task in list_]).to_html()
	return templates.TemplateResponse('tasks_html.html', {'request': requ, 'table': table})


@app.get('/tasks/{num}', response_model=Tasks)
def select_task(num: int):
	task_num = [task for task in list_ if task.id == num]
	return task_num[0]


@app.post('/tasks/', response_model=Tasks)
def set_task(task: Tasks):
	task.id = len(list_) + 1
	list_.append(task)
	return task


@app.put('/tasks/{id}', response_model=Tasks)
def update_task(id: int, task: Tasks):
	task_num = [task_ for task_ in list_ if task.id == id]
	task.id = id
	list_[id-1] = task
	return task

